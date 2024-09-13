# lr_stix_analysis

## TODO:
- ~~Get STIX output for TE x STIX LR 1KG~~
- ~~Get STIX output for TE x STIX SR 1KG~~
- ~~Get STIX output for 1KG SV  x STIX LR 1KG~~
- ~~Get STIX output for 1KG SV  x STIX SR 1KG~~
- Get STIX output for COSMIC x STIX LR 1KG
- Get STIX output for COSMIC x STIX SR 1KG
- Get STIX output for HG002  x STIX LR 1KG
- Get STIX output for HG002  x STIX SR 1KG
- Get short read sample depths


## Figures

## STIX vs 1KG SV frequency

| |Log scale | Linear scale |
|-|----------|--------------|
| Long  |![](img/stix_lr_vs_1kg_pop_freq.png) | ![](img/stix_lr_vs_1kg_pop_freq.no_log.png)|
| Short |![](img/stix_sr_vs_1kg_pop_freq.png) | ![](img/stix_sr_vs_1kg_pop_freq.no_log.png)|
| Both  |![](img/stix_lr_sr_vs_1kg_pop_freq.png) | ![](img/stix_lr_sr_vs_1kg_pop_freq.no_log.png)|

<details>
    
#### Long read
```
python src/hex_plot.py \
    --stix data/lr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.lr_samples.bed \
    --out img/stix_lr_vs_1kg_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "1KG germline SVs"

python src/hex_plot.py \
    --color-scale 0,1100 \
    --stix data/lr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.lr_samples.bed \
    --out img/stix_lr_vs_1kg_pop_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "1KG germline SVs"

r = 0.80, p=0.00e+00
```

#### Short read
```
python src/hex_plot.py \
    --stix data/sr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.sr_samples.bed \
    --out img/stix_sr_vs_1kg_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX short-read depth > 5" \
    --title "1KG germline SVs"

python src/hex_plot.py \
    --color-scale 0,2504 \
    --stix data/sr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.sr_samples.bed \
    --out img/stix_sr_vs_1kg_pop_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX short-read depth > 5" \
    --title "1KG germline SVs"

r = 0.90, p=0.00e+00
```

#### Long and Short read
```
python src/hex_plot.py \
    --stix data/lr_sr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.lr_sr_samples.bed \
    --out img/stix_lr_sr_vs_1kg_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX short- or long-read depth > 5" \
    --title "1KG germline SVs"

python src/hex_plot.py \
    --color-scale 0,2504 \
    --stix data/lr_sr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.lr_sr_samples.bed \
    --out img/stix_lr_sr_vs_1kg_pop_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX short- or long-read depth > 5" \
    --title "1KG germline SVs"

r = 0.90, p=0.00e+00
```

</details>

## STIX vs Long read vs Short read

|Log scale | Linear scale |
|----------|--------------|
|![](img/stix_lr_vs_sr_pop_freq.png) | ![](img/stix_lr_vs_sr_pop_freq.no_log.png)|

<details>

```
python src/hex_plot.py \
    --stix data/lr_1kg_pop_freq_t_5.bed \
    --other data/sr_1kg_pop_freq_t_5.bed \
    --out img/stix_lr_vs_sr_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth > 5" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "1KG germline SVs"

python src/hex_plot.py \
    --color-scale 0,1100 \
    --stix data/lr_1kg_pop_freq_t_5.bed \
    --other data/sr_1kg_pop_freq_t_5.bed \
    --out img/stix_lr_vs_sr_pop_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth > 5" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "1KG germline SVs"

r = 0.80, p=0.00e+00
```

</details>

## STIX HG002

| | Long Reads | Short Reads |
|-|-|-|
| HG002 all  | | ![](img/stix_sr_hg002_vs_gnomad_pop_freq.png)|
| HG002 CMRG | | ![](img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png)|

<details>

