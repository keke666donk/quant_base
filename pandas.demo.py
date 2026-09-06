import pandas as pd
import numpy as np
s=pd.Series([10,20,30],index=["A","B","C"])
print(s)
print(s["B"])
a=pd.DataFrame({
    "close":[12.5,12.8,13.1],
    "volume":[10000,12000,9500]},
    index=["2026-09-01","2026-09-02","2026-09-03"]
               )
print(a)
print(a.loc["2026-09-02"])
print(a.iloc[1])
cond=a["close"]>12.8
print(a[cond])
a_new=a.sort_values("close",ascending=False)
print(a_new.iloc[1])
print(a_new.loc["2026-09-03"])
conds=(a_new["close"]>12.8)&(a_new["volume"]>10000)
print(a_new[conds])