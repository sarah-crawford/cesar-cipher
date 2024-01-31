alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  letters = []
  for character in text:
    if cipher_direction == "encode":
      new_position = alphabet.index(character) + shift
      if new_position > 25:
        new_position = (new_position - 25) - 1

      character = alphabet[new_position]
      
      letters.append(character)
      
    elif direction == "decode":
      original_position = alphabet.index(character) - shift
      original_character = alphabet[original_position]
  
      character = alphabet[original_position]

      letters.append(original_character)

  final_text = ''.join(letters)
  print(f"Here's the {direction}d result: {final_text}")

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
 
