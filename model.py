def choose():
    x = input('Введите имя или телефон  ')
    with open('HomeWorkPython7/file.csv', 'r', encoding='utf-8') as f:
        lst = f.readlines()
       
    lst = list(map(lambda x: x[:-1], lst))
    key = False
        
    for i in lst:
        key = i.find(x) != -1
        if key == True:                      
            print(i)
            quit()
    print('Абонент не существует!')