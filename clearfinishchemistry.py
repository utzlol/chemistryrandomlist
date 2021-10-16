file = open('editelement.json','r')
fileread = file.read()
file.close()

fileread = fileread.replace('}{','},{')
filewrite = open('editelement.json','w+')
b = "{"
c = "}"
filewrite.write(f'{b}     "elements":    [{fileread} ] {c}')
