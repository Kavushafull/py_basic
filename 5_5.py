txt_file = open("5_5.txt", "w", encoding="cp1251")
txt_file.writelines(input())
txt_file.close()

txt_file = open("5_5.txt", "r", encoding="cp1251")
numbers = txt_file.read()
text_list = numbers.split(' ')
i = 0
for x in text_list:
    text_list[i] = int(x)
    i += 1
print(sum(text_list))
txt_file.close()