```
python src/hex_plot.py \
    --stix data/sr_hg002_pop_freq_t_5.bed \
    --other data/HG002.gnomadAF.DEL.bed \
    --out img/stix_sr_hg002_vs_gnomad_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Allele freq. in gnomAD" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "HG002 SVs"

python src/hex_plot.py \
    --stix data/sr_hg002_cmrg_pop_freq_t_5.bed \
    --other data/HG002.cmrg.gnomadAF.DEL.bed \
    --out img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Allele freq. in gnomAD" \
    --ylabel "Num. of samples with STIX long-read depth > 5" \
    --title "HG002 CMRG SVs"

```

</details>

## STIX COSCMIC freq

### STIX Long-read COSCMIC Pop %
| | t > 5 | t > 1 |
|--------------|-|-|
| Fixed bins   | ![](img/lr_cosmic_freq_fixed_bins_t_5.png) | ![](img/lr_cosmic_freq_fixed_bins_t_1.png) |
| Dynamic bins | ![](img/lr_cosmic_freq_fixed_bins_t_5.hist.png) | ![](img/lr_cosmic_freq_fixed_bins_t_1.hist.png) |
| Dynamic bins log scale| ![](img/lr_cosmic_freq_fixed_bins_t_5.hist.log.png) | ![](img/lr_cosmic_freq_fixed_bins_t_1.hist.log.png) |

### STIX Short-read TE Pop %


<details>

### Long-reads
```
cat data/lr_cosmic_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/lr_cosmic_freq_fixed_bins_t_5.png \
    --xlabel "% of samples with long-read depth > 5"\
    --ylabel "Number of TEs" \
    --title "COSMIC SVs"

cat data/lr_cosmic_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/lr_cosmic_freq_fixed_bins_t_1.png \
    --xlabel "% of samples with long-read depth > 1"\
    --ylabel "Number of TEs" \
    --title "COSMIC SVs"

cat data/lr_cosmic_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/lr_cosmic_freq_fixed_bins_t_5.hist.png \
    --xlabel "% of samples with long-read evidence > 5" \
    --ylabel "Freq." \
    --title "COSMIC SVs"

cat data/lr_cosmic_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/lr_cosmic_freq_fixed_bins_t_1.hist.png \
    --xlabel "% of samples with long-read evidence > 1"  \
    --ylabel "Freq." \
    --title "COSMIC SVs"

cat data/lr_cosmic_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --log \
    --out_file img/lr_cosmic_freq_fixed_bins_t_5.hist.log.png \
    --xlabel "% of samples with long-read evidence > 5" \
    --ylabel "Freq." \
    --title "COSMIC SVs"

cat data/lr_cosmic_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --log \
    --out_file img/lr_cosmic_freq_fixed_bins_t_1.hist.log.png \
    --xlabel "% of samples with long-read evidence > 1"  \
    --ylabel "Freq." \
    --title "COSMIC SVs"

```




## STIX TE freq vs depth

| |Log scale | Linear scale |
|-|----------|--------------|
|Long reads | ![](img/stix_lr_te_depth_v_freq.png) | ![](img/stix_lr_te_depth_v_freq.no_log.png)|
|Short reads | ![](img/stix_sr_te_depth_v_freq.png) | ![](img/stix_sr_te_depth_v_freq.no_log.png)|


<details>

#### Long reads
```
python src/hex_plot.py \
    --stix data/lr_te_mean_depth.bed \
    --stix_max 1.0 \
    --other data/lr_te_pop_freq_t_1.bed \
    --out img/stix_lr_te_depth_v_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX long-read depth > 0" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs"
r = 0.91, p=0.00e+00

python src/hex_plot.py \
    --color-scale 0,1100 \
    --stix data/lr_te_mean_depth.bed \
    --stix_max 1.0 \
    --other data/lr_te_pop_freq_t_1.bed \
    --out img/stix_lr_te_depth_v_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX long-read depth > 0" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs"

r = 0.80, p=0.00e+00
```

