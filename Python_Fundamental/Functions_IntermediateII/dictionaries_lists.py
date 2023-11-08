#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changeValue(x):
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if x[i][j] == 10:
                x[i][j] = 15
    return x
print(changeValue(x)) 

#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
def changeLastName(students):
    students[0]['last_name'] = 'Bryant'
    return students  
print(changeLastName(students))  

#3. In the sports_directory, change 'Messi' to 'Andres'
def changeValue(sports_directory):
    for value in sports_directory.values():
        #print(value)
        for i in range(0, len(value)):
           if value[i] == 'Messi':
               value[i] = 'Andres'
    return sports_directory           
                  
print(changeValue(sports_directory))

#4. Change the value 20 in z to 30
def changeValue_in_z(z):
    for key in z[0].keys():
        #print(key)
        if z[0][key] == 20:
            z[0][key] = 30
    return z
print(changeValue_in_z(z))

#2. Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
def iterateDictionary(students):
    for i in range(0, len(students)):
        for key, value in students[i].items():
            print(key,'-',value)

iterateDictionary(students) 

#3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, students):
    for i in range(0, len(students)):
        for key, value in students[i].items():
            if key == key_name:
                print(value)

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, values in dojo.items():
        print(len(values), key.upper())
        for val in values:
            print(val)

printInfo(dojo)

