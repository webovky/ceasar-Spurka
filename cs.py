

shift = 3 

text=input("Zadej text: ") 

prazdny_text = ""

for c in text:

    if c.isupper():

        c_cod = ord(c)

        c_index = ord(c) - ord("A")

        novy_index = (c_index - shift) % 26

        novy_cod = novy_index + ord("A")

        nove_pismeno = chr(novy_cod)

        prazdny_text = prazdny_text + nove_pismeno

    else:

        prazdny_text += c

print("Encrypted text:",text)

print("Decrypted text:",prazdny_text)