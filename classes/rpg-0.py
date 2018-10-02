"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
    
    def alive(self):
        # if self.health >= 1:
        #     return True
        # else:
        #     return False
        return self.health >= 1
    
class Hero(Character):
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class Goblin(Character):
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

class Zombie(Character) :
    def print_status(self):
        print("The zombie has %d health and %d power." % (self.health, self.power))
    def alive(self):
        return True
    
def main():
    my_hero = Hero(10, 5)
    my_goblin = Goblin(6, 2)
    my_zombie = Zombie(100, 100)
    print()
    while my_hero.alive() and (my_goblin.alive() or my_zombie.alive()):
        my_hero.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. fight zombie")
        print("4. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            my_hero.attack(my_goblin)
            my_goblin.print_status()
        elif user_input == "2":
            pass
        elif user_input == "3":
            my_hero.attack(my_zombie)
            my_zombie.print_status()
        elif user_input == "4":
            print("Goodbye.")
        else:
            print("Invalid input %r" % user_input)

main()
