# pip3.12 install --force-reinstall pandas==2.2.2
# pip3.12 install --force-reinstall numpy==1.26.4
# pip3.12 install --force-reinstall matplotlib==3.9.1

# import packages
import sys as sys # no individual installation because is part of the Python Standard Library
import os as os # no individual installation because is part of the Python Standard Library
import datetime as dt # no individual installation because is part of the Python Standard Library
import argparse as ap # no individual installation because is part of the Python Standard Library
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# step control
step1_start = dt.datetime.now()

# set workflow reference
reference = 'Please, site this repository: https://github.com/Nicolas-Radomski/StatisticalRelationships'

# get parser arguments
parser = ap.ArgumentParser(
	prog='Correlations.py', 
	description='Estimating correlations between numerical variables.',
	epilog=reference
	)
# define parser arguments
parser.add_argument(
	'-i', '--input', 
	dest='table', 
	action='store', 
	required=True, 
	help='path of tab-separated values (tsv) file (REQUIRED)'
	)
parser.add_argument(
	'-p', '--prefix', 
	dest='prefix', 
	action='store', 
	required=True, 
	help='path and/or prefix of output files (REQUIRED)'
	)
parser.add_argument(
	'-m', '--method', 
	dest='method', 
	action='store', 
	required=False, 
	default="pearson", 
	help="Pearson ('pearson'), Spearman ('spearman') or Kendall ('kendall') correlation methods (DEFAULT: pearson)"
	)
parser.add_argument(
	'-l', '--labels', 
	dest='labels', 
	type=int,
	action='store', 
	required=False, 
	default=12, 
	help='size of figure labels (DEFAULT: 12)'
	)
parser.add_argument(
	'-d', '--debug', 
	dest='debug', 
	type=int,
	action='store', 
	required=False, 
	default=0, 
	help='limit of the traceback (DEFAULT: 0)'
	)
parser.add_argument(
	'-nc', '--no-check', 
	dest='nocheck', 
	action='store_true', 
	required=False, 
	default=False, 
	help='do not check versions of Python and packages (DEFAULT: False)'
	)

# print help if there are no arguments in the command
if len(sys.argv)==1:
	parser.print_help()
	sys.exit(1)

# reshape arguments
## extract parser arguments
args = parser.parse_args()
## rename arguments
TABLE=args.table
PREFIX=args.prefix
METHOD=args.method
LABELS=args.labels
DEBUG=args.debug
NOCHECK=args.nocheck

# set tracebacklimit
sys.tracebacklimit = DEBUG

# control versions
if NOCHECK == False :
    ## control Python version
	if sys.version_info[0] != 3 or sys.version_info[1] != 12 :
		raise Exception("Python 3.12 version is recommended")
		exit()
	# control versions of packages
	if ap.__version__ != "1.1":
		raise Exception('argparse 1.1 (1.4.1) version is recommended')
		exit()
	if pd.__version__ != "2.2.2":
		raise Exception('pandas 2.2.2 version is recommended')
		exit()
	if np.__version__ != "1.26.4":
		raise Exception('numpy 1.26.4 version is recommended')
		exit()
	if mpl.__version__ != "3.9.1":
		raise Exception('matplotlib 3.9.1 version is recommended')
		exit()
	message_versions = 'The recommended versions of Python and packages were properly controlled'
else:
	message_versions = 'The recommended versions of Python and packages were not controlled'

# print a message about version control
print(message_versions)

# control methods
if METHOD == 'pearson':
	print("The Pearson method has been properly recognized")
elif METHOD == 'spearman':
	print("The Spearman method has been properly recognized")
elif METHOD == 'kendall':
	print("The Kendall method has been properly recognized")
else:
	raise Exception("The Pearson ('pearson'), Spearman ('spearman') or Kendall ('kendall') methods were not properly recognized")
	exit()

# read input tsv
input_df = pd.read_csv(TABLE, sep='\t')

# check if variables are object
unexpected_type = 'object'
dtypes = input_df.dtypes.to_dict()
for col_name, detected_type in dtypes.items():
	if (detected_type == unexpected_type):
		raise ValueError(f"The variable '{col_name}' is an '{detected_type}' while it should be a 'float64' and/or an 'int64'")
print(f"The absence of '{unexpected_type}' variables was properly controlled")

# estimating correlations between numerical variables
## compute pairwise correlations
correlations_df = input_df.corr(method = METHOD).round(2)
## output pairwise correlations
### output path
output_table = PREFIX + '-pairwise-correlations-' + METHOD + '.tsv'
### write output
correlations_df.to_csv(output_table, sep='\t', index=True, header=True)

# plot pairwise correlations
## initiating a fig and axis object
fig, ax = plt.subplots(figsize = (12, 10))
## create a plot
cax = ax.imshow(correlations_df.values, interpolation='nearest', cmap = 'Blues', vmin = -1, vmax = 1)
## set axis tick labels 
ax.set_xticks(ticks = range(len(input_df.columns)),
              labels = input_df.columns)
ax.set_yticks(ticks = range(len(input_df.columns)),
              labels = input_df.columns)
## resize the tick parameters
ax.tick_params(axis = "x", labelsize = LABELS, labelrotation = 90)
ax.tick_params(axis = "y", labelsize = LABELS, labelrotation = 0)
## add a color bar
fig.colorbar(cax).ax.tick_params(labelsize = LABELS)
## add annotation
for (x, y), t in np.ndenumerate(correlations_df):
	ax.annotate("{:.2f}".format(t),
					xy = (x, y),
					va = "center", 
					ha = "center", 
					size = LABELS)
## output path
output_figure = PREFIX + '-pairwise-correlations-' + METHOD + '.pdf'
## save figure
plt.savefig(output_figure, format="pdf", bbox_inches="tight", dpi=600)

# step control
step1_end = dt.datetime.now()
step1_diff = step1_end - step1_start
print('The script lasted '+ str(step1_diff.microseconds) + ' μs')

# print output results
print(reference)
print('Results are here:')
cmd = 'ls -al ' + PREFIX + '-pairwise-correlations-' + METHOD + '*'
os.system(cmd)