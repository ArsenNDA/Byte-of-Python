poem = '''
Programming its Fine
If your work is boring
for make hes best tone 
use a python
yoooo yooo yooo'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()