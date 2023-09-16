def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = 0
    checksum += sum(odd_digits)
    
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    
    return checksum % 10

def get_luhn_key(card_number):
    return (10 - luhn_checksum(card_number)) % 10

state = False
while not state:
    cmd = input("> ")
    if "stop" in cmd:
        state = True
    else:
        cb_id = cmd
        cb_idf = int(cb_id)
        luhn_key = get_luhn_key(cb_idf)
        if luhn_key == 0:
            print('Clé de Luhn : ' + str(luhn_key) + ' (Valide)')
        else:
            print('Clé de Luhn : ' + str(luhn_key) + ' (Non valide)')
