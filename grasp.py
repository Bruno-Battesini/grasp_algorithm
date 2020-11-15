import random
import coloração
import math

# def random_generator(seed, lower_bound, higher_bound):
#     random.seed(seed)
#     return random.randint(lower_bound, higher_bound)


# def grasp(alpha, iterations):
#     for n in range(iterations):
#         pass

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
    perturbate_times = math.floor(len(sorted_by_degree)*0.1)
    for i in range(perturbate_times):
        random_swap(sorted_by_degree)

    colors = {}

    for i in sorted_by_degree:

        colored=False
        for color in colors.keys():
            if( has_no_neighbors_in_color(graph[i], colors[color]) ):
                colors[color].append(i)
                colored=True
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
    if(len(current_solution) < len(colors)):
        return True
    return False

def generate_new_solution(graph, colors):
    n_vertex = len(graph.keys())
    
    randomize_n = math.floor(n_vertex*0.1)

    random_vertexes = []

    # get randomize_n elements from colors solution and remove them from colors solution
    for i in range(0,randomize_n) :
        random_color = random.randint(0, len(colors)-1)
        random_color_list = colors[random_color]

        random_vertex = random.randint(0,len(random_color_list)-1)
        random_vertex_value = colors[random_color][random_vertex]

        del colors[random_color][random_vertex]
        random_vertexes.append(random_vertex_value)

        # print(random_color, random_vertex, random_vertex_value)

    random.shuffle(random_vertexes)

    # add elements to solution
    for i in random_vertexes:
        colored=False
        for color in colors.keys():
            if( has_no_neighbors_in_color(graph[i], colors[color]) ):
                colors[color].append(i)
                colored=True
        if(colored==False):
            colors_size = len(colors)
            colors[colors_size] = [i]

    return colors

def hill_climbing(graph, colors):
    current_solution = colors

    while(not improved_solution(colors,current_solution)):

        neighborhood_size = 10
        for i in range(0,neighborhood_size):
            new_solution = generate_new_solution(graph, colors)

            if(improved_solution(new_solution, current_solution)):
                current_solution = new_solution

    return current_solution            



def main():
    graph = coloração.get_graph()

    colors = find_solution(graph)

    colors = hill_climbing(graph,colors)

    print(colors)

if __name__ == "__main__":
    main()