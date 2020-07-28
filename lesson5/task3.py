MIN_SALARY = 20000  # пороговое значение оклада для сравнения
LINE_NUM_START = 3  # порядковый номер строки, с которой начинаются данные

lines_cntr = 0
sum_salary = 0
with open('files/task3_in.txt', 'r', encoding='utf8') as f_in:
    for idx, line in enumerate(f_in):
        lines_cntr = idx + 1
        if lines_cntr >= LINE_NUM_START:
            rec = [word for word in line[:-1].split(' ') if word != '']
            sum_salary += float(rec[1])
            if float(rec[1]) < MIN_SALARY:
                print(f'{rec[0]} имеет оклад {rec[1]}')

print('Средний оклад: ' + str(round(sum_salary/(lines_cntr - LINE_NUM_START + 1), 2)))
