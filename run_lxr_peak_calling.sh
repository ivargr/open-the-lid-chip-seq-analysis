#!/usr/bin/env bash

macs2 callpeak --verbose 2 -t lxr_sample_filtered.bam -g 2150570000 -n lxr --bdg -q 0.05
macs2 bdgcmp -t lxr_treat_pileup.bdg -c lxr_control_lambda.bdg -m qpois -o lxr_qvalues.bdg
bedtools subtract -A -a lxr_peaks.narrowPeak -b mm9-blacklist.bed | bedtools sort > lxr_peaks_sorted.narrowPeak
