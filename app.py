from employee import Employee
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


emp_1 = Employee("Ajay", "Srilal",42000)


emp_2 = Employee("Johnson", "Jess",12000)


print(emp_1.first)


c.execute("""
    SELECT * FROM employees WHERE last='Panicker'
""")

# Dont use string formatting for inserting to the database
c.execute("""
    INSERT INTO employees (first, last, pay) VALUES (?, ?, ?)
    """, (emp_1.first, emp_1.last, emp_1.pay))


c.execute("""
    INSERT INTO employees VALUES (:first, :last, :pay)
""",{'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# Preferred way!!

# print(c.fetchone())
# print(c.fetchall())
# c.fetchmany(5) #fetch
# c.fetchall()
conn.commit() #commits the current transaction to the database
conn.close() #close the connection