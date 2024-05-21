import pandas as pd 

data = pd.read_csv(r"./data.csv")


# in the get-data file run the file to get to total amount of rows and compare it to this command check if all values are null
# print(data.isnull().sum())

data.drop(columns="country_name",inplace=True)

print(data)

