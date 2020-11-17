
def get_graph(filename):
    

    if(filename==""):
        print("Digite o nome do arquivo")
        filename = input()

    file = open(filename,'r')

    text = file.readlines()

    temp = []

    graph = {}

    vN = int() ## vertex number
    eN = int() ## edge number

    for line in text:
        if line[0] == 'p':
            temp = line.split(' ')
            temp.remove('p')
            temp.remove('edge')
            vN = int(temp[0])
            eN = int(temp[1])
        elif line[0] == 'e':
            temp = line.split(' ')
            temp.remove('e')
            v0 = int(temp[0])
            v1 = int(temp[1])
            if v0 in graph:
                graph[v0].append(v1)
            else:
                graph[v0] = [v1]

            if v1 in graph:
                graph[v1].append(v0)
            else:
                graph[v1] = [v0]
    

    return graph

# print(graph)    