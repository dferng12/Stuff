amount = int(input('Enter ROT value: '))

if amount > 25 or amount < 1 or type(amount) is not int:
    print('Amount must be less than 26 and bigger than 0')
    exit(-1)

to_convert = input('Enter text: ')
direction = int(input('Forward (1) or backward(2)?: '))

if not (direction == 1 or direction == 2):
    print('Direction value not valid')
    exit(-1)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
output = ''

for letter in to_convert:
    if letter.lower() in alphabet:
        rotation = alphabet.index(letter.lower()) + amount if direction == 1 else alphabet.index(letter.lower()) - amount

        if letter.isupper():
            output += alphabet[rotation % len(alphabet)].upper()
        else:
            output += alphabet[rotation % len(alphabet)]
    else:
        output += letter

print('\nRESULT:', output)
