# number of tes after uniq
wcl  ../data/lr_te_pop_freq_t_5.bed
#23703

# number of tes exist in population
cat ../data/lr_te_pop_freq_t_5.bed | awk '$5>0' | wcl 
# 6100

# percentage of tes exist in population
25.7%

# number of tes larger than 1% 
cat ../data/lr_te_pop_freq_t_5.bed | awk '$5/1097 > 0.01' |wcl
2394

# percentage of common tes exist in the population
calc -p "2394/23703*100"
10.1%

