import sqlite3
conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#           first text,
#           last text,
#           pay integer)
# """)

c.execute("""
    ALTER TABLE employees ADD pay integer
""")
conn.commit() #commits the current transaction to the database
conn.close() #close the connection