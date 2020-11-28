param E;                                             #numero de arestas
param V;                                             #numero de vertices
param C;                                             #numero de cores = numero de vertices/pior caso

param edges1 { 1..E };                                    #extremidades das arestas
param edges2 { 1..E };                                    #extremidades das arestas

var y { 1..C } binary;                                    #se a cor h esta na solucao
var x { 1..V, 1..C } binary;                              #se um vertice i recebeu a cor h

minimize obj: sum { h in 1..C } y[h];

subject to R1{i in 1..V}: 
    sum { h in 1..C } x[i,h] = 1;                        #garantir somente uma cor por vertice

subject to R2{i in 1..E, h in 1..C}:
    x[edges1[i],h]+x[edges2[i],h] <= y[h];               #garantir cores distintas para cada par de vertices conectados por uma aresta
