txt_file = open("5_4_a.txt", "w", encoding="cp1251")
text_list = ['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n']
txt_file.writelines(text_list)
txt_file.close()

list_a = []
list_b = ['Один', 'Два', 'Три', 'Четыре']
i = 0
txt_file = open("5_4_a.txt", "r", encoding="cp1251")
translate = txt_file.readlines()
for x in translate:
    translate_list = x.split(' ')
    translate_list[0] = list_b[i]
    list_a.append(' '.join(translate_list))
    i += 1
txt_file.close()

txt_file = open("5_4_b.txt", "w", encoding="cp1251")
txt_file.writelines(list_a)
txt_file.close()
