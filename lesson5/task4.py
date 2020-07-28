digits = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('files/task4_in.txt', 'r', encoding='utf8') as f_in:
    with open('files/task4_out.txt', 'w', encoding='utf8') as f_out:
        for line_in in f_in:
            line_out = line_in.replace(line_in.split(' ', 1)[0], digits.get(line_in.split(' ', 1)[0]))
            f_out.write(line_out)