from  read_file import data


# print(data["stop_duration"].value_counts())


data["stop_duration"] = data["stop_duration"].map({"0-15 Min" : 7.5, "16-30 Min" : 24, "30+ Min" : 45})

print(data["stop_duration"].mean())

# print(data.head())