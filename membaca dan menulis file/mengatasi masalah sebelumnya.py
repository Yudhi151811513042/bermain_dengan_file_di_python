file = open('data.txt', 'a+')
file.write('\n new life!!')

file.seek(0)

text = file.read()
print(text)

