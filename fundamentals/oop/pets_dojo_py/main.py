from ninja import *
from pet import *

# NINJA BONUS: Use modules to separate out the classes into different files.

red_ninja = Ninja('Christian', 'Ramirez', frog, ['cookies', 'brownies', 'cake'], ['Steaks', 'Chicken', 'Sausage'])
red_ninja.feed()
red_ninja.walk()
red_ninja.bathe()

print(red_ninja.pet.name)

#SENSEI BONUS: Use Inheritance to create sub classes of pets.

kitten = Cat('Cleo', 'Leopard', ['Flips', 'Juggles', 'Bites'], 'Purrr')
kitten.noise()

snoop = Dog('Snoop', 'beagle', ['Jokes', 'Talks', 'charming'], 'Woof woof')
snoop.noise()