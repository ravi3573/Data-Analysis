# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot
%matplotlib inline
import seaborn as sns
df=pd.read_csv('../input/zomato-restaurants-rating-dataset/zomato.csv',encoding="latin-1")
df.head()
nan_values=df.isna()
nan_columns=nan_values.any()
nan_columns
df1=pd.read_csv("../input/zomato-restaurants-rating-dataset/Country-Code.csv")
print(df1.head())
len(df1.index)
df2=pd.merge(df,df1,on="Country Code",how="left")
df2.head(2)
# so we added df1 in df in a new dataframe df2 in left merging
print("List of countries in data set: ")
for x in pd.unique(df2.Country):
    print(x)
print("Total number of countries in dataset: ",len(pd.unique(df2.Country)))
# making pie chart for country wise distributuion
import plotly.express as px
from plotly.offline import init_notebook_mode, plot, iplot

labels = list(df2.Country.value_counts().index)
values = list(df2.Country.value_counts().values)
# labels gives names and values gives count
fig = {
    "data":[
        {
            "labels" : labels,
            "values" : values,
            "hoverinfo" : 'label+percent',
            "domain": {"x": [0, .9]},
            "hole" : 0.6,
            "type" : "pie",
            "rotation":120,
        },
    ],
    "layout": {
        "title" : "Restaurants Density Presence around the World",
        "annotations": [
            {
                "font": {"size":20},
                "showarrow": True,
                "text": "Countries",
                "x":0.2,
                "y":0.9,
            },
        ]
    }
}

iplot(fig)
df3=df2.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:"Rating Count"})
df3.head()
import seaborn as sns
sns.set_style("darkgrid")
import matplotlib.pyplot as plt
%matplotlib inline
plt.figure(figsize=(12,6))
# plt.xticks(rotation=75)
plt.title('Rating Color')
sns.barplot(x=df3['Rating color'], y=df3['Rating Count']);
no_rating=df2[df2["Rating color"]=="White"].groupby("Country").size().reset_index().rename(columns={0:"Rating count"})
no_rating
no_rating=df2[df2["Rating color"]=="White"].groupby("Country").size().reset_index().rename(columns={0:"Rating count"})
no_rating
res_india.City.value_counts()
delhi=df2[(df2.City=="New Delhi")]
plt.figure(figsize=(12,6))
sns.barplot(x=delhi.Locality.value_counts().head(10),y=delhi.Locality.value_counts().head(10).index)

plt.ylabel(None)
plt.xlabel("Number of restaurants")
plt.title("Restaurants Listing in New Delhi")
cp=delhi[(delhi.Locality.isin(['Connaught Place'])) & (delhi["Rating text"].isin(['Excellent','Very Good']))]
cp.head(2)