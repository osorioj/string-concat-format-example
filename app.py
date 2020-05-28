# Ask user for name
name = input("What is your name?: ")

# Ask user for age
age = int(input("What is your age?: "))

# Ask user for city
city = input("What city do you live in?: ")

# Ask user for their hobby
hobby = input("What is your hobby?: ")

# Process output / concatenate example
#output = "Your name is " + name + " and you are " + str(age) + " year(s) old. You live in " + city + " and enjoy " + hobby + "."

# Process output / format example
string = "Your name is {} and you are {} years old. You live in {} and you love {}."

output = string.format(name, age, city, hobby)

# Print output
print(output)