cat data/lr_te_pop_freq_t_5.bed \
| awk '{print $5/1109;}' \
|  python src/custom_hist.py \
    --bins 0 0.001 .01 .05 1.0 \
    --bin_names "0%" "(0%-1%]" "(1%-5%]" "(5%-100%]" \
    --out_file img/lr_te_freq_fixed_bins_t_5.png \
    --xlabel "% of samples with long-read depth > 5"\
    --ylabel "Number of TEs" \
    --title "TE SVs" \
    --height 4 \
    --width 5 \
    --fignum 5E
