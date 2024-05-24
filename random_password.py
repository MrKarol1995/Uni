import random
import string

def generate_pass(length):

    """Generowanie hasła długości length składającego się z wygenerowanych losowo liter cyfr i znaków specjalnych"""
    if length < 0:
        print("nie mo")
    else:
        chars = string.digits + string.punctuation + string.ascii_letters
        lista = []
        password = ''.join(random.choice(chars) for _ in range(length-3)) + \
                   random.choice(string.digits) + \
                   random.choice(string.punctuation) + \
                   random.choice(string.ascii_letters)
        lista.extend(password)
        random.shuffle(lista)
        return password, lista

def generate_column(stri):
    a, op, b = stri.split()
    a, b = int(a), int(b)
    if b == 0:
        quit("nie mo")
    if op == '+':
        result = a+b
        max_length = max(len(str(a)), len(str(b)), len(str(result)), len(op) + 1)
        format_str = '{:>' + str(max_length) + '}'
        column = ' ' + format_str.format(a) + ' \n'
        column += op + format_str.format(b) + ' \n'
        alfa = max_length
        column += '-' * (alfa + 1) + ' \n'
        column += ' ' + format_str.format(result)
        return column
    elif op == '*':
        result = a*b
        max_length = max(len(str(a)), len(str(b)), len(str(result)), len(op)+1)
        format_str = '{:>' + str(max_length) + '}'
        column = ' ' + format_str.format(a) + ' \n'
        column += op + format_str.format(b) + ' \n'
        alfa = max_length
        column += '-' * (alfa+1) + ' \n'
        column += ' ' + format_str.format(result)
        return column
    elif op == '-':
        result = a - b
        max_length = max(len(str(a)), len(str(b)), len(str(result)), len(op) + 1)
        format_str = '{:>' + str(max_length) + '}'
        column = ' ' + format_str.format(a) + ' \n'
        column += op + format_str.format(b) + ' \n'
        alfa = max_length
        column += '-' * (alfa + 1) + ' \n'
        column += ' ' + format_str.format(result)
        return column
    elif op == '/':
        result = a / b
        max_length = max(len(str(a)), len(str(b)), len(str(result)), len(op) + 1)
        format_str = '{:>' + str(max_length) + '}'
        column = ' ' + format_str.format(a) + ' \n'
        column += op + format_str.format(b) + ' \n'
        alfa = max_length
        column += '-' * (alfa + 1) + ' \n'
        column += ' ' + format_str.format(result)
        return column
    else:
        return "złe wprowadenie znaku"
