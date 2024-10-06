employees = {
    1001: {"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"},
    1002: {"Name": "Bob", "Department": "Finance", "Position": "Analyst", "Salary": 58000, "Join Date": "2017-09-15", "Project Allocated": "Budget Planning"},
    1003: {"Name": "Charlie", "Department": "IT", "Position": "Developer", "Salary": 90000, "Join Date": "2019-01-10", "Project Allocated": "App Development"},
    1004: {"Name": "David", "Department": "Sales", "Position": "Sales Executive", "Salary": 67000, "Join Date": "2016-05-22", "Project Allocated": "Lead Generation"},
    1005: {"Name": "Eva", "Department": "Marketing", "Position": "SEO Specialist", "Salary": 54000, "Join Date": "2020-03-14", "Project Allocated": "SEO Campaign"},
    1006: {"Name": "Frank", "Department": "HR", "Position": "Recruiter", "Salary": 45000, "Join Date": "2021-07-19", "Project Allocated": "Campus Hiring"},
    1007: {"Name": "Grace", "Department": "IT", "Position": "System Admin", "Salary": 78000, "Join Date": "2018-11-07", "Project Allocated": "Network Maintenance"},
    1008: {"Name": "Hannah", "Department": "Sales", "Position": "Sales Manager", "Salary": 85000, "Join Date": "2014-08-25", "Project Allocated": "Corporate Sales"},
    1009: {"Name": "Ivy", "Department": "Finance", "Position": "Accountant", "Salary": 62000, "Join Date": "2016-12-05", "Project Allocated": "Audit"},
    1010: {"Name": "Jack", "Department": "Marketing", "Position": "Social Media Manager", "Salary": 68000, "Join Date": "2018-02-28", "Project Allocated": "Branding Campaign"},
    1011: {"Name": "Kevin", "Department": "HR", "Position": "Trainer", "Salary": 50000, "Join Date": "2019-10-15", "Project Allocated": "Employee Onboarding"},
    1012: {"Name": "Liam", "Department": "IT", "Position": "Security Specialist", "Salary": 98000, "Join Date": "2021-01-03", "Project Allocated": "Cybersecurity Audit"},
    1013: {"Name": "Mia", "Department": "Finance", "Position": "Finance Manager", "Salary": 93000, "Join Date": "2014-03-12", "Project Allocated": "Investment Planning"},
    1014: {"Name": "Noah", "Department": "Marketing", "Position": "Content Creator", "Salary": 47000, "Join Date": "2022-05-09", "Project Allocated": "Blog Strategy"},
    1015: {"Name": "Olivia", "Department": "HR", "Position": "HR Executive", "Salary": 62000, "Join Date": "2017-12-22", "Project Allocated": "Employee Satisfaction"},
    1016: {"Name": "Paul", "Department": "Sales", "Position": "Regional Manager", "Salary": 89000, "Join Date": "2015-11-03", "Project Allocated": "Expansion Plan"},
    1017: {"Name": "Quinn", "Department": "IT", "Position": "Data Scientist", "Salary": 102000, "Join Date": "2019-07-30", "Project Allocated": "AI Implementation"},
    1018: {"Name": "Rachel", "Department": "Finance", "Position": "Tax Consultant", "Salary": 76000, "Join Date": "2020-08-19", "Project Allocated": "Tax Filing"},
    1019: {"Name": "Sam", "Department": "Sales", "Position": "Sales Representative", "Salary": 49000, "Join Date": "2022-01-12", "Project Allocated": "Client Acquisition"},
    1020: {"Name": "Tina", "Department": "Marketing", "Position": "Brand Manager", "Salary": 71000, "Join Date": "2016-06-30", "Project Allocated": "Rebranding"},
    1021: {"Name": "Uma", "Department": "HR", "Position": "HR Manager", "Salary": 80000, "Join Date": "2014-04-17", "Project Allocated": "Leadership Development"},
    1022: {"Name": "Victor", "Department": "IT", "Position": "Database Admin", "Salary": 92000, "Join Date": "2018-10-11", "Project Allocated": "Database Migration"},
    1023: {"Name": "Wendy", "Department": "Finance", "Position": "Financial Analyst", "Salary": 61000, "Join Date": "2019-02-22", "Project Allocated": "Market Analysis"},
    1024: {"Name": "Xavier", "Department": "Sales", "Position": "Sales Coordinator", "Salary": 53000, "Join Date": "2021-06-13", "Project Allocated": "Retail Sales"},
    1025: {"Name": "Yara", "Department": "Marketing", "Position": "PR Manager", "Salary": 85000, "Join Date": "2013-09-14", "Project Allocated": "Public Relations"},
    1026: {"Name": "Zack", "Department": "IT", "Position": "Cloud Engineer", "Salary": 105000, "Join Date": "2021-04-08", "Project Allocated": "Cloud Migration"},
    1027: {"Name": "Adam", "Department": "HR", "Position": "Compensation Analyst", "Salary": 57000, "Join Date": "2016-08-21", "Project Allocated": "Payroll"},
    1028: {"Name": "Bella", "Department": "Finance", "Position": "Credit Analyst", "Salary": 68000, "Join Date": "2018-12-03", "Project Allocated": "Risk Analysis"},
    1029: {"Name": "Caleb", "Department": "Sales", "Position": "Sales Trainer", "Salary": 62000, "Join Date": "2020-09-27", "Project Allocated": "Sales Workshop"},
    1030: {"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"},
    # ... continue adding until you reach 100 employees ...
}


