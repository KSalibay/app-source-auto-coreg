# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
#THIS IS A DRAFT DO NOT RUN YET

# Author: Kami Salibayeva
# Indiana University

# set up environment
import os
import json
import mne
from mne.coreg import Coregistration
from mne.io import read_info
import numpy as np

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

#Read the file in
fname_epo = config['epo']

#Read the subject
subject = config['subject']

#Read the subject dir
subj_dir = config['subj_dir']

info = read_info(fname_epo)
plot_kwargs = dict(
    subject=subject,
    subjects_dir=subj_dir,
    surfaces="head-dense",
    dig=True,
    eeg=[],
    meg="sensors",
    show_axes=True,
    coord_frame="meg",
)
view_kwargs = dict(azimuth=45, elevation=90, distance=0.6, focalpoint=(0.0, 0.0, 0.0))

fiducials = "estimated"  # get fiducials from fsaverage
coreg = Coregistration(info, subject, subj_dir, fiducials=fiducials)

coreg.fit_fiducials(verbose=True)

coreg.fit_icp(n_iterations=6, nasion_weight=2.0, verbose=True)
coreg.omit_head_shape_points(distance=5.0 / 1000)  # distance is in meters
fig = mne.viz.plot_alignment(info, trans=coreg.trans, **plot_kwargs)

if config['final'] == True:
    coreg.fit_icp(n_iterations=20, nasion_weight=10.0, verbose=True)
    fig = mne.viz.plot_alignment(info, trans=coreg.trans, **plot_kwargs)
    mne.viz.set_3d_view(fig, **view_kwargs)

    dists = coreg.compute_dig_mri_distances() * 1e3  # in mm
    print(
        f"Distance between HSP and MRI (mean/min/max):\n{np.mean(dists):.2f} mm "
        f"/ {np.min(dists):.2f} mm / {np.max(dists):.2f} mm"
    )

    