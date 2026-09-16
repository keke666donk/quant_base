import pandas as pd
import numpy as np
import tushare as ts
# s=pd.Series([10,20,30],index=["A","B","C"])
# print(s)
# print(s["B"])
# a=pd.DataFrame({
#     "close":[12.5,12.8,13.1],
#     "volume":[10000,12000,9500]},
#     index=["2026-09-01","2026-09-02","2026-09-03"]
#                )
# print(a)
# print(a.loc["2026-09-02"])
# print(a.iloc[1])
# cond=a["close"]>12.8
# print(a[cond])
# a_new=a.sort_values("close",ascending=False)
# print(a_new.iloc[1])
# print(a_new.loc["2026-09-03"])
# conds=(a_new["close"]>12.8)&(a_new["volume"]>10000)
# print(a_new[conds])
# a=pd.DataFrame({"code":["001","002","001","002","002"],
#     "date":[1,2,1,2,2],
#     "close":[10.1,10.5,20.2,20.8,21.0]
# })
# r=a.groupby("code", as_index=False)["close"].mean()
# print(r)
# a=pd.DataFrame({"code":["001","002","001","002","002"],
#     "date":[1,2,1,2,2],
#     "close":[10.1,10.5,20.2,20.8,21.0]
# })
# b=pd.DataFrame({"code":["001","002","001","002","002"],
#                 "date":[1,2,1,2,2],
#                 "pe":[5,8,10,8,3]
# })
# c=pd.merge(a,b,on=["date","code"],how="left")
# print(c)
# df1=pd.DataFrame({"code":["001"],"close":[12.5]})
# df2=pd.DataFrame({"code":["002"],"close":[12.1]})
# df_all=pd.concat([df1,df2],axis=0,ignore_index=True)
# print(df_all)
# df=pd.DataFrame({"code":["001","001","001"],
#                  "date":[1,2,3],
#                  "close":[10,10.5,11]})
# df["close_lag1"]=df["close"].shift(1)
# print(df)
pro = ts.pro_api("620d5af00fee0cd9bc908b5f2d0bf44ffeaad14b85deece54134a8e5")
df_raw = pro.daily(ts_code="000001.SZ", start_date="20260101", end_date="20260110")
df_raw["trade_date"] = pd.to_datetime(df_raw["trade_date"])
df_raw = df_raw.sort_values("trade_date").reset_index(drop=True)
df_raw["close_prev"] = df_raw.groupby("ts_code")["close"].shift(1)
df_raw["ret"] = (df_raw["close"] - df_raw["close_prev"]) / df_raw["close_prev"]
df = df_raw[["ts_code", "trade_date", "close", "close_prev", "ret"]]
print(df)
