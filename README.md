# lr_stix_analysis

## TODO:
- Get short read sample depths
- Get CMRG TEs
- STaffr AF

## Fig 3

| | | |
|-|-|-|
|![](img/stix_lr_vs_sr_pop_freq.png) r = 0.80, p=0.00e+00 | ![](img/stix_lr_vs_1kg_pop_freq.png) r = 0.80, p=0.00e+00 | ![](img/stix_lr_vs_1kg_pop_freq_diff.hist.png)|
|![](img/staffr_lr_vs_1kg_af_freq.png) r = 0.75, p=0.00e+00 | ![](img/stix_sr_vs_1kg_pop_freq.png) r = 0.90, p=0.00e+00 | ![](img/stix_sr_vs_1kg_pop_freq_diff.hist.png)|


## Fig 4

| | |
|-|-|
| ![](img/stix_lr_hg002_vs_gnomad_pop_freq.png) | ![](img/stix_sr_hg002_vs_gnomad_pop_freq.png) |
| ![](img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png) | ![](img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png) |

## Fig 5

| | |
|-|-|
| | ![](img/lr_cosmic_freq_fixed_bins_t_5.png)

## Fig 6

| | |
|-|-|
| | |
|![](img/lr_te_tech_upset_t_5.png)    | ![](img/lr_te_freq_fixed_bins_t_5.png) |
|![](img/stix_lr_te_depth_v_freq.png) r = 0.93, p=0.00e+00 | ![](img/stix_sr_te_depth_v_freq.png) r = 0.73, p=0.00e+00 | 

## Figures

## STIX vs 1KG SV frequency

| |Log scale | Linear scale |
|-|----------|--------------|
| Long  |![](img/stix_lr_vs_1kg_pop_freq.png) | ![](img/stix_lr_vs_1kg_pop_freq.no_log.png)|
|       | ![](img/stix_lr_vs_1kg_pop_freq_diff.hist.png) || 
| Short |![](img/stix_sr_vs_1kg_pop_freq.png) | ![](img/stix_sr_vs_1kg_pop_freq.no_log.png)|
| Both  |![](img/stix_lr_sr_vs_1kg_pop_freq.png) | ![](img/stix_lr_sr_vs_1kg_pop_freq.no_log.png)|


<details>
    
#### Long read
```
python src/hex_plot.py \
    --stix data/lr_1kg_pop_freq_t_5.bed \
    --other data/1kg_pop_freq.lr_samples.bed \
    --out img/stix_lr_vs_1kg_pop_freq.png \
    --merged data/stix_lr_vs_1kg_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX long-read depth => 5" \
    --title "1KG germline SVs"

cat data/stix_lr_vs_1kg_pop_freq.bed\
| awk '{print ($5-$6)/(($5+$6)/2)}' \
| python src/hist.py \
    --bins 50 \
    --out_file img/stix_lr_vs_1kg_pop_freq_diff.hist.png \
    --xlabel '% diff in non-ref and STIX long-read depth counts' \
    --ylabel 'Frequency'

cat stix_lr_vs_1kg_pop_freq.bed \
| wc -l
   70144

cat data/stix_lr_vs_1kg_pop_freq.bed | cut -f 4 | sort | uniq -c | sort -nr
52479 DEL
17214 DUP
 294 INV
 157 INS

cat data/stix_lr_vs_1kg_pop_freq.bed | awk '{print $3-$2}' | median
    626,467

cat data/stix_lr_vs_1kg_pop_freq.bed \
| awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}' \
| awk '$7<=-1'\
| awk '{print $3-$2}'\
| median
    271,216

cat data/stix_lr_vs_1kg_pop_freq.bed \
| awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}' \
| awk '$7>=1'\
| awk '{print $3-$2}'\
| median
    6113,3476


cat data/stix_lr_vs_1kg_pop_freq.bed  | awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}'  | awk '$7<=-1' | wc -l
    7680

calc 7680/70144
    0.109489051094891

cat data/stix_lr_vs_1kg_pop_freq.bed  | awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}'  | awk '$7>=1' | wc -l
   15789

calc 15789/70144
    0.225094092153285

cat data/stix_lr_vs_1kg_pop_freq.bed \
 | awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}' \
 | awk '$7>-1 && $7<1' \
 | wc -l
   46675

calc 46675/70144
   0.665416856751825

cat data/stix_lr_vs_1kg_pop_freq.bed \
| awk '{OFS="\t"; print $0,($5-$6)/(($5+$6)/2)}' \
| awk '$7>-1 && $7<1'\
| cut -f 7 
| mean
0.0215880195354463,0.305436256954978


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
    --merged data/stix_sr_vs_1kg_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "Num. samples called non-ref by 1KG" \
    --ylabel "Num. of samples with STIX short-read depth => 5" \
    --title "1KG germline SVs"

cat data/stix_sr_vs_1kg_pop_freq.bed \
| awk '$5+$6 > 0' \
| awk '{print ($5-$6)/(($5+$6)/2)}' \
| python src/hist.py \
    --bins 50 \
    --out_file img/stix_sr_vs_1kg_pop_freq_diff.hist.png \
    --xlabel '% diff in non-ref and STIX short-read depth counts' \
    --ylabel 'Frequency'


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
    --merged data/stix_lr_vs_sr_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth => 5" \
    --ylabel "Num. of samples with STIX long-read depth => 5" \
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

| | Long Reads | Short Reads (DELS)|
|-|-|-|
| HG002 all  | ![](img/stix_lr_hg002_vs_gnomad_pop_freq.png) | ![](img/stix_sr_hg002_vs_gnomad_pop_freq.png)|
| HG002 CMRG | ![](img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png) | ![](img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png)|

<details>

```
cat data/lr_hg002_pop_freq_t_5.bed \
| awk '$4=="INS" || $3-$2>=50' \
> data/lr_hg002_pop_freq_t_5.len_gte_50.bed

