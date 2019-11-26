#!/usr/bin/env bash
bwa aln mm9.fasta lxr_sample.fastq > lxr_sample.sai
bwa samse mm9.fasta lxr_sample.sai lxr_sample.fastq > lxr_sample.sam

samtools view -Su lxr_sample.sam | samtools sort - -o lxr_sample_sorted.bam
samtools view -q 30 -b lxr_sample_sorted.bam > lxr_sample_filtered.bam

