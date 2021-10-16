file = open('elementsdatabase.json','r')
fileread = file.read()
file.close()

fileread = fileread.replace('}{','},{')
filewrite = open('elementsdatabase.json','w+')
b = "{"
c = "}"
filewrite.write(f'{b}     "elements":    [{fileread} ] {c}')
