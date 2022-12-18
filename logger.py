def log(x):
    with open('HomeWorkPython7/file.txt', 'a', encoding='utf-8') as f:
        f.write(f'{x}\n')
    with open('HomeWorkPython7/file.csv', 'a', encoding='utf-8') as f:
        f.write(f'{x}\n')
