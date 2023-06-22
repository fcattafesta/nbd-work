#!/bin/bash

# Define the Python script to run
PYTHON_SCRIPT="single_file.py"

# Define the directory containing the files
DIRECTORY="/gpfs/ddn/srm/cms//store/mc/RunIISummer20UL18NanoAODv9/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/"

# Loop through the files in the directory and its subdirectories
find "$DIRECTORY" -type f -print0 | while read -d $'\0' FILE; do
    echo "Running script for $FILE"
    python $PYTHON_SCRIPT "$FILE"
    if [ $? -ne 0 ]; then
        echo "Script failed for $FILE"
        exit 1
    fi
    echo "Script completed for $FILE"
done
