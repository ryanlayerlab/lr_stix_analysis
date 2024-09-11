# lr_stix_analysis



## Figures

## Data files

### Long-read population frequency

#### TEs
```
python src/get_sample_list.py \
    --lr "data/LR_STIX_1kg_queries/04.3.SR_all.slop100.tmp*.results"\
> data/lr_1kg_samples.txt

python src/get_pop_freq.py \
    --t 5 \
    --lr data/02.3.MosiacTEs.unique.query.final_intersected.slop100.results \
> data/lr_te_pop_freq_t_5.bed

cat data.data/lr_te_pop_freq_t_5.bed \
| cut -f 4 \
| python src/hist.py \
    --out_file img/lr_te_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```
![](img/lr_te_pop_freq_t_5.hist.png)


#### 1KG
```
python src/get_pop_freq.py \
    --t 5 \
    --lr "data/LR_STIX_1kg_queries/04.3.SR_all.slop100.tmp*.results
> data/lr_1kg_pop_freq_t_5.bed

cat data/lr_1kg_pop_freq_t_5.bed \
| cut -f 4 \
| python src/hist.py \
    --out_file img/lr_1kg_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```
![](img/lr_1kg_pop_freq_t_5.hist.png)

### Short-read population frequency

#### TEs
```
python src/get_pop_freq.py \
    --sr "data/persample1kgqueries/queries.*.DEL.bed" \
    --t 5 > data/sr_te_pop_freq_t_5.bed

cat data/sr_te_pop_freq_t_5.bed \
| cut -f 4 \
| python src/hist.py \
    --out_file img/sr_te_pop_freq_t_5.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```
![](img/sr_te_pop_freq_t_5.hist.png)

### 1KG population frequency

```
bcftools view \
    --force-samples \
    -S data/lr_1kg_samples.txt data/1KGP_3202.gatksv_svtools_novelins.freeze_V3.wAF.vcf.gz  \
| bcftools query \
    -f "%CHROM\t%POS\t%INFO/END\t[%GT\t]\n" \
| python src/count_non_refs.py \
> data/1kg_pop_freq.lr_samples.bed

cat data/1kg_pop_freq.lr_samples.bed
| cut -f 4 \
| python src/hist.py \
    --out_file img/1kg_pop_freq.lr_samples.hist.png \
    --log \
    --xlabel "Pop Freq."\
    --ylabel "Freq."
```

![](img/1kg_pop_freq.lr_samples.hist.png)
