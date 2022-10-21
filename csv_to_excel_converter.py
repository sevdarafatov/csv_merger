import pandas as pd
df=pd.read_csv("ent.csv")
df.to_excel("ent.xlsx", sheet_name="Testing", index=False)
