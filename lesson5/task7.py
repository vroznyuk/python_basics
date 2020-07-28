import json
from functools import reduce

companies = {}

with open('files/task7_in.txt', 'r', encoding='utf8') as f_in:
    for line in f_in:
        tmp_lst = line.split(' ')
        companies[tmp_lst[0]] = float(tmp_lst[2]) - float(tmp_lst[3])

companies_with_profit = [val for val in companies.values() if val > 0]
average_profit = round(reduce(lambda x, y: x + y, companies_with_profit) / len(companies_with_profit), 2)
result_list = [companies, {'average_profit': average_profit}]
print(result_list)

with open("files/task7_out.json", "w") as f_out:
    json.dump(result_list, f_out)