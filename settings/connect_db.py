import psycopg2
import os

host = os.environ.get("DBHOST")
dbname = os.environ.get("DBNAME")
user = os.environ.get("DBUSER")
password = os.environ.get("DBPASSWORD")


def connect():
    print(f"details are {host} {dbname} {user} {password}")
    conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
    print(f"connection string {conn_string}")
    conn = psycopg2.connect(conn_string) 
    cursor = conn.cursor()
    print("connected")
    return [conn,cursor]


def fetchData():
    print("hhii")
    print(os.environ.get("host"))
    connectors = connect()
    conn,cursor = connectors[0],connectors[1]
    postgreSQL_select_Query = "select * from users"
    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from users table using cursor.fetchall")
    publisher_records = cursor.fetchall()
    print(f"length of records are {len(publisher_records)}")
    users = []
    for row in publisher_records:
        ls = [row[1],row[2]]
        print(f"name {ls}")
        users.append(ls)
    conn.close()
    cursor.close()
    
    return users
    


def saveData(name,email):
    connectors = connect()
    conn,cursor = connectors[0],connectors[1]
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    print("data saved!")
    conn.commit()
    cursor.close()
    conn.close()

def createDB():
    connectors = connect()
    conn,cursor = connectors[0],connectors[1]
    cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, name VARCHAR(50), email VARCHAR(50));")
    conn.commit()
    cursor.close()
    conn.close()

'''


conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
print(f"connection string {conn_string}")
conn = psycopg2.connect(conn_string) 
print("Connection established")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed)")

cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")

cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")

conn.commit()
cursor.close()
conn.close()'''