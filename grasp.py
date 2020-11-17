import random
import coloração
import math
import copy
import time
import argparse

p1=0.25 #initial solution perturbation
p2=0.25 #neighbor generation perturbation
f1=100  #grasp max iterations
f2=50  #hc max iterations
f3=25   #neighborhood size


def has_no_neighbors_in_color(neighbors, color):
    for n in neighbors:
        for vertex in color:
            if(n==vertex):
                return False
    return True

def sort_by_degree(x):
    sorted_graph = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    return sorted_graph.keys()

def random_swap(e_list):
    idx = range(len(e_list))
    i1,i2 = random.sample(idx,2)
    e_list[i1], e_list[i2] = e_list[i2], e_list[i1]

def find_solution(graph):
    #sort graph by value length
    sorted_by_degree = list(sort_by_degree(graph))

    #generate perturbation in 10% of the element
    perturbate_times = math.floor(len(sorted_by_degree)*p1)
    for i in range(perturbate_times):
        random_swap(sorted_by_degree)

    colors = {}

    for i in sorted_by_degree:

        colored=False
        for color in colors.keys():
            if( has_no_neighbors_in_color(graph[i], colors[color]) ):
                colors[color].append(i)
                colored=True
                break
        if(colored==False):
            colors_size = len(colors)
            colors[colors_size] = [i]

    # print(colors)
    # print(is_solution_valid(graph, colors))
    return colors

def is_solution_valid(graph, colors):
    for color in colors:

        color_set = set(colors[color])

        for vertex in colors[color]:
            neighbor_set = set(graph[vertex])

            if(neighbor_set & color_set):
                return False
    return True

def improved_solution(colors, current_solution):
    if(len(current_solution) > len(colors)):
        return True
    return False

def clear_dict(colors):
    new_dict = {}
    index = 0

    for color in colors.keys():
        if(len(colors[color]) > 0):
            new_dict[index] = colors[color]
            index += 1

    return new_dict

def generate_new_solution(graph, colors):
    n_vertex = len(graph.keys())
    
    randomize_n = math.floor(n_vertex*p2)

    random_vertexes = []

    # get randomize_n elements from colors solution and remove them from colors solution
    for i in range(0,randomize_n) :
        random_color = random.randint(0, len(colors)-1)
        random_color_list = colors[random_color]

        random_vertex = random.randint(0,len(random_color_list)-1)
        random_vertex_value = colors[random_color][random_vertex]

        del colors[random_color][random_vertex]
        colors = clear_dict(colors)


        random_vertexes.append(random_vertex_value)


    random.shuffle(random_vertexes)


    # add elements to solution
    for i in random_vertexes:
        colored=False
        sorted_colors = list(sort_by_degree(colors))

        for color in sorted_colors:
            if( has_no_neighbors_in_color(graph[i], colors[color]) ):
                # print("adicionando " + str(i) + " em " + str(color))
                colors[color].append(i)
                colored=True
                break

        if(colored==False):
            colors_size = len(colors)
            colors[colors_size] = [i]

    return colors

def hill_climbing(graph, colors):
    current_solution = copy.deepcopy(colors)
    j=0

    while(not improved_solution(colors, current_solution) and j<f2):

        neighborhood_size = f3
        for i in range(0,neighborhood_size):

            copy_current_solution = copy.deepcopy(current_solution)

            new_solution = generate_new_solution(graph, copy_current_solution)


            if(improved_solution(new_solution, current_solution)):
                current_solution = copy.deepcopy(new_solution)
        j+=1
        # print(len(current_solution))
        # print(j)

    return current_solution            


def grasp(graph):

    current_solution = {}

    for loop in range(0,f1):

        colors = find_solution(graph)

        if(len(current_solution)==0):
            current_solution=copy.deepcopy(colors)

        current_solution_copy = copy.deepcopy(colors)
        new_solution = hill_climbing(graph, current_solution_copy)

        if(improved_solution(new_solution, current_solution)):
            print("atualizado")
            current_solution = copy.deepcopy(new_solution)

        print("best so far = " + str(len(current_solution)))

    return current_solution

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=False, nargs='*')
    args = parser.parse_args()

    file_input = ""
    if(args.input):
        file_input = args.input[0]

    graph = coloração.get_graph(file_input)

    start_time = time.time()
    colors = grasp(graph)

    print(colors)
    print(is_solution_valid(graph, colors))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()