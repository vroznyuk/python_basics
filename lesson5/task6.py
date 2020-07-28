stud_plan = {}

with open('files/task6_in.txt', 'r', encoding='utf8') as f_in:
    for line in f_in:
        tmp_lst = line.split(' ')
        # сумма часов в учебном плане
        sum_hours = 0
        for itm in tmp_lst[1:]:
            if itm and itm.find('-') == -1:
                sum_hours += int(itm[:itm.find('(')])
        stud_plan.update({tmp_lst[0]: sum_hours})

print(stud_plan)