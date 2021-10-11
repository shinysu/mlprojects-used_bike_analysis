import pandas as pd
import datetime
import matplotlib.pyplot as plt
'''
loading data into pandas dataframe
'''
bike_details = pd.read_csv('used_bikes_cleaned2.csv')
#print(bike_details)

'''
Preview data using head/tail comands on pandas
'''
print(bike_details.head(5))
print(bike_details.tail(5))

'''
sort the dataframes
'''
bike_details.sort_values(by='Kilometers')

'''
Extract two columns Model of the vehicle and price 
'''
print(bike_details[['Model', 'Price']])

'''
filter based on model
'''
print(bike_details[bike_details['Model'] == 2018])

'''
Extract brand, age, price where price < average price (for all models)
'''

current_year = datetime.datetime.now().year
bike_details['Age'] =  current_year - bike_details['Model']
print(bike_details[bike_details['Price'] < bike_details['Price'].mean()][['Brand', 'Age','Price']])


'''
brand, age, price for the top 10% (in price) of the model (sort reverse by price and pick the top 10%)'''

print(bike_details.sort_values('Price',ascending=False).head(int(bike_details.shape[0]*.1))[['Brand', 'Age', 'Price']])

'''
Plot the average cost of bikes by model'''

average_cost = bike_details[['Model', 'Price']].groupby('Model', as_index=False).mean()
average_cost.plot.line(x='Model', y='Price', title='Average cost of bikes by model')


'''
average cost of bikes by model for specific brands
'''


filtered_bikes = bike_details[(bike_details['Brand'].isin(['Royal Enfield Bullet Classic', 'Royal Enfield Thunderbird 350', 'Bajaj Pulsar 160 NS']) )
& (bike_details['Model'] >= 2010)][['Brand', 'Model', 'Price']].groupby(['Brand','Model'], as_index=False).mean()
fig, ax = plt.subplots(figsize=(10,5))

for brand, value in filtered_bikes.groupby('Brand'):
    value.plot(x='Model', y='Price', ax=ax, label=brand, title='average cost of bikes by model for specific brands')
plt.show()
