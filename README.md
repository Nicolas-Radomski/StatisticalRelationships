# Usage
The repository StatisticalRelationships provides Python (recommended version 3.12) scripts called Correlations.py and Associations.py to compute correlations (Pearson, Spearman or Kendall methods) or associations (Cramer’s V or Theil’s U methods) across numerical or categorical variables, respectively.
# Recommanded library versions
- pandas==2.2.2
- numpy==1.26.4
- dython==0.7.6
- PyQt5==5.15.11
- matplotlib==3.9.1
# Recommended Python environment
## Download Miniconda for Ubuntu 20.04
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda-installer.sh
```
## Install Miniconda
```
bash /opt/miniconda-installer.sh
```
## Update Conda
```
conda update --all
```
## Create an environment
```
conda create --name py312 python=3.12
```
## Activate the environment
```
conda activate py312
```
## Check the Python version
```
python --version
```
## Install a Python library
```
conda install pandas
conda install numpy
conda install conda-forge::dython
conda install anaconda::pyqt
conda install matplotlib
```
## Check the list of Python libraries
```
conda list
```
## Desactivate the environment after use
```
conda deactivate
```
# Examples of commands
## Correlations from numerical variables
```
python Correlations.py -i input/data_numerical.tsv -p output/test -m pearson -l 15 -nc
python Correlations.py -i input/data_numerical.tsv -p output/test -m spearman -l 15 -nc
python Correlations.py -i input/data_numerical.tsv -p output/test -m kendall -l 15 -nc
```
## Associations from categorical variables
```
python Associations.py -i input/data_categorical.tsv -p output/test -m cramer -l 20 -nc
python Associations.py -i input/data_categorical.tsv -p output/test -m theil -l 20 -nc
```
# Expected input
## Correlations from numerical variables
```
GC	contigs	N50	length	binar
35.4	10	44556	122421	0
35.7	132	21190	142512	1
34.6	124	24425	152390	0
37.5	354	2834	13678	1
35.4	11	42421	44556	0
36.6	145	22512	181190	1
32.6	123	22390	174425	0
38.5	423	2678	19834	1
34.9	16	52323	165489	0
38.5	123	22345	142445	1
37.4	125	24589	153225	0
34.2	324	2123	16004	1
37.4	18	45489	192323	0
38.2	144	22445	102345	1
38.4	111	23225	114589	0
38.5	345	2004	14123	1
```
## Associations from categorical variables
```
phenotype_A	phenotype_B	gene_A		gene_B		gene_C
fast		green		presence	absence		presence
slow		red		absence		presence	absence
fast		blue		presence	presence	presence
slow		red		absence		absence		absence
fast		blue		presence	presence	presence
slow		red		absence		presence	absence
fast		green		presence	absence		presence
slow		red		absence		presence	absence
fast		blue		presence	absence		presence
slow		red		absence		presence	absence
fast		blue		presence	absence		presence
slow		red		absence		presence	absence
fast		green		presence	absence		presence
slow		red		absence		presence	absence
fast		green		presence	absence		absence
slow		red		absence		presence	presence
```
# Expected output
## Correlations from numerical variables
```
	 GC	contigs N50	length	binar
GC	  1.0	 0.32	-0.28	-0.25	 0.41
contigs   0.32	 1.0	-0.94	-0.74	 0.71
N50	 -0.28	-0.94	 1.0	 0.64	-0.73
length	 -0.25	-0.74	 0.64	 1.0	-0.48
binar	  0.41	 0.71	-0.73	-0.48	 1.0
```
## Associations from categorical variables
```
		phenotype_A	phenotype_B	gene_A	gene_B	gene_C
phenotype_A	1		0.96		0.87	0.45	0.59
phenotype_B	0.96		1		0.96	0.65	0.7
gene_A		0.87		0.96		1	0.45	0.59
gene_B		0.45		0.65		0.45	1	0
gene_C		0.59		0.7		0.59	0	1
```
# Illustration
![workflow figure](https://github.com/Nicolas-Radomski/StatisticalRelationships/blob/main/illustration.png)
# Reference
Rahul Raoniar (2022) https://medium.com/the-researchers-guide/generate-numerical-correlation-and-nominal-association-plots-using-python-c8548aa4a663
# Please site
https://github.com/Nicolas-Radomski/StatisticalRelationships
# Acknowledgment
The GENPAT-IZSAM Staff for our discussions about the Python syntax.
# Author
Nicolas Radomski
