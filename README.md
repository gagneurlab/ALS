End ALS Kaggle Challenge
==============================

**When the outlier is the signal**

[TODO: introduction & motivation]

Installation
------------

Please install the following conda environment from the repository root.

```commandline
conda env create -f environment.yml
```

This will create a conda environment called `als`.

**Note:** You can alternatively use [mamba](https://mamba.readthedocs.io/en/latest/index.html) for faster install times.

After a fresh install of the environment, you need to install the correct Ensembl release.
This only needs to be done once.

```commandline
conda activate als
pyensembl install --release 84 --species human
```

Prepare the input data
----------------------

Before executing the pipeline, you need to prepare the input data.
If you prepare the data as described here, you won't need to change any paths in the `configs/config.yml`.

1. Create a link in `data/` called `raw` that links to your location of `end-als` from the [End ALS Kaggle Challenge](https://www.kaggle.com/alsgroup/end-als).

2. Create a directory or link to an empty directory elsewhere in `data/` called `processed`.
We recommend that use a symlink, as the output can get quite large

3. In `data/external/hg38/` download or copy a annotation GTF from Ensembl and FASTA reference file for the assembly hg38.
Here, we call the GTF `Homo_sapiens.GRCh38.84.gtf` and the FASTA `GRCh38.primary_assembly.genome.fa`, which you could also modify in the `configs/config.yml`.


Run the pipeline
----------------

The workflow is implemented as a [Snakemake](https://snakemake.github.io) pipeline.
Snakemake is installed from the conda command above.
Before running the pipeline, please adapt the `configs/config.yaml` file so that it links to the correct input.

After adjusting the paths according to your input locations, you can call the pipeline from the repository root via

```commandline
snakemake -n
```

This should give you an overview of the jobs that Snakemake would want to run.
This is a good point to check of the input and output paths are set correctly.
If this step completes without errors, you can continue to execute the steps shown.
We recommend you to start by visualizing the actual workflow as a directed acyclic graph first, for a better understanding of what is run.
The following command creates a dependency file of the rules (`reports/figures/dependency/rulegraph.png`) as well as all runs (`reports/figures/dependency/dag.png`):

```commandline
snakemake dependency -j 1
```

where `-j 1` allows the pipeline to use at most 1 core.

![rulegraph](reports/figures/dependency/rulegraph.png "Rule graph of the Snakemake workflow")


To run the complete pipeline with e.g. 10 cores, call

```commandline
snakemake -j 10
```

All independent steps will run in parallel if you specify more than 1 core.


Folder Structure
----------------

    ├── LICENSE
    |
    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── configs            <- Config files for Snakemake pipeline
    |
    ├── data
    │   ├── external       <- Data from third party sources. You need to include reference
    |   |                     files in external/hg38/ directory
    |   |
    │   ├── interim        <- Intermediate data that has been transformed.
    |   |
    │   ├── processed      <- The final, canonical data sets for modeling.
    |   |                     This directory will be created autmatically once you run the pipeline.
    |   |                     We recommend that you create a link to an existing directory, as the 
    |   |                     output can be pretty large. 
    |   |
    │   └── raw            <- The original, immutable data dump. You need to create a link
    |                         to the end-als data here
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── workflow           <- Snakemake workflow
    |   ├── notebooks      <- Notebooks to be rendered during pipeline execution
    |   ├── scripts        <- Scripts to be run during pipeline execution
    |   └── Snakefile      <- Snakefile with all the Snakemake rules
    |
    ├── environment.yml   <- Conda environment for reproducing the pipeline
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
