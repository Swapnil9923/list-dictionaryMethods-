# list_practice.py

# Sample dataset: List of people with their names, ages, and cities
data = [
    ["John", 28, "New York"],
    ["Emma", 22, "London"],
    ["Liam", 35, "Sydney"],
    ["Olivia", 27, "Paris"],
    ["Noah", 40, "Tokyo"],
    ["Ava", 30, "Berlin"],
    ["Ethan", 33, "Rome"],
    ["Sophia", 29, "Toronto"],
    ["James", 45, "Chicago"],
    ["Mia", 32, "Dubai"],
    ["Lucas", 26, "Mumbai"],
    ["Isabella", 36, "Moscow"],
    ["Henry", 24, "Seoul"],
    ["Charlotte", 31, "Cape Town"],
    ["Alexander", 38, "Madrid"],
    ["Amelia", 28, "Beijing"],
    ["Benjamin", 41, "Los Angeles"],
    ["Harper", 23, "São Paulo"],
    ["Jack", 27, "Mexico City"],
    ["Evelyn", 34, "Istanbul"],
    ["Sebastian", 39, "Vienna"],
    ["Ella", 26, "Stockholm"],
    ["Jackson", 37, "Warsaw"],
    ["Grace", 30, "Cairo"],
    ["Daniel", 44, "Shanghai"],
    ["Victoria", 25, "Rio de Janeiro"],
    ["Matthew", 32, "Buenos Aires"],
    ["Chloe", 29, "Vancouver"],
    ["Joseph", 33, "Dubai"],
    ["Zoey", 31, "New Delhi"],
    ["David", 36, "San Francisco"],
    ["Lily", 40, "Barcelona"],
    ["Andrew", 42, "Amsterdam"],
    ["Hannah", 27, "Lisbon"],
    ["Samuel", 38, "Zurich"],
    ["Sofia", 35, "Prague"],
    ["Anthony", 29, "Brussels"],
    ["Avery", 30, "Dublin"],
    ["Christopher", 37, "Oslo"],
    ["Aria", 28, "Vienna"],
    ["Joshua", 43, "Berlin"],
    ["Scarlett", 32, "Hong Kong"],
    ["Gabriel", 26, "Sydney"],
    ["Layla", 27, "Munich"],
    ["Dylan", 39, "Tokyo"],
    ["Lillian", 41, "London"],
    ["Nathan", 31, "Toronto"],
    ["Nora", 36, "Paris"],
    ["Caleb", 34, "Moscow"],
    ["Zoe", 29, "New York"],
    ["Christian", 45, "Cape Town"],
    ["Penelope", 23, "Rio de Janeiro"],
    ["Isaac", 40, "Mexico City"],
    ["Camila", 30, "Madrid"],
    ["Aaron", 32, "Beijing"],
    ["Riley", 28, "Warsaw"],
    ["Ryan", 33, "Rome"],
    ["Leah", 24, "Vienna"],
    ["Luke", 35, "Los Angeles"],
    ["Paisley", 26, "Buenos Aires"],
    ["Owen", 38, "Dubai"],
    ["Ellie", 27, "New Delhi"],
    ["Julian", 29, "Cairo"],
    ["Violet", 34, "Shanghai"],
    ["Brandon", 42, "Istanbul"],
    ["Savannah", 31, "Amsterdam"],
    ["Adam", 41, "Chicago"],
    ["Audrey", 30, "Lisbon"],
    ["Isaiah", 36, "Prague"],
    ["Bella", 25, "Cape Town"],
    ["Cameron", 37, "Brussels"],
    ["Aurora", 33, "Stockholm"],
    ["Connor", 28, "San Francisco"],
    ["Hazel", 26, "Barcelona"],
    ["Eli", 40, "Amsterdam"],
    ["Stella", 24, "Rome"],
    ["Robert", 43, "Dubai"],
    ["Lucy", 32, "Munich"],
    ["Hudson", 35, "Vancouver"],
    ["Willow", 27, "Cairo"],
    ["Nolan", 39, "New York"],
    ["Maya", 34, "Zurich"],
    ["Asher", 29, "Madrid"],
    ["Claire", 30, "Oslo"],
    ["Lincoln", 41, "Tokyo"],
    ["Elena", 28, "Berlin"],
    ["Grayson", 38, "Mexico City"],
    ["Madison", 31, "London"],
    ["Hunter", 37, "Sydney"],
    ["Ivy", 25, "Toronto"],
    ["Leo", 26, "Paris"],
    ["Eleanor", 33, "Moscow"],
    ["Thomas", 42, "Vienna"],
    ["Addison", 29, "Beijing"],
    ["Jason", 45, "Hong Kong"]
]

# Example: Print the first 5 records
#print("First 5 records:")
#for record in data[:5]:
 #   print(record)


# Append 

data =["jason",45,"hong kong"]

data.append("china")

print(f'data after append {data}')


# 2nd Example 

data =[["Grayson", 38, "Mexico City"], 
["Madison", 31, "London"],
["Hunter", 37, "Sydney"]]

print(f'data before append{data}')

data.append("wolrd")

print(f'data after append{data}')


print('-------')
print('-------')
print('-------')

# Clear 

data =["Scarlett", 32, "Hong Kong"]

print(f'data before clear{data}')

data.clear()


print(f'data after clear{data}')

print('-------')
print('-------')
print('-------')

# Copy 

data= ["Joseph", 33, "Dubai"]

print(f'data before copy{data}')

data.copy()

print(f'data after copy{data}')


print('-----')
print('-----')
print('-----')

# Count

data = ["Ellie", 27, "New Delhi"]

print(f'data before count{data}')

data.count("New delhi")

print(f'data after count{data}')

print('----')
print('----')
print('----')
print('----')

# 2nd example 

points=[1,2,3,3,4,4,5,6,7,8,8,8,8]

points.count(8)

print(points.count(8))

print('-----')
print('-----')
print('-----')
print('-----')

#Extend 

data =["Thomas", 42, "Vienna"]

print(f'data before extend{data}')

data2 = ["footballer","Handsome"]

data.extend(data2)

print(f'data after extend{data}')

print('------')
print('------')
print('------')
print('------')



print('-----')
print('-----')
print('-----')
print('-----')

# Insert

data =["Leah", 24, "Vienna"]

print(f'data before insert{data}')

data.insert(3,"USA")
      
print(f'data after insert{data}')

print('-----')
print('-----')
print('-----')
print('-----')

# POP
data =["Jack", 27, "Mexico City"]

print(f'data before pop{data}')

data.pop(1)

print(f'data after pop{data}')

print('----')
print('----')
print('----')

# Remove
data =["Jack", 27, "Mexico City"]

print(f'data before remove{data}')

data.remove(27)

print(f'data after remove{data}')

print('------')
print('------')
print('------')

# reverse

data =["John", 28, "New York"]

print(f'data before reverse{data}')

data.reverse()

print(f'data after reverse{data}')

print('-----')
print('-----')
print('-----')

# sort 

data =["John", "New York"]
print(f'data before sort{data}')

data.sort()
print(f'data after sort{data}')

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(f'cars after sort{cars}')