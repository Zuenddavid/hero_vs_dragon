import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
try:
    hero_hp = int(input("how many hp does the hero have?"))
    dragon_hp = int(input("how many hp does the dragon have?"))
    hero_max_dmg = int(input("how many dmg does the hero make?"))
    dragon_max_dmg = int(input("how many dmg does the dragon make?"))
except ValueError:
    print("Please give me a proper number")
except:
    print("Some other exception I did not see coming")
"""
hero_hp = 50
dragon_hp = 100
hero_max_dmg = 20
dragon_max_dmg = 10
"""

print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")


while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp = hero_hp - dragon_attack

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    if hero_hp<=0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp = dragon_hp- hero_attack

    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    if dragon_hp <= 0:
        print("Our valiant hero has slain the dragon!")
        break
    continue
    input("Round over. Press any key")