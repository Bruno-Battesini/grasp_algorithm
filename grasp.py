import random
import coloração


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

def find_solution(graph):
    #sort graph by value length
    sorted_by_degree = sort_by_degree(graph)

    #generate perturbation

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

    print(colors)
    print(is_solution_valid(graph, colors))

    return colors

def is_solution_valid(graph, colors):
    for color in colors:

        color_set = set(colors[color])

        for vertex in colors[color]:
            neighbor_set = set(graph[vertex])

            if(neighbor_set & color_set):
                return False
    return True



def main():
    graph = coloração.get_graph()

    find_solution(graph)

if __name__ == "__main__":
    main()