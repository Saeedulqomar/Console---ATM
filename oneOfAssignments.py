import pandas as pd
import numpy as np

data = {
    'Name' : ['Alice', 'Max', 'Bro', 'Charlie'],
    'Age' : [np.nan,43,54,np.nan],
    'City' : [np.nan,'New York', 'LA', 'Moscow'],
}

df = pd.DataFrame(data)

df_filled = df.fillna({'Age' : df['Age'].mean(), 'City': 'Unknown'})
print(df_filled)