# lr_stix_analysis



## Figures

## Data files

### Long-read population frequency

#### TEs
```
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