python src/hex_plot.py \
    --stix data/lr_hg002_pop_freq_t_5.bed \
    --other data/HG002.gnomadAF.uniq.bed \
    --out img/stix_lr_hg002_vs_gnomad_pop_freq.png \
    --merged data/stix_lr_hg002_vs_gnomad_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "SV AF by SVAFotate" \
    --ylabel "Num. of samples with STIX long-read depth => 5" \
    --title "HG002 SVs" \
    --color Blues

cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | wc -l
   26122
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | awk '$6>0' | wc -l
    8744
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | awk '$5>0' | wc -l
   25064

calc 8744/26122
    0.334737003292244
calc 25064/26122
    0.95949774136743

cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep INS | wc -l
   15917
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep INS | awk '$6>0' | wc -l
    2760
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep INS | awk '$5>0' | wc -l
   15082

calc 2760/15917
    0.173399509957907
calc 15082/15917

cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep DEL | wc -l
   10205
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep DEL | awk '$6>0' | wc -l
    5984    
cat data/stix_lr_hg002_vs_gnomad_pop_freq.bed | grep DEL | awk '$5>0' | wc -l
   9982

calc 5984/10205
    0.586379225869672
calc 9982/10205
    0.978147966682999

python src/hex_plot.py \
    --stix data/lr_hg002_cmrg_pop_freq_t_5.bed \
    --other data/HG002.cmrg.gnomadAF.bed \
    --out img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png \
    --merged data/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "SV AF by SVAFotate" \
    --ylabel "Num. of samples with STIX long-read depth => 5" \
    --title "HG002 CMRG SVs" \
    --color-scale 0,5 \
    --color Blues

cat data/sr_hg002_pop_freq_t_5.bed | wc -l
   10205
cat data/sr_hg002_pop_freq_t_5.bed  | awk '$5>0' | wc -l
    9896
calc 9896/10205
    0.969720725134738

python src/hex_plot.py \
    --stix data/sr_hg002_pop_freq_t_5.bed \
    --other data/HG002.gnomadAF.DEL.bed \
    --out img/stix_sr_hg002_vs_gnomad_pop_freq.png \
    --merged data/stix_sr_hg002_vs_gnomad_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "SV AF by SVAFotate" \
    --ylabel "Num. of samples with STIX short-read depth => 5" \
    --title "HG002 DELs" \
    --color Blues

python src/hex_plot.py \
    --stix data/sr_hg002_cmrg_pop_freq_t_5.bed \
    --other data/HG002.cmrg.gnomadAF.DEL.bed \
    --out img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png \
    --merged data/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "SV AF by SVAFotate" \
    --ylabel "Num. of samples with STIX short-read depth > 5" \
    --title "HG002 CMRG DELs" \
    --color-scale 0,5 \
    --color Blues

