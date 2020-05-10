# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df = pd.read_csv(path)

# convert state column in lower case
df['state'] = df['state'].apply(lambda x: x.lower())

# Calculate the total
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]

# sum of amount
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()

# append the row
df_final = df.append(sum_row, ignore_index=True)

# Code ends here


# --------------
import requests

# Code starts here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=requests.get(url)
df1=pd.read_html(response.content)[0]
df1.columns=df1.iloc[11]
df1=df1.iloc[12:,:]
df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
print(df1.head())
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
print(df1.columns)
mapping=df1.set_index('United States of America')['US'].to_dict()
df_final['abbr']=map(df_final['state'],mapping)
# Code ends here


# --------------
# Code starts here

# replace missing values 

df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')

df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')


# replace the final_df
df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)
df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)



# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))

# Code ends here


# --------------
sum_row=df_sub[["Jan","Feb","Mar","total"]].sum()
df_sub_sum=pd.DataFrame(sum_row).T
df_sub_sum=df_sub_sum.applymap(lambda x: "${:,.0f}".format(x))
final_table=formatted_df.append(df_sub_sum)
print(final_table)
final_table = final_table.rename(index={0:"Total"})



# --------------
# Code starts here
df_sub['total']=df_sub['Jan'].sum()+df_sub['Feb'].sum()+df_sub['Mar'].sum()
print(df_sub.head())
df_sub['total'].plot(kind='pie')
plt.show()
# Code ends here


