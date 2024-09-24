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
            --merged data/stix_sr_te_depth_v_freq.bed \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX short-read depth > 0" \
            --ylabel "Mean SV evidence depth / coverage " \
            --title "TE SVs" \
            --color "Greens"
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
            --merged data/stix_lr_te_depth_v_freq.bed \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX long-read depth > 0" \
            --ylabel "Mean SV evidence depth / coverage " \
            --title "TE SVs" \
            --color "Greens"
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

rule filter_hg002_variants_by_svlen:
    "Filter hg002 variants by svlen >=50"
    input:
        hg002_vcf = 'data/GRCh38_HG002-T2TQ100-V1.0_stvar.vcf.gz',
        hg002_cmrg_vcf = 'data/HG002_GRCh38_difficult_medical_gene_SV_benchmark_v0.01_trusted_SVTYPE.addID.vcf',
        gnomad_lr_bed = 'data/HG002.gnomadAF.bed',
        gnomad_lr_cmrg_bed = 'data/HG002.cmrg.gnomadAF.bed',
        gnomad_sr_bed = 'data/HG002.gnomadAF.DEL.bed',
        gnomad_sr_cmrg_bed = 'data/HG002.cmrg.gnomadAF.DEL.bed',
        stix_lr_bed = 'data/lr_hg002_pop_freq_t_5.bed',
        stix_sr_bed = 'data/sr_hg002_pop_freq_t_5.bed',
        stix_lr_cmrg_bed = 'data/lr_hg002_cmrg_pop_freq_t_5.bed',
        stix_sr_cmrg_bed = 'data/sr_hg002_cmrg_pop_freq_t_5.bed',

    output:
        gnomad_lr_bed = 'data/HG002.gnomadAF.svlengte50.bed',
        gnomad_lr_cmrg_bed = 'data/HG002.cmrg.gnomadAF.svlengte50.bed',
        gnomad_sr_bed = 'data/HG002.gnomadAF.DEL.svlengte50.bed',
        gnomad_sr_cmrg_bed = 'data/HG002.cmrg.gnomadAF.DEL.svlengte50.bed',
        stix_lr_bed = 'data/lr_hg002_pop_freq_t_5.svlengte50.bed',
        stix_sr_bed = 'data/sr_hg002_pop_freq_t_5.svlengte50.bed',
        stix_lr_cmrg_bed = 'data/lr_hg002_cmrg_pop_freq_t_5.svlengte50.bed',
        stix_sr_cmrg_bed = 'data/sr_hg002_cmrg_pop_freq_t_5.svlengte50.bed',

    shell:
        """
        bash src/filter_hg002_by_svlen.sh \
            -b {input.gnomad_lr_bed} \
            -v {input.hg002_vcf} \
            -o {output.gnomad_lr_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.gnomad_lr_cmrg_bed} \
            -v {input.hg002_cmrg_vcf} \
            -o {output.gnomad_lr_cmrg_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.gnomad_sr_bed} \
            -v {input.hg002_vcf} \
            -o {output.gnomad_sr_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.gnomad_sr_cmrg_bed} \
            -v {input.hg002_cmrg_vcf} \
            -o {output.gnomad_sr_cmrg_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.stix_lr_bed} \
            -v {input.hg002_vcf} \
            -o {output.stix_lr_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.stix_sr_bed} \
            -v {input.hg002_vcf} \
            -o {output.stix_sr_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.stix_lr_cmrg_bed} \
            -v {input.hg002_cmrg_vcf} \
            -o {output.stix_lr_cmrg_bed}
        bash src/filter_hg002_by_svlen.sh \
            -b {input.stix_sr_cmrg_bed} \
            -v {input.hg002_cmrg_vcf} \
            -o {output.stix_sr_cmrg_bed}
        """


