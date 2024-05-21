from  read_file import data

print(data.groupby("driver_gender").search_conducted.value_counts())



