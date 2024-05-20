text = input('print text:\n').strip()
shift = 15

def caesar_encrypt(plaintext, shift, direction=1):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  final_text = ''

  for char in plaintext.lower():
    if not char.isalpha(): 
      final_text += char # if character is not alphabetic add it to final_text
    else:
      char_index = alphabet.index(char) # find the index of a given character in the alphabet
      new_index = char_index + shift * direction # find new index according to shift
      new_char = alphabet[(new_index) % len(alphabet)] # find new character in the alphabet
      final_text += new_char

  return final_text

encrypt_decrypt = caesar_encrypt(text, shift) # add -1 as 3-rd argument to decrypt 
print('final text:')
print(encrypt_decrypt)
