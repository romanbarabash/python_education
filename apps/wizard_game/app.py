import random
import time

from apps.wizard_game.actors import Creature, Wizard, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------')
    print('          WIZARD GAME APP        ')
    print('---------------------------------')
    print()


def game_loop():
    global hero
    HARRY = 0
    HERMIONA = 1

    enemies = [
        SmallAnimal('Spider', 4),
        SmallAnimal('Bat', 5),
        Creature('Tiger', 45),
        Dragon('Dragon', 200, 13, True),
        Wizard('Evil Wizard', 1000)
    ]

    heroes = [
        Wizard('Harry', 351),
        Wizard('Hermiona', 401)
    ]

    spells = ['Arresto Momentum', 'Avada Kedavra', 'Bombarda Maxima', 'Cistem Aperio', 'Confringo', 'Expulso',
              'Petrificus Totalus', 'Sectumsempra']

    while True:

        cmd_hero = input('Please select your hero: [Ha]rry or [He]rmiona and [q] for exit: ')
        print()

        if cmd_hero.lower() == 'ha':
            hero = heroes[HARRY]
        elif cmd_hero.lower() == 'he':
            hero = heroes[HERMIONA]
        elif cmd_hero.lower() == 'q':
            print()
            print("EXIT GAME")
            print()
            break
        else:
            print("Your hero choice is incorrect, please try again")
            print()
            continue

        while True:

            active_creature = random.choice(enemies)
            spell = random.choice(spells)
            print('A {} of level {} has appear from a foggy forest...'.format(active_creature.name,
                                                                              active_creature.level))
            print()

            cmd_enemy = input('Do you [a]ttack, [r]unaway or [l]ook around? ')
            if cmd_enemy == 'a':
                if hero.attack(active_creature, spell):
                    enemies.remove(active_creature)
                else:
                    print("The wizard runs and hides taking time to recover...")
                    time.sleep(5)
                    print("The wizard return revitalized")
            elif cmd_enemy == 'r':
                print('The Wizard is unsure about his power and just flex')
            elif cmd_enemy == 'l':
                print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
                for c in enemies:
                    print(' * A {} of level {}'.format(c.name, c.level))
            else:
                print('OK, exiting game... bye!')
                print()
                break

            print()

            if not enemies:
                print("You've defeated all the creatures, well done!")
                print()
                break


if __name__ == '__main__':
    main()
