def func(text):
    sum1=0
    sum2=0
    for char in text:
        if char.isupper():
            sum1+=1
        if char.islower():
            sum2+=1
    return sum1,sum2
text=input()
print(func(text))