```

</details>

## STIX COSMIC freq

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

</details>



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
    --other data/lr_te_pop_freq_t_2.bed \
    --out img/stix_lr_te_depth_v_freq.png \
    --merged data/stix_.r_te_depth_v_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX long-read depth => 2" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs" \
    --color "Greens"
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
    --other data/sr_te_pop_freq_t_4.bed \
    --out img/stix_sr_te_depth_v_freq.png \
    --merged data/stix_sr_te_depth_v_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "Num. of samples with STIX short-read depth => 4" \
    --ylabel "Mean SV evidence depth / coverage " \
    --title "TE SVs" \
    --color "Greens"

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
    --xlabel "% of samples with long-read depth => 5"\
    --ylabel "Number of TEs" \
    --title "TE SVs" \
    --width 5 \
    --height 4



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

cat  data/lr_te_pop_freq_by_tech_hprc_ont_vienna_t_5.bed \
| python src/upset_plot.py \
    --out_file img/lr_te_tech_upset_t_5.png

python src/group_hist.py \
    --in_file data/lr_te_pop_freq_t_5.bed \
    --out_file img/lr_te_pop_freq_total_seen_t_5.png \
    --title "TE SVs" \
    --xlabel "Length (KB)" \
    --ylabel "Freq." 
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

#### HG002


<details>

```
cat data/GRCh38_HG002-T2TQ100-V1.0_stvar.addID.svafotate.STIXanno_minreads5.slop100.results \
| python src/get_gnomad_af.py  \
> data/HG002.gnomadAF.bed

cat data/HG002_GRCh38_difficult_medical_gene_SV_benchmark_v0.01_trusted_SVTYPE.addID.svafotate.slop100.results \
| python src/get_gnomad_af.py  \
> data/HG002.cmrg.gnomadAF.bed

python src/get_pop_freq.py \
    --t 5 \
    --lr data/GRCh38_HG002-T2TQ100-V1.0_stvar.addID.svafotate.STIXanno_minreads5.slop100.results \
> data/lr_hg002_pop_freq_t_5.bed


python src/get_pop_freq.py \
    --t 5 \
    --lr data/HG002.SV.benchmark.gt50.noGT0.slop100.results \
> data/lr_hg002_pop_freq_t_5.bed

cat data/HG002.SV.benchmark.gt50.noGT0.slop100.results \
| python src/get_gnomad_af.py  \
> data/HG002.gnomadAF.bed



cat data/lr_hg002_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_hg002_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --t 1 \
    --lr data/GRCh38_HG002-T2TQ100-V1.0_stvar.addID.svafotate.STIXanno_minreads5.slop100.results \
> data/lr_hg002_pop_freq_t_1.bed


cat data/lr_hg002_pop_freq_t_1.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_hg002_pop_freq_t_1.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --t 5 \
    --lr data/HG002_GRCh38_difficult_medical_gene_SV_benchmark_v0.01_trusted_SVTYPE.addID.svafotate.slop100.results \
> data/lr_hg002_cmrg_pop_freq_t_5.bed

cat data/lr_hg002_cmrg_pop_freq_t_5.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_hg002_cmrg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."

python src/get_pop_freq.py \
    --t 1 \
    --lr data/HG002_GRCh38_difficult_medical_gene_SV_benchmark_v0.01_trusted_SVTYPE.addID.svafotate.slop100.results \
> data/lr_hg002_cmrg_pop_freq_t_1.bed

cat data/lr_hg002_cmrg_pop_freq_t_1.bed \
| cut -f 5 \
| python src/hist.py \
    --out_file img/lr_hg002_cmrg_pop_freq_t_1.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."


bedtools groupby \
    -i <(cat data/HG002.gnomadAF.bed| sort) \
    -g 1,2,3,4 \
    -c 5 \
    -o max \
| wc -l
    26122

bedtools groupby \
    -i <(cat data/HG002.gnomadAF.bed| sort) \
    -g 1,2,3,4 \
    -c 5 \
    -o max \
| awk '$5>0' \
| wc -l
    8744

