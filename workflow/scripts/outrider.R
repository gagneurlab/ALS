suppressPackageStartupMessages({
    library(data.table)
    library(OUTRIDER)
    library(BiocParallel)
})

padj_cutoff <- snakemake@params$padj_cutoff
register(MulticoreParam(snakemake@threads))

ods <- readRDS(snakemake@input$ods)

# run end-to-end pipeline
ods <- OUTRIDER(ods)
saveRDS(ods, snakemake@output$ods)

# extract and save results
res <- results(ods, padjCutoff = padj_cutoff)
fwrite(res, snakemake@output$results)

