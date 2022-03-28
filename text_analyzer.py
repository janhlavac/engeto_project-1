'''
author =Jan Hlavac
'''
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
jmeno = input("username:")
heslo = input("password:")
prihlasovaci_udaje = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"

}
if not jmeno in prihlasovaci_udaje or prihlasovaci_udaje[jmeno] != heslo:
    print("unregistered user, terminating the program..")
    quit()
cara = "=" * 35
print(cara)
print(f"""Welcome to the app, {jmeno}
We have 3 texts to be analyzed.""")
print(cara)
cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
cislo_textu_int = int(cislo_textu)
print(cara)
vycistena_slova = []
for slovo in TEXTS[cislo_textu_int - 1].split():
    ciste_slovo = slovo.strip(",.:;'")
    vycistena_slova.append(ciste_slovo)
pocet_slov = 0
pocet_slov_velkych = 0
pocet_slov_velka = 0
pocet_slov_mala = 0
pocet_cisel = 0
soucet_cisel = 0
nejdelsi_slovo = 0
for slovo in vycistena_slova:
    if not (slovo).isdigit():
        pocet_slov += 1
    if slovo[0].isupper():
        pocet_slov_velkych = pocet_slov_velkych + 1
    if slovo.isupper():
        pocet_slov_velka += 1
    if slovo.islower():
        pocet_slov_mala += 1
    if str.isdigit(slovo):
        pocet_cisel = pocet_cisel + 1
        soucet_cisel += int(slovo)
    if len(slovo) > nejdelsi_slovo:
        nejdelsi_slovo = len(slovo)
histogram = [0] * (nejdelsi_slovo + 1)
nejvetsi_cetnost = 0
for slovo in vycistena_slova:
    histogram[len(slovo) - 1] += 1
    if histogram[len(slovo) - 1] > nejvetsi_cetnost:
        nejvetsi_cetnost = histogram[len(slovo) - 1]
print(f"""There are {pocet_slov} words in the selected text.""")
print(f"""There are {pocet_slov_velkych} titlecase words.""")
print(f"""There are {pocet_slov_velka} uppercase words.""")
print(f"""There are {pocet_slov_mala} lowercase words.""")
print(f"""There are {pocet_cisel} numeric strings.""")
print(f"""The sum of all the numbers {soucet_cisel}.""")
print(cara)
print("LEN| OCCURENCES |NR.")
for i in range(0, nejdelsi_slovo - 1):
    print(f"{i + 1: >3}|{'*' * histogram[i]:<{nejvetsi_cetnost}}|{histogram[i]}")



