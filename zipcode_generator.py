import pandas as pd
data1 = pd.read_csv("MoreColumns.csv")
from uszipcode import Zipcode, SearchEngine
search = SearchEngine(simple_zipcode=False)
for i in range(0, len(data1)):
    val = (search.by_coordinates(float(data1.iloc[i]['latitude']), float(data1.iloc[i]['longitude']), radius=30, returns=1))[0].to_dict().get('zipcode')
    data1.set_value(i,'ZipCode',val)
    if i%1000 == 0:
        print(i)
		
data1.iloc[0:len(data)]['ZipCode'].to_csv('output1.csv');