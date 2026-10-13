#project-5 oop wrapper

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee (Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.__employee_id = employee_id
        self.__salary = float(salary)


    def get_employee_id(self):
     return self.__employee_id

    def set_employee_id(self,new_id):
     self.__employee_id = new_id

    def get_salary(self):
      return self.__salary 

    def set_salary(self, new_salary):
      if new_salary >= 0:
         self.__salary = float(new_salary)

      else:
          print("Salary cannnot be nagative!")


    def display(self):
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")
      print(f"Employee_id: {self.__employee_id}")
      print(f"Salary: {self.__salary}")

    def _del__(self):
     print(f"Employee {self.name} deleted")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary,department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
      super().display() 
      print(f"Department: {self.department}")

print(f"Is Manager subclass of Employee? {issubclass(Manager,Employee)}")

all_data = []

while True:
    print("\n Choose an operation: ")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\n Enter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        p = Person(name,age)
        all_data.append(p)
        print(f"\n Person created with name: {name}, age: {age}.")
        print("\n --- Choose another operation ---")

    elif choice == '2':
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        
        e = Employee(name,int(age),emp_id,salary)
        all_data.append(e)

        print(f"\nEmployee Details: ")
        print(f"Name: {name}, Age: {age}, Employee ID: {emp_id}, Salary: {float(salary)}")
        print("\n--- Choose another operation ----")


    elif choice == '3':
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        m = Manager(name,int(age),emp_id,salary,dept)
        all_data.append(m)

        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: {float(salary)}, and department: {dept}.")
        print("\n--- Choose another operation ---")

    elif choice == '4':
        print("\n--- Showing All Details ---")
        for obj in all_data:
            obj.display()
            print("---------------------")

    elif choice == '5':
        print("\nExting the system. All resources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice! Try again.")



        


        





      

          
        





