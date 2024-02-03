
import pandas as pandas
import pandas as pd

# Reading CSV file
data_value = pd.read_csv("data.csv")

# Statistical description
data_value.describe()

#Checking for null values
null_values = data_value.isnull().sum()
print(null_values)

#replacing nullvalues with the mean
data_value.fillna(data_value.mean(), inplace=True)
print(data_value)

#Selecting two columns
data_value = data_value[["Duration", "Pulse" ]]

#Aggregating the data 
agg_dict = {"Duration": ["max", "min", "count", "mean"],
            "Pulse": ["max", "min", "count", "mean"]}
agg_data_value = data_value.agg(agg_dict)
print(agg_data_value)

# Filtering the dataframe to select the rows with calories values between 500 and 1000. 
data_value = pd.read_csv("data.csv")
Calories_filter = (data_value["Calories"] >= 500) & (data_value["Calories"] <= 1000)
filtered_data_value = data_value[Calories_filter]
print(filtered_data_value)

#Filtering the dataframe to select the rows with calories values > 500 and pulse < 100.
data_value = pd.read_csv("data.csv")
Calories_filter = (data_value["Calories"] > 500) & (data_value["Pulse"] < 100)
filtered_data_value = data_value[Calories_filter]
print(filtered_data_value)

#Creating a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse” and deleting that maxpulse column from the main df fataframe 
df_modified = data_value.drop(columns=["Maxpulse"])
print(df_modified)

# Converting the datatype of calories column to int datatype
data_value['Calories'] = data_value['Calories'].fillna(0).astype(int)
print(data_value)

# Plotting the output
import matplotlib.pyplot as plt

data_value.plot(kind='scatter', x='Duration', y='Calories', figsize=(6,3))
plt.show()

