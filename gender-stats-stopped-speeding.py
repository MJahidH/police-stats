from  read_file import data

# prints the first few rows  
# print(data.head())
# print(data.violation)

print(data[data.violation == "Speeding"].driver_gender.value_counts())



