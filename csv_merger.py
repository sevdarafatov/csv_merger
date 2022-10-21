import numpy as np
import pandas as pd
import re
import warnings
import argparse
warnings.simplefilter(action='ignore')
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--samplename", required = True, help = "sample name")
ap.add_argument("-f", "--idsfile", required = True, help = "filtered file")
args = vars(ap.parse_args())
df_ann = pd.read_csv(args["idsfile"], delimiter="\t")
name= args["samplename"]
df= df_ann.merge(df_ss, on="sseqid", how= 'inner')
df.to_csv(name, '\t', index=False)
