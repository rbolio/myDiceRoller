"""
Small project to run attacks
"""
from random import randrange


class the_math:
    def roll(self, amount, sides):
        """function to roll and return"""
        total = 0

        for x in range(0, amount):
            die_value = randrange(1, sides)
            print(f"Rolled a D{sides}, got {die_value}")
            total += die_value
        return total

    def readAttack(self, diceList):
        total = 0
        for rollInstruction in diceList:
            if "d" in rollInstruction:
                string_split = rollInstruction.split("d")
                total += self.roll(int(string_split[0]), int(string_split[1]))
        return total


class spells:
    def __init__(self, name, dice_list, spell_level, extra_damage):
        self.name = name
        self.dice_list = dice_list
        self.spell_level = spell_level
        self.extra_damage = extra_damage


class myChar:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.available_spells = []

    def add_spell(self, spell_name, hit_dice_list, spell_level, extra_dmg):
        new_spell = spells(spell_name, hit_dice_list, spell_level, extra_dmg)
        self.available_spells.append(new_spell)
        print("{} was added to the spell list".format(new_spell.name))

    def attack(self, spell_name):
        attack_spell = self.get_spell_data(spell_name)
        damage = the_math()
        if attack_spell:
            print("Hit with {}".format(damage.readAttack(attack_spell.dice_list)))

    def get_spell_data(self, spell_name):
        for spell in self.available_spells:
            if spell.name == spell_name:
                return spell
        return False


if __name__ == "__main__":
    char = myChar("Stelion the Covert", 8)
    char.add_spell("Fireball", ["8d6"], 3, 0)
    char.attack("Fireball")
