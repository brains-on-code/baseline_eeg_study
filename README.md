# On the Influence of the Baseline in Neuroimaging Experiments on Program Comprehension

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This repository contains the preregistration, replication package, analysis scripts, and additional plots and raw data for our paper.

## Pregistration

We preregistered this study at [osf](https://osf.io/h892p/). We also include this pregistration as a pdf here: `Preregistration.pdf`.

## Replication Package

We aim to provide everything necessary to replicate our study in this repository.

### Experiment Setup

We provide the experiment setup for replicating the study in `/PsychoPy/`.

    - open the file test.psyexp in Psychopy Version 2021.2.3
    - choose the option to run the experiment without devices
    - the study supports participant numbers 1
    
We also provide the questionnaire for demographic data and programming experience: `Prequestionnaire.pdf`

### Data Analysis 
We provide the analysis protocol for replicating the data analysis in `/scripts/`.

Here, you:

    - install the requirements: requirements.txt
    - download EEGLab and Matlab
    - let the scripts run in their correct ordering: `Preprocessing01_fif_to_set.ipynb`, `Preprocessing02_ICA.m`, `Preprocessing03_data_format.ipynb`, `Preprocessing04_fixation_detection.ipynb` and `Baseline.ipynb`

## Additional Figures and Data
Finally, we provide extended versions of the figures used in the paper in `/plots/`.

    - averaged_programcomprehension_with_baseline: Figure 6 in the paper and Figures for every baseline individual with the raw and baselinecorrected graph
    - averaged_total: Figure 8 in the paper and Figures for every task type individual
    - heatmaps: The heatmaps based on the eyetracking data for all tasks, divided into ProgCompr and Baselinetasks (averaged over all participants)
    - scanpaths: The scanpaths based on the eyetracking data for all tasks for all participants (not anonymized participant numbering)
    - statistics: all statistic values presented in the paper    
    - topoplots: Topoplots averaged over all participants for all task types and for ProgCompr with respect to all baselines
    
We also provide the raw data of the response times and correctness values of the pilot study in `Pilot_Study.csv`.

# License

This repository is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

