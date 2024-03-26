# app-source-auto-coreg

# Run an automated coregistration routine (iteratively, if needed)

This Brainlife App runs an automated coregistration of MEG/EEG Epochs .fif file to the anatomical MRI. The coregistration is done using the MNE-Python function `mne.coregistration` which is based on the FSL's FLIRT algorithm. The coregistration is done in an iterative manner, where the head shape is extracted from the MEG/EEG data and used to coregister the MEG/EEG data to the anatomical MRI. If the coregistration is not satisfactory, the head shape is extracted from the MRI and used to coregister the MEG/EEG data to the MRI. The process is repeated until the coregistration is satisfactory. The final coregistration is saved as a transformation matrix (*-trans.fif file) that can be used to transform the MEG/EEG data to the MRI space.

# Documentation

#### Input files are:
* a MEG/EEG Epochs file in fif format (mne/Epochs).
* a series of Boundary Element Model (BEM) files (neuro/meeg/bem file)

#### Ouput file is:
  * a transformation matrix file in fif format (if the necessary parameter for saving the output is selected when running the app)

## Authors
- Kamilya Salibayeva (ksalibay@iu.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*brainlife.io Publishing and Apps*
Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

*MNE-Python package:*  
Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  
**MEG and EEG data analysis with MNE-Python**  
Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267
      
  --

#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University
