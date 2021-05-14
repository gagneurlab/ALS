from splicing_outlier_prediction import SpliceOutlier, SpliceOutlierDataloader
from pathlib import Path

dl = SpliceOutlierDataloader(
    snakemake.input['fasta'], snakemake.input['vcf'],
    ref_tables5=list(snakemake.input['ref_tables5']),
    ref_tables3=list(snakemake.input['ref_tables3']),
    regex_pattern='splice_maps\/(.*)_junction_annotation',
    combined_ref_tables5=Path(snakemake.input['combined_ref_tables5']), 
    combined_ref_tables3=Path(snakemake.input['combined_ref_tables3']),
    save_combined_ref_tables=False,
    samples=True)

model = SpliceOutlier()
model.predict_save(dl, snakemake.output['result'])
