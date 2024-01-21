import mysql.connector
import csv

# Establish a connection to the MySQL database

mydb = mysql.connector.connect(
    host="127.0.0.1",
    
    port=3306,  # Specify the MySQL server port
    user="root",
    password="",
    database="mayur")
# Create a cursor to execute SQL queries
mycursor = mydb.cursor()

# Read data from CSV file and prepare the values
#with open('D:\send\sample_data.txt') as csv_file:
 #   csv_reader = csv.reader(csv_file, delimiter=',')
  #  all_values = [tuple(row) for row in csv_reader]


# Read data from CSV file and skip the header
with open('D:\\send\\sample_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip the header row
    all_values = [tuple(row) for row in csv_reader]

# Define the query to insert data into the 'Employee' table

query = "INSERT INTO `test` (`ID`, `First_Name`, `Last_Name`) VALUES (%s, %s, %s)"


# Execute the query with the data
mycursor.executemany(query, all_values)

# Commit the changes to the database
mydb.commit()

# Close the cursor and database connection
mycursor.close()
mydb.close()
