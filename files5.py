file_path = input("Enter the file path: ")
data_list = input().split(',')

with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(f"{item}\n" for item in data_list)