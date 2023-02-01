# Baselinestudy_Replication_Package
This repository contains:
- the analysis protocol: /scripts/
    - install the requirements: requirements.txt
    - download EEGLab and Matlab
    - let the scripts run in their correct ordering: Preprocessing01_fif_to_set.ipynb, Preprocessing02_ICA.m, Preprocessing03_data_format.ipynb, Preprocessing04_fixation_detection.ipynb and Baseline.ipynb
- the experiment setup: /PsychoPy/
    - open the file test.psyexp in Psychopy Version 2021.2.3
    - choose the option to run the experiment without devices
    - the study supports participant numbers 1
- the extended versions of the figures used in the paper: /plots/
    - averaged_programcomprehension_with_baseline: Figure 6 in the paper and Figures for every baseline individual with the raw and baselinecorrected graph
    - averaged_total: Figure 8 in the paper and Figures for every task type individual
    - heatmaps: The heatmaps based on the eyetracking data for all tasks, divided into ProgCompr and Baselinetasks (averaged over all participants)
    - scanpaths: The scanpaths based on the eyetracking data for all tasks for all participants (not anonymized participant numbering)
    - statistics: all statistic values presented in the paper    
    - topoplots: Topoplots averaged over all participants for all task types and for ProgCompr with respect to all baselines
- the response times and correctness values of the pilotstudy: Pilot_Study.csv
- the preregistration from osf.io: Preregistration.pdf
- the questionnaire for demographic data and programming experience: Prequestionnaire.pdf
