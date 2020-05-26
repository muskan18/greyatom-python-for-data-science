# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings

new_class = class_1+class_2
# Append the list


new_class.append('Peter Warden')

new_class.remove('Carla Gentry')

#print(new_class)


# Create the Dictionary
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
l = courses.values()
total = sum(l)
#print(total)
# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`

# Print the total
percentage = (total/500)*100
# Insert percentage formula

# Print the percentage

#print(percentage)


# Create the Dictionary
mathematics = {"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,  "Hilary Mason" :70,"Corinna Cortes":66,"Peter Warden":75}

topper = max(mathematics,key = mathematics.get)
#print(topper)

tpon = topper.split()

first_name = tpon[-1]

Last_name = tpon[0]
# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

full_name = first_name+" "+Last_name

# Concatenate the string

# print the full_name

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


