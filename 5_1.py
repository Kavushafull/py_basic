txt_file = open("5_1.txt", "w", encoding="cp1251")
text_list = []
while True:
    text = input()
    if text != '':
        text_list.append(text + '\n')
    else:
        break
txt_file.writelines(text_list)
txt_file.close()
