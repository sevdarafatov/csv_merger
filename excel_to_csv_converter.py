import pandas as pd
import sys

file = sys.argv[1]
out =  sys.argv[2]
df = pd.read_excel(file, sheet_name=0)
df.to_csv(out, index=False)
