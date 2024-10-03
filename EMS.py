import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='employee_management',
            user='root',  
            password='Yogesh@24'  
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def add_employee(first_name, last_name, age, department, salary):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO employees (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"
            values = (first_name, last_name, age, department, salary)
            cursor.execute(query, values)
            connection.commit()
            print("Employee added successfully.")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def view_all_employees():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def update_employee(emp_id, first_name=None, last_name=None, age=None, department=None, salary=None):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "UPDATE employees SET "
            updates = []
            values = []
            
            if first_name:
                updates.append("first_name = %s")
                values.append(first_name)
            if last_name:
                updates.append("last_name = %s")
                values.append(last_name)
            if age:
                updates.append("age = %s")
                values.append(age)
            if department:
                updates.append("department = %s")
                values.append(department)
            if salary:
                updates.append("salary = %s")
                values.append(salary)
            
            query += ", ".join(updates) + " WHERE emp_id = %s"
            values.append(emp_id)
            cursor.execute(query, tuple(values))
            connection.commit()
            print("Employee updated successfully.")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def delete_employee(emp_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM employees WHERE emp_id = %s"
            cursor.execute(query, (emp_id,))
            connection.commit()
            print("Employee deleted successfully.")
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            connection.close()

def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            add_employee(first_name, last_name, age, department, salary)
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            emp_id = int(input("Enter employee ID to update: "))
            first_name = input("Enter new first name (leave blank to skip): ") or None
            last_name = input("Enter new last name (leave blank to skip): ") or None
            age = input("Enter new age (leave blank to skip): ")
            department = input("Enter new department (leave blank to skip): ") or None
            salary = input("Enter new salary (leave blank to skip): ")
            age = int(age) if age else None
            salary = float(salary) if salary else None
            update_employee(emp_id, first_name, last_name, age, department, salary)
        elif choice == '4':
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(emp_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