bedtools groupby \
    -i <(cat data/HG002.gnomadAF.bed| sort) \
    -g 1,2,3,4 \
    -c 5 \
    -o max \
> data/HG002.gnomadAF.uniq.bed


calc 8744/26122
    0.334737003292244

cat data/lr_hg002_pop_freq_t_5.bed | wc -l
    26122

cat data/lr_hg002_pop_freq_t_5.bed | awk '$5>0' | wc -l
    25064

calc 25064/26122
    0.95949774136743





```

</details>

| Experiment | Histogram |
|------------|-----------|
| Long Read, HG002 SVs, samples with depth > 5 | ![](img/lr_hg002_pop_freq_t_5.hist.png) |
| Long Read, HG002 SVs, samples with depth > 1 | ![](img/lr_hg002_pop_freq_t_1.hist.png) |
| Long Read, HG002 CMRG SVs, samples with depth > 5 | ![](img/lr_hg002_cmrg_pop_freq_t_5.hist.png) |
| Long Read, HG002 CMRG SVs, samples with depth > 1 | ![](img/lr_hg002_cmrg_pop_freq_t_1.hist.png) |

#### TEs

<details>

```
python src/get_pop_freq_by_tech.py \
    --t 5 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
    --samples data/ont_pb_samples.txt \
> data/lr_te_pop_freq_by_tech_hprc_ont_vienna_t_5.bed

python src/get_pop_freq.py \
    --t 5 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
> data/lr_te_pop_freq_t_5.bed

python src/get_pop_freq.py \
    --t 2 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
> data/lr_te_pop_freq_t_2.bed

python src/get_pop_freq.py \
    --t 2 \
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

cat data/lr_te_mean_depth.bed \s
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

cat data/LR_1kg_queries_sampleswise_agg.staffr.bed \
| tail -n +2 \
| awk -F "\t" '$13<=0.05' \
| cut -f 1,2,5,7,12 \
> data/lr_1kg_staffr_q.bed

cat data/lr_1kg_staffr_q.bed \
| awk '$5>0.1' \
> data/lr_1kg_staffr_q.q_gt_0.1.bed

cat data/1kg_af.bed \
| awk '$5>0.1' \
> data/1kg_af.af_gt_0.1.bed

python src/hex_plot.py \
    --stix data/lr_1kg_staffr_q.bed \
    --other data/1kg_af.bed \
    --out img/staffr_lr_vs_1kg_af_freq.png \
    --merged data/staffr_lr_vs_1kg_af_freq.bed \
    --height 4 \
    --width 5 \
    --xlabel "SV AF by 1KG" \
    --ylabel "SV AF by long-read staffr" \
    --title "1KG germline SVs"
r = 0.73, p=0.00e+00
```

</details>

| Experiment | Histogram |
|------------|-----------|
|Long Read, 1KG SVs, samples with depth > 5 | ![](img/lr_1kg_pop_freq_t_5.hist.png) |
|staffr af with Long Read, 1KG SVs, samples with depth > 5 | ![](img/staffr_lr_vs_1kg_af_freq.png) |


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

cat data/queriesSR.DEL.staffr.bed \
| awk '$9>30 && $9<40' \ 
| cut -f 1,2,3,4,9 \
| tail -n +2 \
> data/sr_1kg_staffr_q.bed

cat data/queriesSR.DUP.staffr.bed \
| cut -f 1,2,3,4,9 \
| tail -n +2 \
>> data/sr_1kg_staffr_q.bed

cat data/queriesSR.INV.staffr.bed \
| cut -f 1,2,3,4,9 \
| tail -n +2 \
>> data/sr_1kg_staffr_q.bed

cat data/sr_1kg_staffr_q.bed \
| awk '$5>0.1' \
> data/sr_1kg_staffr_q.q_gt_0.1.bed

python src/hex_plot.py \
     --stix data/sr_1kg_staffr_q.q_gt_0.1.bed \
     --other data/1kg_af.af_gt_0.1.bed \
     --out img/staffr_sr_vs_1kg_af_freq.png \
     --merged data/staffr_sr_vs_1kg_af_freq.bed \
     --height 4 \
     --width 5 \
     --xlabel "SV AF by 1KG" \
     --ylabel "SV AF by short-read staffr" \
     --title "1KG germline SVs"
r = 0.15, p=4.72e-39
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
