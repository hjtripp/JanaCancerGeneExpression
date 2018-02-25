import os
import sys
# -*- coding: utf-8 -*-
"""
This program merges three gene expression files from Wang et al. 2017
"""

os.chdir('/Users/hjtripp/Desktop/Jana_GTExData/production/scripts')

master_genelist=sys.argv[1]

# The load_dict function returns a dictionary loaded from a file
#   WARNING: skips one field of tab-delimited data


def load_dict(filename, sample):
    first = True
    file = open(filename, 'rU')
    dict = {}
    for line in file:
        chomped_line = line.rstrip()
        fields = chomped_line.split('\t')
        gene_key = fields[0]
        gene_data = ""
        for field in fields[2:]:
            if (first):
                field = sample
            gene_data = gene_data + field + '\t'
        stripped_gene_data = gene_data.rstrip()
        dict[gene_key] = stripped_gene_data
        first = False
    return dict


# Load dictionaries of expression data
cervix_dict = load_dict(sys.argv[2], 'cervix')
salivary_dict = load_dict(sys.argv[3], 'salivary')
uterus_dict = load_dict(sys.argv[4], 'uterus')

# Load master file of all genes into master_gene list. The master file
# came from cut -f 1 commands to extract all the genes in all 3 expression
# into a single file, then a sort -uniq of that to make the master file
f = open(master_genelist, 'rU')
master_genes = []
for line in f:
    # print line,
    master_genes.append(line.rstrip())
f.close()

# Look up expression dictionary entries for each master file gene
# and write it out. Skip genes that are not found.
fout = open('../data/output/master_uniq_out.txt', 'w')
for gene in master_genes:
    if gene in cervix_dict and gene in salivary_dict and gene in uterus_dict:
        lineout = (gene + '\t' + cervix_dict[gene] + '\t' +
                   salivary_dict[gene] + '\t' + uterus_dict[gene] + '\n')
    else:
        continue
    fout.write(lineout)
fout.close()
