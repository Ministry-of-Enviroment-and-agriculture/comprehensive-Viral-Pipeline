# VirusConsensusPipe
## A robust pipeline to build consensus genome for virus. A case study on camelpox virus genomes

VirusConsensusPipe is a open-source nextflow based pipeline that provides assembly to variant identification to consensus of different viruses. VirusConsensusPipe consists of several steps: 

(1) Read quality control 

(2) Trimming

(3) Reference mapping

(4) de novo genome assembly

(5) Reference-based assembly

(6) Annotation

(7) Variant identification

(8) Consensus

(9) Report Generation

All the steps were consolidated into one command line offering efficient and fast results. To facilitate usage, the pipeline was compiled into docker containers to avoid problems with incompatibility and installation of the tools. VirusConsensusPipe was validated using 17 camelpox datasets that were sequenced in our lab


## This work is funded by Ministry of Environment, Water and Agriculture of Saudi Arabia
