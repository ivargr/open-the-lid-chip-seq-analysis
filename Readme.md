# Reproducing the ChIP-seq analysis
The following is a guide on how to run the scripts used to do the ChIP-seq analysis in **Open the LID: LXRα regulates ChREBPα transactivity in a
target gene-specific manner through an agonist-modulated LBD-
LID interaction**.

## Prerequisites
### Software
The following software are needed:
* MACS2 (for peak calling)
* BWA (for aligning raw reads)
* Python3 (for analysis)
* [Rgmatch](https://bitbucket.org/pfurio/rgmatch/src) (to associate transcription factors to genes and gene elements)

## Data
All the necessary data (raw reads, mapping indexes etc) for running the scripts below are available at Zenodo by following this link. 
The only exception is the mapped ChREBP reads, which were were kindly provided to us by Prof. Lawrence Chan.

## Scripts for reproducing the analysis
### Step 1: Run peak calling
The following scripts run peak calling for all the transcription factors. This script assumes you have two files `chrebp_sample_reads.bed`  and `chrebp_control_reads.bed` in this directory (these are not availale through the Zenodo data repository).

```bash
./run_chrepb_peak_calling.sh
```

For LXR, the raw reads are available through the Zenodo data repository. We map these to the MM9 reference genome with the following script:
```bash
./map_lxr_reads.sh
```

After mapping, this script performs the peak calling:
```bash
./run_lxr_peak_calling.sh
```

### Step 2: Find pairs of close ChREBP and LXR peaks

The following script finds pairs of close ChREBP and LXR peaks:

### Step 3: Run Rgmatch
```bash
python3 rgmatch.py --report gene --distance 25 --promoter 5000 -g gencode.vM1.annotation.gtf -b tfs_close.bed -G gene_name -o gene_associations_tmp.csv

# Since Rgmatch does not divide between near/far, we do this manually with the following script
python3 divide_rgmatch_results_into_near_and_far.py gene_associations_tmp.csv > gene_associations_gene_level.csv

# Finally, we add peak to peak distance (using the tfs_close.bed file generated in step 2):
python3 add_peak_distance_to_gene_associtaions.py tfs_close.bed gene_associations_gene_level.csv > gene_associations_gene_level_with_peak_to_peak_distance.csv
```

The final csv file `gene_associations_gene_level_with_peak_to_peak_distance.csv` is used to generated Figure 1.
