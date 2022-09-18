import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
runs={"Sachin":100,"Pappu":420,"Saubhagya":1}
wickets={"Sachin":1,"Pappu":420}
data=[runs,wickets]
index=["Runs","Wickets"]
df=pd.DataFrame(data,index)
print(df)
# df.to_csv("h:\\csv\\scores.csv")
# df.to_excel("h:\\csv\\scores.xlsx")
# x=pd.read_csv("h:\\csv\\scores.csv")
# print(x)
# x=pd.read_csv("h:\\csv\\scores.csv",index_col=0)
# print(x)
# x=pd.read_csv("h:\\csv\\scores.csv")
# print(x)
# x=pd.read_csv("h:\\csv\\scores.csv",index_col=0)
# print(x)
# x=pd.read_excel("h:\\csv\\scores.xlsx")
# print(x)
# x=pd.read_excel("h:\\csv\\scores.xlsx",index_col=0)
# print(x)