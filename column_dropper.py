import pandas as pd
from pandas import ExcelWriter
import os

def dropper(file):
    output = os.path.basename(file).split(".")[1] + "_dropped.xlsx"
    df = pd.read_excel(file, usecols=["Symbol", "padj", "log2FoldChange", "pvalue", "stat", "foldChange", "log10padj"])
    with ExcelWriter(output) as writer:
        df.to_excel(writer, sheet_name="result", header=True, index=False)

if __name__ == "__main__":
    files = [i for i in os.listdir(os.getcwd()) if i.endswith("_new.xlsx")]
    for file in files:
        dropper(file)