#### Short reads
```
python src/hex_plot.py \
    --stix data/sr_te_mean_depth.bed \
    --stix_max 1.0 \
    --other data/sr_te_pop_freq_t_1.bed \
    --out img/stix_sr_te_depth_v_freq.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth > 0" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs"
r = 0.12, p=8.15e-44

python src/hex_plot.py \
    --color-scale 0,1100 \
    --stix data/sr_te_mean_depth.bed \
    --stix_max 1.0 \
    --other data/sr_te_pop_freq_t_1.bed \
    --out img/stix_sr_te_depth_v_freq.no_log.png \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth > 0" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs"
```

</details>

### STIX Long-read TE Pop %
| | t > 5 | t > 1 |
|--------------|-|-|
| Fixed bins   | ![](img/lr_te_freq_fixed_bins_t_5.png) | ![](img/lr_te_freq_fixed_bins_t_1.png) |
| Dynamic bins | ![](img/lr_te_freq_fixed_bins_t_5.hist.png) | ![](img/lr_te_freq_fixed_bins_t_1.hist.png) |

### STIX Short-read TE Pop %
| | t > 5 | t > 1 |
|--------------|-|-|
| Fixed bins   | ![](img/sr_te_freq_fixed_bins_t_5.png) | ![](img/sr_te_freq_fixed_bins_t_1.png) |
| Dynamic bins | ![](img/sr_te_freq_fixed_bins_t_5.hist.png) | ![](img/sr_te_freq_fixed_bins_t_1.hist.png) |


<details>

### Long-reads
```
cat data/lr_te_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/lr_te_freq_fixed_bins_t_5.png \
    --xlabel "% of samples with long-read depth > 5"\
    --ylabel "Number of TEs" \
    --title "TE SVs"

cat data/lr_te_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/lr_te_freq_fixed_bins_t_1.png \
    --xlabel "% of samples with long-read depth > 1"\
    --ylabel "Number of TEs" \
    --title "TE SVs"

cat data/lr_te_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/lr_te_freq_fixed_bins_t_5.hist.png \
    --xlabel "% of samples with long-read evidence > 5" \
    --ylabel "Freq." \
    --title "TE SVs"

cat data/lr_te_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/lr_te_freq_fixed_bins_t_1.hist.png \
    --xlabel "% of samples with long-read evidence > 1"  \
    --ylabel "Freq." \
    --title "TE SVs"
```

### Short-reads

```
cat data/sr_te_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/sr_te_freq_fixed_bins_t_5.png \
    --xlabel "% of samples with short-read depth > 5"\
    --ylabel "Number of TEs"

cat data/sr_te_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/sr_te_freq_fixed_bins_t_1.png \
    --xlabel "% of samples with short-read depth > 1"\
    --ylabel "Number of TEs"

cat data/sr_te_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/sr_te_freq_fixed_bins_t_5.hist.png \
    --xlabel "% of samples with short-read evidence > 5" \
    --ylabel "Freq." \
    --title "TE SVs"

cat data/sr_te_pop_freq_t_1.bed \
| awk '{print $5/1109;}' \
| python src/hist.py \
    --out_file img/sr_te_freq_fixed_bins_t_1.hist.png \
    --xlabel "% of samples with short-read evidence > 1"  \
    --ylabel "Freq." \
    --title "TE SVs"
```


</details>


## Data files

### Long-reads

#### TEs

<details>

```
python src/get_pop_freq.py \
    --t 5 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
> data/lr_te_pop_freq_t_5.bed

cat data/lr_te_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_te_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --t 1 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
> data/lr_te_pop_freq_t_1.bed

cat data/lr_te_pop_freq_t_1.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_te_pop_freq_t_1.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_depth_stats.py \
    --stat mean \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
    --coverage data/lr_sample_depth.txt \
> data/lr_te_mean_depth.bed

cat data/lr_te_mean_depth.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_te_mean_depth.hist.png \
    --log \
    --xlabel "Mean Alt Evidence Depth / Coverage"\
    --ylabel "Freq."
```

</details>

| Experiment | Histogram |
|------------|-----------|
| Long Read, TE SVs, samples with depth > 5 | ![](img/lr_te_pop_freq_t_5.hist.png) |
| Long Read, TE SVs, samples with depth > 1 | ![](img/lr_te_pop_freq_t_1.hist.png) |
| Long Read, TE SVs, mean sample depth      | ![](img/lr_te_mean_depth.hist.png) | 

