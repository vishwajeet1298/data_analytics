import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
customers_data=pd.read_csv('customers.csv')
#To display the top 5 rows, Matrix(rows*columns) -> head() is used 
print(customers_data.head())
#To display the bottom 5 rows, Matrix(rows*columns) -> tail() is used 
print(customers_data.tail())
#To get information about the Columns,  Non-Null Values Count, Data Type of those Columns, Class of Data, index values,RangeIndex along with memory uses
customers_data.info()


# to remove trailing spaces from column names of the main customers csv data
customers_data.columns = customers_data.columns.str.strip()

'''to set the maximum number of rows to display in the output, we can use the pd.options.display.max_rows attribute. 
By default, it is set to 60, but we can change it to a higher value to display more rows if needed.'''
pd.options.display.max_rows=9999
print("Display Maximum rows: ",pd.options.display.max_rows) 

#To get the iloc (integer location) of the DataFrame, which allows us to access specific rows and columns by their integer index.
print(customers_data.iloc[[0,1,2]])

#To get data type of the specific column from a specific dataframe
print(type(customers_data["Website"]))
#To get specific columns from a DataFrame
website=customers_data["Website"]
print(website.head())
#To get data type of new dataframe
print(type(website))
# shape generally return the total number of rows in a column
print("Number of Websites:", website.shape)

#To get the total number of Comapany in customers_data dataframe
print(customers_data["Company"].shape)

#To copy few columns data from main dataframe to another new dataframe
companies_info_df=customers_data[["Company","Website","Subscription Date"]].copy()  # copies Company","Website","Subscription Date Column in new dataframe
print(companies_info_df.head())

np.random.seed(123)  # to ensure reproducibility of random numbers
companies_info_df["Employee Count"]=np.random.randint(0,501,size=len(companies_info_df))
#to convert the data type of Employee Count to int64
companies_info_df["Employee Count"] = companies_info_df["Employee Count"].astype("int64")
print(companies_info_df.to_string(index=False)) # this can halt or make terminal unresponsive for large data
#or
print(companies_info_df.head(20).to_string(index=False))
# or
print(companies_info_df.sample(20, random_state=0).to_string(index=False))
companies_info_df.info()
print(companies_info_df.head())

'''To save this new DataFrame in local system as csv file, we can use to_csv() method of pandas DataFrame. 
The index=False argument is used to prevent the index from being saved as a separate column in the CSV file.'''
#companies_info_df.to_csv("companies_information_dataframe.csv", index=False)

'''describe method is used to get total count, mean, median, std deviation, min value, 25%, 50%, 75%, max value.
Generally it works only on the Numerical Data in the DataFrame but if we write decribe(include="all"), it shows extended information'''
print(companies_info_df.describe(include="all"))
print("Display Column Names Only from a DataFrame",companies_info_df.columns) # to print Column Names only

companies_info_df.info()
# to convert  to list
print("Columns from the dataframe are converted to list",companies_info_df.columns.tolist())
# this helps to remove trailing spaces from column names 
companies_info_df.columns.str.strip()

#to convert date from string to Date_Time format 
companies_info_df["Subscription Date"] = pd.to_datetime(companies_info_df["Subscription Date"], errors="coerce")
companies_info_df.info()

#to insert two more columns from main csv data to new dataframe- companies_info_df at specified location 0 and 1
companies_info_df.insert(0, "First Name", customers_data["First Name"])
companies_info_df.insert(1, "Last Name",  customers_data["Last Name"])

# Add a new Column named Age in companies_info_df.csv
companies_info_df["Age"]=np.random.randint(18,61,size=len(companies_info_df)).astype("int64")
print(companies_info_df.head())

#To Save this new dataFrame with Age Column
companies_info_df.to_csv("companies_information_dataframe.csv", index=False)









