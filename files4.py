import os
sum=0
if __name__ == "__main__":
    file_path = input("Enter the file path: ")
with open(file_path,'r', encoding='utf-8') as file:
            for _ in file:
                    sum+=1
print(sum)