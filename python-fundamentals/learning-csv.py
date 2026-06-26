import csv

#to write

data = [
    ["A", 60000],
    ["B", 45000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Salary"])
    writer.writerows(data)

#to read 


with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)  

#to append

new_employee = ["C", 70000]

with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(new_employee)            