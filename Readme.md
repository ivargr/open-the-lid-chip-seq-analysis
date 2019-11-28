# Reproducing the ChIP-seq analysis
The following is a guide on how to run the scripts used to do the ChIP-seq analysis in **Open the LID: LXRα regulates ChREBPα transactivity in a
target gene-specific manner through an agonist-modulated LBD-
LID interaction**.

## Prerequisites
### Data
* The mm9 reference genome, downloaded [from here](https://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/mm9.2bit) and converted to fasta. Needs to be indexed with `bwa index`.
* LXR raw reads (downloaded from the NCBI SRA archive with SRA ID [SRX118172](https://www.ncbi.nlm.nih.gov/sra?term=SRX118172))
* ChREBP sequencing reads (not available online, these were provided to us by by Prof. Lawrence Chan)
* mm9 blacklisted regions, [available here](http://mitra.stanford.edu/kundaje/akundaje/release/blacklists/mm9-mouse/mm9-blacklist.bed.gz)
* PPARalpha peaks downloaded from [this NCBI GEO archive](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM864671)
* FXR peaks downloaded from [this NCBI GEO archive](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1899651)

### Software
The following software are needed:
* MACS2 (for peak calling)
* BWA (for aligning raw reads)
* Python3 (for analysis)
* [Rgmatch](https://bitbucket.org/pfurio/rgmatch/src) (to associate transcription factors to genes and gene elements)

## Scripts for reproducing the analysis
### Step 1: Run peak calling
The following scripts run peak calling for LXR and ChREBP. For PPARalpha and FXR, called peaks available at NCBI were used in the analysis, since these already were called using the same pipeline that we use here.

The following script assumes you have two files `chrebp_sample_reads.bed`  and `chrebp_control_reads.bed` in this directory.

```bash
./run_chrepb_peak_calling.sh
```

For LXR, the raw reads are downloaded from NCBI SRA archive (see link at the top). We map these to the MM9 reference genome with the following script:
```bash
./map_lxr_reads.sh
```

After mapping, this script performs the peak calling:
```bash
./run_lxr_peak_calling.sh
```

### Step 2: Find pairs of close ChREBP and LXR peaks

The following script finds pairs of close ChREBP and LXR peaks:
```bash
./find_close_tf_peaks.sh
```
The resulting file `tfs_close.bed` contains the pairs of close transcription factors.

### Step 3: Run Rgmatch
```bash
python3 rgmatch.py --report gene --distance 25 --promoter 5000 -g gencode.vM1.annotation.gtf -b tfs_close.bed -G gene_name -o gene_associations_tmp.csv

# Since Rgmatch does not divide between near/far, we do this manually with the following script
python3 divide_rgmatch_results_into_near_and_far.py gene_associations_tmp.csv > gene_associations_gene_level.csv

# Finally, we add peak to peak distance (using the tfs_close.bed file generated in step 2):
python3 add_peak_distance_to_gene_associtaions.py tfs_close.bed gene_associations_gene_level.csv > gene_associations_gene_level_with_peak_to_peak_distance.csv
```

The final csv file `gene_associations_gene_level_with_peak_to_peak_distance.csv` is used to generated Figure 1.

