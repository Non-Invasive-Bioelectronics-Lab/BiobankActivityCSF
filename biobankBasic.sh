#!/bin/bash --login
#$ -cwd
#$ -l mem256

# Basic script to process a single CWA file stored in the data-sets folder on the CSF3
# This script will copy the file to your current directory, run the processing
# and then delete the file
# THIS SCRIPT SHOULD BE RUN FROM THE SCRATCH DIRECTORY

module load apps/binapps/anaconda3/2019.03
module load tools/java/1.8.0

export HDF5_USE_FILE_LOCKING=FALSE
export OMP_NUM_THREADS="1"
export _JAVA_OPTIONS="-XX:ParallelGCThreads=1 -XX:ParallelCMSThreads=1 -Xmx16G"

INFILE=XXXXXXX_90001_0_0.cwa
cp /mnt/data-sets/ukbiobank/activity-data/bulk/$INFILE .
python accProcess.py $INFILE
rm $INFILE

