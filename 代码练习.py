pro = ts.pro_api("620d5af00fee0cd9bc908b5f2d0bf44ffeaad14b85deece54134a8e5")
df_raw = pro.daily(ts_code="000001.SZ", start_date="20260101", end_date="20260110")
df_raw["trade_date"] = pd.to_datetime(df_raw["trade_date"])
df_raw = df_raw.sort_values("trade_date").reset_index(drop=True)
df_raw["close_prev"] = df_raw.groupby("ts_code")["close"].shift(1)
df_raw["ret"] = (df_raw["close"] - df_raw["close_prev"]) / df_raw["close_prev"]
df = df_raw[["ts_code", "trade_date", "close", "close_prev", "ret"]]
print(df)
