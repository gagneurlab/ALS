import pandas as pd
import matplotlib.pyplot as plt
import umap
import umap.plot
import numba

numba.set_num_threads(snakemake.threads)

gene_counts = pd.read_table(snakemake.input['counts'], sep = '\t')
# TODO: add sample annotations

del gene_counts['gene_id']
X = gene_counts.transpose()
embed_counts = umap.UMAP().fit(X)

umap.plot.points(embed_counts)
plt.savefig(snakemake.output['plot'])
