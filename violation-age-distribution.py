from  read_file import data

print(data.groupby("violation").driver_age.describe())

