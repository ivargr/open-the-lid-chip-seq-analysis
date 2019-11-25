#!/usr/bin/env bash
macs2 callpeak -t chrep_sample_reads.bed -c chrebp_control_reads.bed -g 2150570000 -n chrebp --bdg -q 0.05
macs2 bdgcmp -t chrebp_treat_pileup.bdg -c chrebp_control_lambda.bdg -m qpois -o chrebp_qvalues.bdg
bedtools subtract -A -a chrebp_peaks.narrowPeak -b mm9-blacklist.bed | sort -r -n -k 9,9  | head -n 20000 | bedtools sort > chrebp_peaks_blacklisted_removed.narrowPeak
~
~
~
~
~
~
~
~
~
