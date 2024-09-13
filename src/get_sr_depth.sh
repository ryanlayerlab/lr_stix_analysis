aws s3 \
    cp s3://1000genomes/1000G_2504_high_coverage/1000G_2504_high_coverage.sequence.index - \
| grep -v "^#" \
| awk -v FS="\t" '{OFS="\t"; if ($21>0) print $10,$21/3088302970; else print $10,30;}' \
> data/sr_sample_depth.txt
