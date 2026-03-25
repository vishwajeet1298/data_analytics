import pandas as pd
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

# want specific columns from a DataFrame
companies=customers_data["Company"]
print(companies.head())
print(type(customers_data["Company"]))
print(type(companies))
# shape generally return the total number of rows in a column
print("Company shape:", companies.shape)
print(customers_data["Company"].shape)

companies_website=customers_data[["Company","Website","Subscription Date"]].copy()
print(companies_website.head())




