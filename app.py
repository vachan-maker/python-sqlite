import sqlite3
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#           first text,
#           last text,
#           pay integer)
# """)

# c.execute("""
#     ALTER TABLE employees ADD pay integer
# """)

# c.execute("""
#     INSERT INTO employees VALUES ("Arjun", "Panicker",20000)    
# """)
c.execute("""
    SELECT * FROM employees WHERE last='Panicker'
""")
# print(c.fetchone())
print(c.fetchall())
# c.fetchmany(5) #fetch
# c.fetchall()
conn.commit() #commits the current transaction to the database
conn.close() #close the connection