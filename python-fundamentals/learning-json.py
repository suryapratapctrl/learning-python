import json

#to write

employees = [
    {"Name": "Alex", "Salary": 60000},
    {"Name": "Bob", "Salary": 45000}
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

#to read


with open("employees.json", "r") as file:
    data = json.load(file)

print(data)

for employee in data:
    print(employee)

#to append 


new_employee = {"Name": "Charlie", "Salary": 70000}

# Read existing data
with open("employees.json", "r") as file:
    employees = json.load(file)

# Add new employee
employees.append(new_employee)

# Write updated data back
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)    