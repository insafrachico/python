x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

x[1][0] = 15
print(x)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 20} ]

print(sports_directory)

z[0]['y']= 30
print(z)
"""________________________________________________________________"""
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary(students):
    for s in students:
        print('first name -',s['first_name'],',',' last name -',s['last_name'])

# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for s in students:
        print(s[key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

""""__________________________________________________"""

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(dojo):
    print(len(dojo['locations']), "LOCATIONS")
    for location in dojo['locations']:
        print(location)
    print()
    print(len(dojo['instructors']), "INSTRUCTORS")
    for instructor in dojo['instructors']:
       print(instructor)
       
printInfo(dojo)
