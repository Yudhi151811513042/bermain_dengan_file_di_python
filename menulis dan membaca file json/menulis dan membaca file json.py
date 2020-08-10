import json

"""data = {}
data['member'] = [
    {'name': 'JetLee', 'skill': 'nafas naga'},
    {'name': 'Yip', 'skill': 'tendangan beruang'},
    {'name': 'Superwoman', 'skill': 'cakar emas'}
]
"""
with open('member.txt', 'r') as memberfile:
    data= json.load (memberfile)

    for member in data['member']:
        print('namanya adalah ' + member['name '] + ' punya skill ' + member['skill'])