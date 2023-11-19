import pandas as pd

# #Read CSV and print
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)

# # Print ages in a Serie
# ages = [23,45,7,34,6,63,36,78,54,34]
# data = pd.Series(ages)
# print(data)

# #Print date range
# date_range = pd.date_range("05-01-2021", "05-12-2021")
# print(date_range)

# #Series apply and print
# my_series = pd.Series([2, 4, 6, 8, 10])
# print(my_series.apply(lambda x:x/2))

# #Create car DataFrame and print
# data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
# data_frame = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
# print(data_frame)

# #Create DataFrame with 'dict' and print
# data = [
#     { 
#         "brand": "Toyota", 
#         "make": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "make": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porche", 
#         "make": "Cayenne",
#         "color": "White"
#     },
#     {
#         "brand": "Tesla", 
#         "make": "Model S",
#         "color": "Red"
#     }
# ]
# data_frame = pd.DataFrame(data)
# print(data_frame)

# #Retrieve any cel
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.iloc[133, 6])

# #Retrieve first three rows
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.head(3))

# #Retrieve last three rows
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.tail(3))

# #Retrieve Name and Type of the first five elements
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame[['Name', 'Type 1']][0:10])

# #Retrieve pokemons with an attack of more than 80
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame.loc[data_frame['Attack'] > 80])

# #Retrieve legendary pokemon count
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(len(data_frame.loc[data_frame['Legendary']]))

# #Print first five baby names
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data_frame.head(5))

# #Print first five baby names
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data_frame.head(5))

# #Remove first column and print first five elements
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# del data_frame[data_frame.columns[0]]
# print(data_frame.head(5))

# #Print DataFrame Gender values count
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(data_frame['Gender'].value_counts())

# #Group by name and print the count of groups
# data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
# print(len(data_frame.groupby('Name').sum()))