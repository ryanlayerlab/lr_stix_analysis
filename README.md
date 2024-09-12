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


## Figures

### 1KG SV frequency

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




## Data files

### Long-read population frequency

#### TEs
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
```
![](img/lr_te_pop_freq_t_5.hist.png)


#### 1KG
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
![](img/lr_1kg_pop_freq_t_5.hist.png)

#### Cosmic
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
```
![](img/lr_cosmic_pop_freq_t_5.bed.hist.png)

### Short-read population frequency

#### TEs
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
```
![](img/sr_te_pop_freq_t_5.hist.png)
#### 1KG
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

| DEL | DUP | INV | All|
|-----|-----|-----|----|
| ![](img/sr_1kg_DEL_pop_freq_t_5.hist.png) | ![](img/sr_1kg_DUP_pop_freq_t_5.hist.png) | ![](img/sr_1kg_INV_pop_freq_t_5.hist.png) | ![](img/sr_1kg_pop_freq_t_5.hist.png) |

#### HG002
```
python src/get_pop_freq.py \
    --sr "data/persample1kgqueries/queries.*.DEL.bed" \
    --t 5 > data/sr_te_pop_freq_t_5.bed
```

#### HG002 CMRG

### Joint population frequency
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

## 1KG population frequency

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

![](img/1kg_pop_freq.lr_samples.hist.png)