#### 1KG

<details>

```
python src/get_sample_list.py \
    --lr "data/LR_STIX_1kg_queries/04.3.SR_all.slop100.tmp*.results"\
> data/lr_1kg_samples.txt

python src/get_pop_freq.py \
    --t 5 \
    --adj \
    --lr "data/LR_STIX_1kg_queries/04.3.SR_all.slop100.tmp*.results" \
> data/lr_1kg_pop_freq_t_5.bed

cat data/lr_1kg_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_1kg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```

</details>

| Experiment | Histogram |
|------------|-----------|
|Long Read, 1KG SVs, samples with depth > 5 | ![](img/lr_1kg_pop_freq_t_5.hist.png) |


#### Cosmic

<details>

```
python src/get_pop_freq.py \
    --t 5 \
    --lr "data/fig.4b.Cosmic_StructuralVariants_v99_GRCh38.del.slop100.results" \
> data/lr_cosmic_pop_freq_t_5.bed

cat data/lr_cosmic_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_cosmic_pop_freq_t_5.bed.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --t 1 \
    --lr "data/fig.4b.Cosmic_StructuralVariants_v99_GRCh38.del.slop100.results" \
> data/lr_cosmic_pop_freq_t_1.bed

cat data/lr_cosmic_pop_freq_t_1.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_cosmic_pop_freq_t_1.bed.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq." \
    --title "COSMIC SVs"
```

</details>

![](img/lr_cosmic_pop_freq_t_5.bed.hist.png)
![](img/lr_cosmic_pop_freq_t_1.bed.hist.png)

### Short-reads

#### Sample depth

<details>

```
bash src/get_sr_depth.sh > data/sr_sample_depth.txt

cat data/sr_sample_depth.txt \
| cut -f 2 \
| python src/hist.py \
    --out_file img/sr_sample_depth.hist.png \
    --xlabel "Sample depth" \
    --ylabel "Freq."
```

</details>

![](img/sr_sample_depth.hist.png)

#### TEs

<details>

```
python src/get_pop_freq.py \
    --sr "data/SR_STIX_TE_queries/queries.*.DEL.bed" \
    --t 5 > data/sr_te_pop_freq_t_5.bed

cat data/sr_te_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_te_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --sr "data/SR_STIX_TE_queries/queries.*.DEL.bed" \
    --t 1 > data/sr_te_pop_freq_t_1.bed

cat data/sr_te_pop_freq_t_1.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_te_pop_freq_t_1.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."


python src/get_depth_stats.py \
    --stat mean \
    --sr "data/SR_STIX_TE_queries/queries.*.DEL.bed" \
    --coverage data/sr_sample_depth.txt \
> data/sr_te_mean_depth.bed

cat data/sr_te_mean_depth.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_te_mean_depth.hist.png \
    --log \
    --xlabel "Mean Alt Evidence Depth / Coverage"\
    --ylabel "Freq."
```

</details>

| Experiment | Histogram |
|------------|-----------|
| Short Read, TE SVs, samples with depth > 5 | ![](img/sr_te_pop_freq_t_5.hist.png) |
| Short Read, TE SVs, samples with depth > 1 | ![](img/sr_te_pop_freq_t_1.hist.png) |
| Short Read, TE SVs, mean sample depth      | ![](img/sr_te_mean_depth.hist.png) | 

#### 1KG

<details>

