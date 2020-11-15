print("Digite o nome do arquivo")
fileName = input()

file = open('r', fileName)

text = file.read()

temp = str()

graph = {}

vN = int()
eN = int()

for line in text:
    if line[0] == 'p':
        temp = line.split(' ')
        temp = temp.remove('p')
        temp = temp.remove("edge")
        vN = int(temp[0])
        eN = int(temp[1])
    elif line[0] == 'e':
        temp = line.split(' ')
        temp = temp.remove('e')
        v0 = int(temp[0])
        v1 = int(temp[1])
        graph[v0] = v1
