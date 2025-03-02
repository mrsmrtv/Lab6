s1 = input()
s2 = input()

with open(s1, 'r', encoding='utf-8') as ctrlc, open(s2, 'w', encoding='utf-8') as ctrlv:
    ctrlv.write(ctrlc.read())