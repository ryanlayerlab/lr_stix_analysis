rule figs:
    input:
        'img/stix_lr_vs_1kg_pop_freq.png',               #fig 3B
        'img/stix_lr_vs_sr_pop_freq.png',                #fig 3C
        'img/stix_lr_hg002_vs_gnomad_pop_freq.png',      #fig 3D
        'img/stix_sr_hg002_vs_gnomad_pop_freq.png',      #fig 3F
        'img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png', #fig 3G
        'img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png', #fig 3H
        'img/lr_cosmic_freq_fixed_bins_t_5.png',         #fig 4B
        'img/lr_te_freq_fixed_bins_t_5.png',             #fig 5E
        'img/stix_lr_te_depth_v_freq.png',               #fig 5F
        'img/stix_sr_te_depth_v_freq.png'                #fig 5G

rule fig_5G:
    input:
        'data/sr_te_mean_depth.bed',
        'data/sr_te_pop_freq_t_1.bed',
    output:
        'img/stix_sr_te_depth_v_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/sr_te_mean_depth.bed \
            --stix_max 1.0 \
            --other data/sr_te_pop_freq_t_1.bed \
            --out img/stix_sr_te_depth_v_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX short-read depth > 0" \
            --ylabel "Mean SV evidence depth / coverage " \
            --title "TE SVs" \
            --fignum 5G
        """

rule fig_5F:
    input:
        'data/lr_te_mean_depth.bed',
        'data/lr_te_pop_freq_t_1.bed',
    output:
        'img/stix_lr_te_depth_v_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/lr_te_mean_depth.bed \
            --stix_max 1.0 \
            --other data/lr_te_pop_freq_t_1.bed \
            --out img/stix_lr_te_depth_v_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX long-read depth > 0" \
            --ylabel "Mean SV evidence depth / coverage " \
            --title "TE SVs" \
            --fignum 5F
        """

rule fig_5E:
    input:
        'data/lr_te_pop_freq_t_5.bed'
    output:
        'img/lr_te_freq_fixed_bins_t_5.png'
    shell:
        """
        bash src/make_fig5e.sh
        """

rule fig_4B:
    input:
        'data/lr_cosmic_pop_freq_t_5.bed'
    output:
        'img/lr_cosmic_freq_fixed_bins_t_5.png'
    shell:
        """
        bash src/make_fig4b.sh
        """

rule fig_3H:
    input:
        'data/sr_hg002_cmrg_pop_freq_t_5.bed',
        'data/HG002.cmrg.gnomadAF.DEL.bed'
    output:
        'img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/sr_hg002_cmrg_pop_freq_t_5.bed \
            --other data/HG002.cmrg.gnomadAF.DEL.bed \
            --out img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX short-read depth > 5" \
            --title "HG002 CMRG DELs" \
            --fignum 3H
        """

rule fig_3G:
    input:
        'data/lr_hg002_cmrg_pop_freq_t_5.bed',
        'data/HG002.cmrg.gnomadAF.bed'
    output:
        'img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/lr_hg002_cmrg_pop_freq_t_5.bed \
            --other data/HG002.cmrg.gnomadAF.bed \
            --out img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX long-read depth > 5" \
            --title "HG002 CMRG SVs" \
            --fignum 3G
        """

rule fig_3F:
    input:
        'data/sr_hg002_pop_freq_t_5.bed',
        'data/HG002.gnomadAF.DEL.bed'
    output:
        'img/stix_sr_hg002_vs_gnomad_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/sr_hg002_pop_freq_t_5.bed \
            --other data/HG002.gnomadAF.DEL.bed \
            --out img/stix_sr_hg002_vs_gnomad_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX short-read depth > 5" \
            --title "HG002 DELs" \
            --fignum 3F
        """

rule fig_3D:
    input:
        'data/lr_hg002_pop_freq_t_5.bed',
        'data/HG002.gnomadAF.bed',
    output:
        'img/stix_lr_hg002_vs_gnomad_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/lr_hg002_pop_freq_t_5.bed \
            --other data/HG002.gnomadAF.bed \
            --out img/stix_lr_hg002_vs_gnomad_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX long-read depth > 5" \
            --title "HG002 SVs" \
            --fignum 3D
        """

rule fig_3C:
    input:
        'data/lr_1kg_pop_freq_t_5.bed',
        'data/sr_1kg_pop_freq_t_5.bed'
    output:
        'img/stix_lr_vs_sr_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/lr_1kg_pop_freq_t_5.bed \
            --other data/sr_1kg_pop_freq_t_5.bed \
            --out img/stix_lr_vs_sr_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX short-read depth > 5" \
            --ylabel "Num. of samples with STIX long-read depth > 5" \
            --title "1KG germline SVs" \
            --fignum 3C
        """

rule fig_3B:
    input:
        'data/lr_1kg_pop_freq_t_5.bed',
        'data/1kg_pop_freq.lr_samples.bed'
    output:
        'img/stix_lr_vs_1kg_pop_freq.png'
    shell:
        """
        python src/hex_plot.py \
            --stix data/lr_1kg_pop_freq_t_5.bed \
            --other data/1kg_pop_freq.lr_samples.bed \
            --out img/stix_lr_vs_1kg_pop_freq.png \
            --height 4 \
            --width 5 \
            --xlabel "Num. samples called non-ref by 1KG" \
            --ylabel "Num. of samples with STIX long-read depth > 5" \
            --title "1KG germline SVs" \
            --fignum 3B
        """
