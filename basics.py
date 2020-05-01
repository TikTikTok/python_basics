import psycopg2
from psycopg2 import connect, extensions, sql

conn = psycopg2.connect(
    database = "updatedatabse",
    user = "postgres",
    password = "password",
    host = "localhost",
    port = "5432"
)

autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
print ("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# set the isolation level for the connection's cursors
# will raise ActiveSqlTransaction exception otherwise
conn.set_isolation_level( autocommit )

print(" Postgres connected!!!!!!!! ")

cursor = conn.cursor();

name_Database   = "UpdateDatabse";

sqlCreateDatabase = "create database "+name_Database+";"

# cursor.execute(sqlCreateDatabase);


cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Ramya', 'Rama Priya', 27, 'F', 9000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Vinay', 'Battacharya', 20, 'M', 6000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Sharukh', 'Sheik', 25, 'M', 8300)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Sarmista', 'Sharma', 26, 'F', 10000)''')

cursor.execute('''INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
   ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

#Retrieving data
cursor.execute('''SELECT * from EMPLOYEE''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching all the rows before the update
print("Contents of the Employee table: ")
cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())

#Updating the records
sql = '''UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX = 'M' '''
cursor.execute(sql)
print("Table updated...... ")

#Fetching all the rows after the update
print("Contents of the Employee table after the update operation: ")
cursor.execute('''SELECT * from EMPLOYEE''')
print(cursor.fetchall())

#Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()


