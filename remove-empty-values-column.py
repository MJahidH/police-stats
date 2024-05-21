from  read_file import data

# in the get-data file run the file to get to total amount of rows and compare it to this command check if all values are null
# print(data.isnull().sum())

data.drop(columns="country_name",inplace=True)

print(data)

