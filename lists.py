# working with lists
bicycles = ['trek', 'cannondale', 'readline', 'scott', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0,'kawazaki')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('yamaha')
print(motorcycles)

cars = ['bmw', 'jaguar', 'ford', 'audi', 'mercedes']
print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print(len(cars))

# looping through lists

for i in cars:
    print(i)
    print(i.title()+"\n")

for x in range(1,6):
    print(x)

numbers = list(range(1,11))
print(numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

min = min(squares)
max = max(squares)
sum = sum(squares)

print(min, max, sum)

# or with list comprehension

squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)

# slicing lists
names = ['charles', 'matt', 'phil', 'liam', 'carl', 'jen', 'anna']
print(names[0:3])
print(names[-3:])

# copy a list or a bit of a list to create another list
names2 = names[-4:]
print(names2)







