import os


def get_graph(fileName):
    # print("Digite o nome do arquivo")
    # fileName = input()

    file = open(fileName,'r')

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

    return graph,vN,eN, fileName

def write_file(graph,v,e, f):
    base = os.path.splitext(f)[0]
    fo = open(base+'.dat', "w+")

    fo.write("data;\n")
    fo.write("param E := " + str(e) + ";\n")
    fo.write("param V := " + str(v) + ";\n")
    fo.write("param C := " + str(v) + ";\n")

    edges1 = ""
    edges2 = ""
    i = 1
    for vertex in graph.keys():
        for neighbor in graph[vertex]:
            edges1 += " " + str(i) + " " + str(vertex)
            edges2 += " " + str(i) + " " + str(neighbor)
            i += 1

    fo.write("param edges1 :="+edges1+";\n")
    fo.write("param edges2 :="+edges2+";\n")

    fo.write("end;\n")
    fo.close()   



def main():

    files = [
                "2-FullIns_3.col",
                "2-FullIns_4.col",
                "4-FullIns_3.col",
                "5-FullIns_3.col",
                "queen5_5.col",
                "queen6_6.col",
                "queen7_7.col",
                "queen9_9.col",
                "queen10_10.col",
                "queen11_11.col"
            ]

    for filename in files:
        graph,v, e, f = get_graph(filename)

        write_file(graph,v,e, f)


if __name__ == "__main__":
    main()