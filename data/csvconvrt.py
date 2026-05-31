import pandas as pd

data1 = pd.read_csv("daily_sales_data_0.csv")
data1 = data1[data1["product"] == "pink morsel"]
data1['price'] = data1['price'].str.replace('$', '', regex=False).astype(float)
data1["sales"] = data1["price"] * data1["quantity"]
data1["date"] = data1["date"]
data1["region"] = data1["region"]

data2 = pd.read_csv("daily_sales_data_1.csv")
data2 = data2[data2["product"] == "pink morsel"]
data2['price'] = data2['price'].str.replace('$', '', regex=False).astype(float)
data2["sales"] = data2["price"] * data2["quantity"]
data2["date"] = data2["date"]
data2["region"] = data2["region"]

data3 = pd.read_csv("daily_sales_data_2.csv")
data3 = data3[data3["product"] == "pink morsel"]
data3['price'] = data3['price'].str.replace('$', '', regex=False).astype(float)
data3["sales"] = data3["price"] * data3["quantity"]
data3["date"] = data3["date"]
data3["region"] = data3["region"]

final_data = pd.concat([data1, data2, data3], ignore_index= True)

final_data = final_data[["sales", "date", "region"]]

final_data.to_csv("single_formatted_output.csv", index = False)