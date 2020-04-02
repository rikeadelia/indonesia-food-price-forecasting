import pandas as pd

df = pd.read_csv("/home/rike/Documents/bangkit/assignment_5/wfpvam_foodprices.csv", index_col=False)
df_indonesia = df.loc[df["adm0_name"] == "Indonesia"]
df_indonesia["month_year"] = df_indonesia["mp_month"].astype(str) + "-" + df_indonesia["mp_year"].astype(str)
# df_indonesia["month_year"] = df_indonesia[["mp_month", "mp_year"]].agg("-".join, axis=1)
df_indonesia = df_indonesia.set_index("month_year").drop("mp_commoditysource", axis=1)
df_indonesia.to_csv("foodprices_indonesia.csv")