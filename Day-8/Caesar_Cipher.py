from art import logo
print(logo)

# Letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encryptions and Decryptions Function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # Decoding
  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      # Encoding 
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

wanna_try = True
while wanna_try:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if result == "no":
    wanna_try = False
    print("GoodBye!!")

# End of the Function 