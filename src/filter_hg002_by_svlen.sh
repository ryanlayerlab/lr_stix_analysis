#!/bin/env bash


while getopts "b:v:o:" opt; do
  case $opt in
    b) bed=$OPTARG ;;
    v) vcf=$OPTARG ;;
    o) out=$OPTARG ;;
    *) echo "Invalid option: -${OPTARG}" ;;
  esac
done

# check if bed file uses chr prefix in chromosome names
# if not, add it.
function check_chr_prefix {
    head -n 1 $1 | awk '{print $1}' | grep -o "chr" | wc -l
}

chr_prefix=$(check_chr_prefix $bed)
if [ $chr_prefix -eq 0 ]; then
    awk '{print "chr"$0}' $bed > "${bed}.tmp"
    bed="${bed}.tmp"
fi

set -euo pipefail

bcftools view -i 'SVLEN>=50' $vcf |
    bcftools query -f '%CHROM\t%POS\t%SVLEN\t%SVTYPE\n' |
    awk -v OFS='\t' '
        function abs(x){
            return ((x < 0) ? -x : x)
        }
        {
            if ($4 == "DEL") print $1, $2, $2+abs($3), $4
            else if ($4 == "INS") print $1, $2, $2, $4
        }
    ' |
    bedtools intersect -a stdin -b $bed -wb -f 1.0 > $out

if [[ $chr_prefix -eq 0 ]]; then
    rm $bed
fi