rule fig_3H:
    input:
        # 'data/sr_hg002_cmrg_pop_freq_t_5.bed',
        # 'data/HG002.cmrg.gnomadAF.DEL.bed'
        stix_sr_cmrg_bed = rules.filter_hg002_variants_by_svlen.output.stix_sr_cmrg_bed,
        gnomad_sr_cmrg_bed = rules.filter_hg002_variants_by_svlen.output.gnomad_sr_cmrg_bed
    output:
        plot = 'img/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.png',
        merged_bed = 'data/stix_sr_hg002_cmrg_vs_gnomad_pop_freq.bed'
    shell:
        """
        python src/hex_plot.py \
            --stix {input.stix_sr_cmrg_bed} \
            --other {input.gnomad_sr_cmrg_bed} \
            --out {output.plot} \
            --merged {output.merged_bed} \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX short-read depth => 5" \
            --title "HG002 CMRG DELs"  \
            --color-scale 0,5 \
            --color "Blues"
        """

rule fig_3G:
    input:
        # 'data/lr_hg002_cmrg_pop_freq_t_5.bed',
        # 'data/HG002.cmrg.gnomadAF.bed'
        stix_lr_cmrg_bed = rules.filter_hg002_variants_by_svlen.output.stix_lr_cmrg_bed,
        gnomad_lr_cmrg_bed = rules.filter_hg002_variants_by_svlen.output.gnomad_lr_cmrg_bed
    output:
        plot = 'img/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.png',
        merged_bed = 'data/stix_lr_hg002_cmrg_vs_gnomad_pop_freq.bed'
    shell:
        """
        python src/hex_plot.py \
            --stix {input.stix_lr_cmrg_bed} \
            --other {input.gnomad_lr_cmrg_bed} \
            --out {output.plot} \
            --merged {output.merged_bed} \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX long-read depth => 5" \
            --title "HG002 CMRG SVs" \
            --color-scale 0,5 \
            --color "Blues"
        """


rule fig_3F:
    input:
        # sr_stix_bed = 'data/sr_hg002_pop_freq_t_5.bed',
        # gnomad_bed = 'data/HG002.gnomadAF.DEL.bed'
        stix_sr_bed = rules.filter_hg002_variants_by_svlen.output.stix_sr_bed,
        gnomad_sr_bed = rules.filter_hg002_variants_by_svlen.output.gnomad_sr_bed
    output:
        plot = 'img/stix_sr_hg002_vs_gnomad_pop_freq.png',
        merged_bed = 'data/stix_sr_hg002_vs_gnomad_pop_freq.bed'
    shell:
        """
        python src/hex_plot.py \
            --stix {input.stix_sr_bed} \
            --other {input.gnomad_sr_bed} \
            --out {output.plot} \
            --merged {output.merged_bed} \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX short-read depth => 5" \
            --title "HG002 DELs" \
            --color "Blues"
        """


rule fig_3D:
    input:
        # 'data/lr_hg002_pop_freq_t_5.bed',
        # 'data/HG002.gnomadAF.bed',
        stix_lr_bed = rules.filter_hg002_variants_by_svlen.output.stix_lr_bed,
        gnomad_lr_bed = rules.filter_hg002_variants_by_svlen.output.gnomad_lr_bed,
    output:
        plot = 'img/stix_lr_hg002_vs_gnomad_pop_freq.png',
        merged_bed = 'data/stix_lr_hg002_vs_gnomad_pop_freq.bed'
    shell:
        """
        python src/hex_plot.py \
            --stix {input.stix_lr_bed} \
            --other {input.gnomad_lr_bed} \
            --out {output.plot} \
            --merged {output.merged_bed} \
            --height 4 \
            --width 5 \
            --xlabel "Allele freq. in gnomAD" \
            --ylabel "Num. of samples with STIX long-read depth => 5" \
            --title "HG002 SVs" \
            --color "Blues"
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
            --merged data/stix_lr_vs_sr_pop_freq.bed \
            --height 4 \
            --width 5 \
            --xlabel "Num. of samples with STIX short-read depth => 5" \
            --ylabel "Num. of samples with STIX long-read depth => 5" \
            --title "1KG germline SVs"
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
            --merged data/stix_lr_vs_1kg_pop_freq.bed \
            --height 4 \
            --width 5 \
            --xlabel "Num. samples called non-ref by 1KG" \
            --ylabel "Num. of samples with STIX long-read depth => 5" \
            --title "1KG germline SVs"
        """
