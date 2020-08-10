file = open('data1.txt', 'a+')

def add_to_list(newText):
    file.write('\n' + newText)
    ask_user()

def ask_user():
    add_to_list(input('Mau nulis apa? '))

ask_user()