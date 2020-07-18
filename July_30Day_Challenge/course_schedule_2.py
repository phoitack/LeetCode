''' 
Not sure how to do this since this is part of Graph Theory
Algorithms
'''

def findOrder(numCourses, prerequisites):

    import itertools

    if not prerequisites:
        #flat_list = [item for sublist in prerequisites for item in sublist]
        return(list(range(numCourses)))
        #return (sorted(list(set(flat_list))))
    else:
        flat_list = [item for sublist in prerequisites for item in sublist]

        flat_list = sorted(list(set(flat_list)))

        #flat_list = set(list(itertools.combinations(flat_list,numCourses)))

        #return (sorted(list(set(flat_list))))
        return (flat_list)
    
    
    
n = 4
prereq = [[1, 0], [2, 0], [3, 1], [3, 2]]

#n = 2
#prereq = []

print(findOrder(n, prereq))