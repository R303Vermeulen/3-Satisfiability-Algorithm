import sys
import graph
import vertex_cover as vc

def formatInput(inList):
    cuttheenter = len(inList[0]) - 1
    inString = inList[0][:cuttheenter]
    splitStrings = inString.split(" & ")
    clauseList = []

    for sting in splitStrings:
        splitsting = sting.split(" | ")
        dumlen = len(splitsting[2])
        plause = [splitsting[0][2:], splitsting[1], splitsting[2][:dumlen - 2]]

        clause = []
        cidx = len(clauseList)
        for i in range(3):
            elem = plause[i]
            if (len(elem) == 1):
                clause.append((elem, cidx, 0, i))
            if (len(elem) == 2):
                clause.append((elem[1], cidx, 1, i))


        clauseList.append(clause)

    return clauseList

def threeSatFunc(clauses):
    G = frime(clauses)
    clique = cliqueFunc(G, clauses)
    if clique is None:
        return None
    a = hprime(clique)
    return a

def cliqueFunc(gaph, clauses):
    k = len(clauses)
    comp = f(gaph, clauses)
    cover = vc.vertex_cover(comp, 2*k)
    if cover is None:
        return None
    clique = h(cover, gaph)
    return clique

def frime(clauses):
    g = graph.Graph([])
    for clause in clauses:
        for v in clause:
            graph.add_vertex(g, v)

    for clause1 in clauses:
        for v1 in clause1:
            for clause2 in clauses:
                for v2 in clause2:
                    if ( v1[1] != v2[1]):
                        if ( v1[0] != v2[0]):
                            graph.add_edge(g, v1, v2)
                        elif ( v1[2] == v2[2]):
                            graph.add_edge(g, v1, v2)

    return g

def f(gaph, clauses):
    if (len(gaph.matrix) == 0):
        return None

    comp = graph.Graph([])
    for clause1 in clauses:
        for v1 in clause1:
            edges = gaph.matrix[v1]
            for clause2 in clauses:
                for v2 in clause2:
                    if v2 != v1 and (v2 not in edges):
                        graph.add_edge(comp, v1, v2)
    return comp

def h(cover, gaph):
    for vert in cover:
        graph.remove_vertex(gaph, vert)
    return gaph

def hprime(clique):
    clique = sorted(clique)
    a = []
    for vert in clique:
        stin = ""
        if vert[2] == 1:
            stin += "~"
        stin += vert[0]
        if stin not in a:
            a.append(stin)
    return a

if __name__ == "__main__":
    inFile = open(sys.argv[1])
    inList = inFile.readlines()
    clauses = formatInput(inList)
    assignment = threeSatFunc(clauses)
    if (assignment is None) or (len(assignment) == 0):
        print("No satisfying assignments.")
    else:
        print("Satisfying assignment:")
        retstin = ""
        retstin += assignment[0]
        i = 1
        while i < len(assignment):
            retstin += ", "
            retstin += assignment[i]
            i += 1
        print(retstin)




