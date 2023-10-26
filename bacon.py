# By: Shuban Pal
# Algorithm: Bacon Cipher
# Project: CSP Passion Project
# Date: 2023
class bacon:
  def __init__(self, text):
    self.text = text
  def encrypt(enc):
    dex = {
      "A": "AAAAA",
      "B": "AAAAB",
      "C": "AAABA",
      "D": "AAABB",
      "E": "AABAA",
      "F": "AABAB",
      "G": "AABBA",
      "H": "AABBB",
      "I": "ABAAA",
      "J": "ABAAB",
      "K": "ABABA",
      "L": "ABABB",
      "M": "ABBAA",
      "N": "ABBAB",
      "O": "ABBBA",
      "P": "ABBBB",
      "Q": "BAAAA",
      "R": "BAAAB",
      "S": "BAABA",
      "T": "BAABB",
      "U": "BAABB",
      "V": "BAABB",
      "W": "BABAA",
      "X": "BABAB",
      "Y": "BABBA",
      "Z": "BABBB",
    }
    ptparse = []
    ct = ""
    for i in range(0,len(enc.text)):
      if int(ord(enc.text[i])) != 32:
        ptparse.append(enc.text[i].upper())
    for j in range(0,len(ptparse)):
      ct += dex[ptparse[j]]
      ct += " "
    return ct


  def decrypt(dec):
    inverted_dex = {
      "AAAAA": "A",
      "AAAAB": "B",
      "AAABA": "C",
      "AAABB": "D",
      "AABAA": "E",
      "AABAB": "F",
      "AABBA": "G",
      "AABBB": "H",
      "ABAAA": "I",
      "ABAAB": "J",
      "ABABA": "K",
      "ABABB": "L",
      "ABBAA": "M",
      "ABBAB": "N",
      "ABBBA": "O",
      "ABBBB": "P",
      "BAAAA": "Q",
      "BAAAB": "R",
      "BAABA": "S",
      "BAABB": "T",
      "BABAA": "W",
      "BABAB": "X",
      "BABBA": "Y",
      "BABBB": "Z"
    }

    ctparse = dec.text.split(" ")
    pt = ""
    for i in range(0,len(ctparse)):
      pt += inverted_dex[ctparse[i]]
    return pt


mycipher = bacon("Hello World") 
print(mycipher.encrypt())
cipher2 = bacon("AABBB AABAA ABABB ABABB ABBBA BABAA ABBBA BAAAB ABABB AAABB")
print(cipher2.decrypt())