```
python src/get_sample_list.py \
    --sr "data/SR_STIX_1kg_queries/queries.DEL.*.txt" \
> data/sr_1kg_samples.txt

python src/get_pop_freq.py \
    --sr "data/SR_STIX_1kg_queries/queries.DEL.*.txt" \
    --t 5 > data/sr_1kg_DEL_pop_freq_t_5.bed

cat data/sr_1kg_DEL_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_1kg_DEL_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --sr "data/SR_STIX_1kg_queries/queries.DUP.*.txt" \
    --t 5 > data/sr_1kg_DUP_pop_freq_t_5.bed

cat data/sr_1kg_DUP_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_1kg_DUP_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --sr "data/SR_STIX_1kg_queries/queries.INV.*.txt" \
    --t 5 > data/sr_1kg_INV_pop_freq_t_5.bed

cat data/sr_1kg_INV_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_1kg_INV_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --sr "data/SR_STIX_1kg_queries/queries.*.txt" \
    --t 5 > data/sr_1kg_pop_freq_t_5.bed

cat data/sr_1kg_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/sr_1kg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```

</details>

| DEL | DUP | INV | All|
|-----|-----|-----|----|
| ![](img/sr_1kg_DEL_pop_freq_t_5.hist.png) | ![](img/sr_1kg_DUP_pop_freq_t_5.hist.png) | ![](img/sr_1kg_INV_pop_freq_t_5.hist.png) | ![](img/sr_1kg_pop_freq_t_5.hist.png) |

#### HG002

<details>

```
python src/get_pop_freq.py \
    --sr "data/SR_STIX_HG002_queries/HG002.raw.*.bed" \
    --t 5 > data/sr_hg002_pop_freq_t_5.bed

cat data/sr_hg002_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --title "HG002 SVs" \
    --out_file img/sr_hg002_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --sr "data/SR_STIX_HG002_queries/HG002.CMRG.raw.*.bed" \
    --t 5 > data/sr_hg002_cmrg_pop_freq_t_5.bed

cat data/sr_hg002_cmrg_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --title "HG002 SVs" \
    --out_file img/sr_hg002_cmrg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

```

| HG002 all | HG002 CMRG |
|-|-|
| ![](img/sr_hg002_pop_freq_t_5.hist.png) | ![](img/sr_hg002_cmrg_pop_freq_t_5.hist.png) |

</details>

#### HG002 CMRG

## Joint population frequency

<details>

```
python src/get_pop_freq.py \
    --t 5 \
    --adj \
    --lr "data/LR_STIX_1kg_queries/04.3.SR_all.slop100.tmp*.results" \
    --sr "data/SR_STIX_1kg_queries/queries.*.txt"\
> data/lr_sr_1kg_pop_freq_t_5.bed

cat data/lr_sr_1kg_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_sr_1kg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```
</details>

![](img/lr_sr_1kg_pop_freq_t_5.hist.png)


## 1KG population frequency

<details>

```
bcftools view \
    --force-samples \
    -S data/lr_1kg_samples.txt data/1KGP_3202.gatksv_svtools_novelins.freeze_V3.wAF.vcf.gz  \
| bcftools query \
    -f "%CHROM\t%POS\t%INFO/END\t%INFO/SVTYPE\t[%GT\t]\n" \
| python src/count_non_refs.py \
> data/1kg_pop_freq.lr_samples.bed

cat data/1kg_pop_freq.lr_samples.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/1kg_pop_freq.lr_samples.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

bcftools view \
    --force-samples \
    -S data/sr_1kg_samples.txt data/1KGP_3202.gatksv_svtools_novelins.freeze_V3.wAF.vcf.gz  \
| bcftools query \
    -f "%CHROM\t%POS\t%INFO/END\t%INFO/SVTYPE\t[%GT\t]\n" \
| python src/count_non_refs.py \
> data/1kg_pop_freq.sr_samples.bed

(cat data/lr_1kg_samples.txt; cat data/sr_1kg_samples.txt) \
| sort \
| uniq \
> data/lr_sr_1kg_samples.txt

bcftools view \
    --force-samples \
    -S data/lr_sr_1kg_samples.txt data/1KGP_3202.gatksv_svtools_novelins.freeze_V3.wAF.vcf.gz  \
| bcftools query \
    -f "%CHROM\t%POS\t%INFO/END\t%INFO/SVTYPE\t[%GT\t]\n" \
| python src/count_non_refs.py \
> data/1kg_pop_freq.lr_sr_samples.bed
```

</details>

![](img/1kg_pop_freq.lr_samples.hist.png)
