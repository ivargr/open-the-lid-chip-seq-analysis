#!/usr/bin/env bash

# First convert narrow peak to only summits, so that we can run Bedtools on them
python3 narrowpeak_to_summit.py chrebp_peaks_sorted.narrowPeak > chrebp_summits.bed
python3 narrowpeak_to_summit.py lxr_peaks_sorted.narrowPeak > lxr_summits.bed

# Run bedtools to find close pairs
bedtools closest -d -a lxr_summits.bed -b chrebp_summits.bed | awk '$13 < 1000' | sort -n -k 13 > close.txt
python3 parse_bedtools_output.py close.txt tfs_close.bed




