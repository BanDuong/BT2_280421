import pandas
import mysql.connector as mc
from sqlalchemy import create_engine

MYSQL_USER 		= 'root'
MYSQL_PASSWORD 	= 'lovestory99'
MYSQL_HOST_IP 	= '127.0.0.1'
MYSQL_PORT		= '3306'
MYSQL_DATABASE	= 'customers'

'''
table = "CREATE TABLE cusInfor (" \
        "customerid INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
        "firstname VARCHAR(50)," \
        "lastname VARCHAR(50)," \
        "companyname VARCHAR(255)," \
        "billingaddress1 VARCHAR(255)," \
        "billingaddress2 VARCHAR(255)," \
        "city VARCHAR(50)," \
        "state VARCHAR(10)," \
        "postalcode VARCHAR(20)," \
        "country VARCHAR(50)," \
        "phonenumber VARCHAR(30)," \
        "emailaddress VARCHAR(70)," \
        "Createddate VARCHAR(30))"

mycursor = mydb.cursor()
mycursor.execute(table)
'''

cus_list = pandas.read_csv("customer.csv")

engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+MYSQL_PORT+'/'+MYSQL_DATABASE, echo=False)

#cus_list.to_sql(name='cusinfor',con=engine,if_exists='replace',index=False)
#print(engine.execute("SELECT * FROM customers.cusInfor").fetchall())
print(pandas.read_csv("customer.csv").head())
