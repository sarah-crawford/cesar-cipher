alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  enc_letters = []
  # 1. Go through text and collect indexes from alphabet
  for character in text:
    new_position = alphabet.index(character) + shift
    if new_position > 25:
      new_position = (new_position - 25) - 1
        
    new_character = alphabet[new_position]

    enc_letters.append(new_character)
    
  encrypted_text = ''.join(enc_letters)
  print(f"The encoded text is: {encrypted_text}")

def decrypt(text, shift):
  dec_letters = []
  for character in text:
    original_position = alphabet.index(character) - shift

    original_character = alphabet[original_position]

    dec_letters.append(original_character)

  decoded_text = ''.join(dec_letters)
  print(f"The decoded text is: {decoded_text}")


if direction == 'encode':
  encrypt(text, shift)
else:
  decrypt(text, shift)
 
