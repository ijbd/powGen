# ijbd:
# 
# Perform some basic checks on powGen output files. 

import numpy as np
import sys
from netCDF4 import Dataset

cf_root = "/scratch/mtcraig_root/mtcraig1/shared_data/merraData/cfs/"

region = sys.argv[1]
year = sys.argv[2]
gen_type = sys.argv[3]


if len(sys.argv) == 5:
    if sys.argv[4] == "old":
        filename = cf_root + region + '/' + year + '_' + gen_type + '_ac_generation.nc'
    if sys.argv[4] == "test":
        filename = year + "_" + gen_type + "_generation_cf.nc"
else:
    filename = cf_root + region + "/" + year + "_" + gen_type + "_generation_cf.nc"

data = Dataset(filename)

if len(sys.argv) == 5:
    if sys.argv[4] == "old":
        cf = np.array(data.variables['ac'])
    if sys.argv[4] == "test":
        cf = np.array(data.variables['cf'])
else:
    cf = np.array(data.variables['cf'])

# print some stats

print("Maximum:", np.max(cf))
print("Minimum:", np.min(cf))
print("Average:", np.average(cf))
print("Valid Entries:", np.sum(np.logical_and(cf>=0,cf<=1)), "of", cf.size)