lines_cntr = 0  # счетчик строк
with open('files/task2_in.txt', 'r', encoding='utf8') as f_in:
    for idx, line in enumerate(f_in):
        lines_cntr = idx + 1
        print('Слов в ' + str(idx + 1) + ' строке: ' + str(len([word for word in line.split(' ') if word != ''])))
    print('Всего ' + str(lines_cntr) + ' строк в файле')
