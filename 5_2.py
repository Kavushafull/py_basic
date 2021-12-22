txt_file = open("5_2.txt", "w", encoding="cp1251")
text_list =['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n']
txt_file.writelines(text_list)
txt_file.close()

txt_file = open("5_2.txt", "a", encoding="cp1251")
txt_file.write(input()+'\n')
txt_file.write(input()+'\n')
txt_file.close()

txt_file = open("5_2.txt", "r", encoding="cp1251")
list_1 = txt_file.readlines()
print('Строк ', len(list_1))
for x in list_1:
    print(len(x.split(' ')))