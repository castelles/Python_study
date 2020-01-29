myfile = open('test.txt')
contents = myfile.read()
myfile.readlines()
myfile.seek(0)
myfile.close()

# Não precisa fechar o arquivo
with open('test.txt') as my_new_file:
    contents = my_new_file.read()

#r ler
#w escrever sobrescrevendo o antigo arquivo
#a adiciona ao final do arquivo
#r+ ler e escrever
#w+ escrever e ler sobrescrevendo
with open('test.txt',mode='r') as myfile:
    contents = myfile.read()

