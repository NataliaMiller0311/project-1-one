"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Natalie Millerová
email: inventuranata@seznam.cz
discord: Natalka
"""
import re

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

delici_čára = ("----------------------------------------")
registrovany_uzivatele = {
    'bob': {
    'heslo': '123',
  },
    'ann': {
    'heslo': 'pass123'
  },
    'mike': {
    'heslo': 'pasword123',
   }, 
    'liz': {
    'heslo': 'pass123',
  }
  }
  


jmeno = input("zadejte jmeno: ")
uzivatel = registrovany_uzivatele.get(jmeno)

if uzivatel == None:
    print("uzivatel", jmeno, "neregistrován, ukončuji program")
    quit()

zadane_heslo = input("zadejte heslo: ")
uzivatelovo_heslo = uzivatel.get('heslo')

if uzivatelovo_heslo == zadane_heslo:
    print(delici_čára)
    print("vitej v aplikaci,", jmeno)
    print("Máme 3 texty k analýze")
    print(delici_čára)


cislo_textu = input("Zadej číslo mezi 1 a 3 pro výběr textu: ")
while not cislo_textu.isdigit() or int(cislo_textu) not in range(1, 4):
    print("Špatné číslo, ukončuji program")
    quit()
text = TEXTS[int(cislo_textu) - 1]

words = text.split()
word_count = len(words)
print(f"There are {word_count} words in the selected text.")

titlecase_count = sum(1 for word in words if word.istitle())
print(f"There are {titlecase_count} titlecase words.")

uppercase_count = sum(1 for word in words if word.isupper())
print(f"There are {uppercase_count} uppercase words.")

lowercase_count = sum(1 for word in words if word.islower())
print(f"There are {lowercase_count} lowercase words.")

numbers = re.findall(r'\b\d+\b', text)
number_count = len(numbers)
print(f"There are {number_count} numeric strings.")

number_sum = sum(int(num) for num in numbers)
print(f"The sum of all the numbers {number_sum}")

print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
word_lengths = [len(word.strip(",.")) for word in words]
unique_lengths = sorted(set(word_lengths))
for length in unique_lengths:
    count = word_lengths.count(length)
    stars = '*' * count
    print(f"{length:2}|{stars:^13}| {count}")





  