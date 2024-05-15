import numpy as np

class Frame:

    def __init__(self, coords):
        self.coords = coords
    
    def get_selection(self, sel):
        return Frame(self.coords[sel])
        
    def __getitem__(self, item):
         return self.coords[item]
        
    def __len__(self):
        return len(self.coords)

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
            
    def compute_distance_matrix(FrameSel1, FrameSel2):
        distance_matrix = np.zeros((len(FrameSel1),len(FrameSel2)))
        for i in range(len(FrameSel1)):
            for j in range(len(FrameSel2)):
                distance_matrix[i,j] = Frame.compute_distance(FrameSel1[i], FrameSel2[j])
                
        return distance_matrix
    def output_distance_matrix(matrix, outstr):
        with open(outstr, "a") as f:
            np.savetxt(f, matrix)
            f.write("\n")
       
