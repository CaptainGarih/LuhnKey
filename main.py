#   Fonction pour calculer le 16ème chiffre de la carte bleue
def luhn_key(card_number):
    
    reversed_digits = card_number[::-1]

    doubled_digits = [int(reversed_digits[i]) * 2 if i % 2 == 1 else int(reversed_digits[i]) for i in range(len(reversed_digits))]

    subtracted_digits = [x - 9 if x > 9 else x for x in doubled_digits]

    total = sum(subtracted_digits)

    if total % 10 == 0:
        key = 0
    else:
        key = 10 - (total % 10)

    return key

state = False
while state == False:
    cmd = input("> ")
    if "stop" in cmd:
        state = True
    else:
        carte_partielle = cmd
        if len(carte_partielle) == 15:
            cle_luhn = luhn_key(carte_partielle)
            print("Le 16ème chiffre de la carte est :" + cle_luhn)
            #4520 5373 4310 550