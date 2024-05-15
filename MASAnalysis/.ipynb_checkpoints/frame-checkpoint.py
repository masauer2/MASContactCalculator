import numpy as np

class Frame:

    def __init__(self, coords):
        self.coords = coords
    
    def get_selection(self, sel):
        return self.coords[sel]
        
    def __getitem__(self, item):
         return self.coords[item]
        
    def compute_distance(coord1, coord2):
        return np.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2 + (coord1[2]-coord2[2])**2)

    def compute_inverse_distance(coord1, coord2):
        if coord1 == None or coord2 == None:
            raise Exception("Distance calculator requires two coordinates.")
        tmp = Frame.compute_distance(coord1, coord2)
        if tmp != 0:
            return 1/tmp
        else:
            return -1
            
    def compute_distance_matrix(coordset1, coordset2):
        distance_matrix = np.zeros((len(coordset1),len(coordset2)))
        for i in range(len(coordset1)):
            for j in range(len(coordset2)):
                distance_matrix[i,j] = Frame.compute_distance(coordset1[i], coordset2[j])
                
        return distance_matrix
    def output_distance_matrix(matrix, outstr):
        with open(outstr, "a") as f:
            np.savetxt(f, matrix)
            f.write("\n")
       