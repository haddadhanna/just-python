import random
import mypackage.dice

for i in range(3):
    print(random.randint(10, 20))

members = ['Hanna', 'Camil', 'Haddad']
print(random.choice(members))

dice = mypackage.dice.Dice()
print(dice.roll())