print('----')
print('----')
print('----')
print('----')
# Clear method

employees ={"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"}

print(f'emplyees before clear{employees}')

employees.clear()

print(f'employees after clear{employees}')

print('------')
print('------')
print('------')
print('------')

# Copy Method

employees ={"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"}

print(f'employees before copy{employees}')

employees.copy()

print(f'employees after copy{employees}')

print('------')
print('------')
print('------')
print('------')

# get 

employees ={"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"}

print(f'employees before get{employees}')

X = employees.get("Name")

print(f'X after get{X}')

print('------')
print('------')
print('------')
print('------')

# Items 

employees = {"Name": "Diana", "Department": "Marketing", "Position": "Digital Strategist", "Salary": 74000, "Join Date": "2017-05-18", "Project Allocated": "Digital Transformation"}

print(f'employees before items{employees}')

employees.items()

print(f'employees after items{employees}')


print('------')
print('------')
print('------')
print('------')

#  keys 

employees = {"Name": "Hannah", "Department": "Sales", "Position": "Sales Manager", "Salary": 85000, "Join Date": "2014-08-25", "Project Allocated": "Corporate Sales"}

print(f'employees before keys{employees}')

X = employees.keys()

print(X)

print('------')
print('------')
print('------')
print('------')

# Pop

employees ={"Name": "Frank", "Department": "HR", "Position": "Recruiter", "Salary": 45000, "Join Date": "2021-07-19", "Project Allocated": "Campus Hiring"}

print(f'employees before pop{employees}')

X = employees.pop("Name")

print(f'x after pop{X}')

print('------')
print('------')
print('------')
print('------')

# popitems
employees ={"Name": "Frank", "Department": "HR", "Position": "Recruiter", "Salary": 45000, "Join Date": "2021-07-19", "Project Allocated": "Campus Hiring"}

print(f'employees before popitems{employees}' )

X =employees.popitem()


print(f'X after popitems{X}')

print('------')
print('------')
print('------')
print('------')


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(f'car before popitems{car}')
X = car.popitem()

print(f'X after popitems{X}')

print('------')
print('------')
print('------')
print('------')

# set default

employees ={"Name": "Frank", "Department": "HR", "Position": "Recruiter", "Salary": 45000, "Join Date": "2021-07-19", "Project Allocated": "Campus Hiring"}

print(f'employees before setdefault{employees}')

X =employees.setdefault("Department","Biotechnology")

print(f'X after setdefault{X}')


print('------')
print('------')
print('------')
print('------')

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f'car before setdefault{car}')
x = car.setdefault("model", "Bronco")

print(f'x afetr setdefault{x}')

print('------')
print('------')
print('------')
print('------')

# Update 

employees ={"Name": "Bob", "Department": "Finance", "Position": "Analyst", "Salary": 58000, "Join Date": "2017-09-15", "Project Allocated": "Budget Planning"}
print(f'employees before update{employees}')

employees.update({"Position" : "Senior Analyst"})

print(f'employees after update{employees}')

print('------')
print('------')
print('------')
print('------')

# Values

employees ={"Name": "Bob", "Department": "Finance", "Position": "Analyst", "Salary": 58000, "Join Date": "2017-09-15", "Project Allocated": "Budget Planning"}

print(f'employees before values{employees}')

X = employees.values()

print(f'X after values{X}')

print('------')
print('------')
print('------')
print('------')

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(f'cars before values{car}')
x = car.values()

car["year"] = 2018

print(f'x after values{x}')
