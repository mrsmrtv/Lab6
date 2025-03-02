import string

for letter in string.ascii_uppercase:
    with open("{letter}.txt", 'w', encoding='utf-8') as file:
        file.write("Yo")