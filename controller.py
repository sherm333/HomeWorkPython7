from logger import log
from model import choose
from view import choose_mod

def run():
    if choose_mod() == 0:
        choose()
    else:
        log(input('Введите имя и телефон  '))