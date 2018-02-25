#!/bin/bash

##
#
# Make a master list of all genes in
# a set of expression files.
#
# Jim Tripp Feb 23, 2018
##


WORKFILE1='../data/workfiles/temp_genelist.txt'
WORKFILE2='../data/workfiles/temp_genelist_sortu.txt'
WORKFILE3='../data/workfiles/temp_genelist_sortu_edited.txt'

if [ -f $WORKFILE1 ]; then rm $WORKFILE1 ; fi
if [ -f $WORKFILE2 ]; then rm $WORKFILE2 ; fi
if [ -f $WORKFILE3 ]; then rm $WORKFILE3 ; fi

DATAFILE1='../data/input/cervix-rsem-fpkm-gtex.txt'
DATAFILE2='../data/input/salivary-rsem-fpkm-gtex.txt'
DATAFILE3='../data/input/uterus-rsem-fpkm-gtex.txt'


# extract and append gene names from expression file
# and put into mast list of genes with duplicates

for filename in ../data/input/*.txt ; do
    cut -f 1 $filename >> $WORKFILE1
done


# eliminate duplicate gene names in master list

sort -u $WORKFILE1 > $WORKFILE2


# delete the "Hugo_Symbol" entry in $WORKFILE2 and
# add it to the top of $WORKFILE3

echo Hugo_Symbol > $WORKFILE3
sed '/Hugo_Symbol/d' $WORKFILE2 >> $WORKFILE3


# Call python script to merge all expression data
# associated with master list of genes

python MergeGeneExpressionFiles.py $WORKFILE3 $DATAFILE1 $DATAFILE2 $DATAFILE3
