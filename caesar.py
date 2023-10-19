# Shuban Pal 2023

class caesar:
  def __init__(self, key, text):
    self.key = key
    self.text = text
  def encrypt(enc):
    ct=""
    for i in range(0,len(enc.text)):
      char = enc.text[i]
      if char.isalpha():
        shift = 97 if char.islower() else 65
        ct+=chr((ord(char) - shift + enc.key)%26 + shift)
      else:
        ct += char
    return ct
  
  def decrypt(dec):
    pt=""
    for i in range(0,len(dec.text)):
      char = dec.text[i]
      shift = 97 if char.islower() else 65
      dec.text+=chr((ord(char) - shift - dec.key)%26 + shift)
    else:
      pt += char
    return pt

mycipher = caesar(3,"Hello World")
print(mycipher.encrypt())
