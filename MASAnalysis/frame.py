import numpy as np

class Frame:
    """
    A Frame object contains coordinates of a single timestep of an MD simulation.

    Keyword arguments:
    coords -- array of size N*3 to store atomic coordinates (N = number of atoms)
    """
    def __init__(self, coords):
        self.coords = coords
    
    # Select only certain atoms of a Frame 
    # Re-implement w/ selection class
    def get_selection(self, sel):
        return Frame(self.coords[sel])
        
    def __getitem__(self, item):
         return self.coords[item]
        
    def __len__(self):
        return len(self.coords)

    # Distance functions
    @staticmethod
    def compute_distance(coord1, coord2):
        """Compute distance between positions of two atoms."""
        if len(coord1) != 3 or len(coord2) != 3:
            raise Exception("Distance calculator requires 2 arrays of length 3.")
        return np.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2 + (coord1[2]-coord2[2])**2)

    @staticmethod
    def compute_inverse_distance(coord1, coord2):
        """Compute inverse distance between positions of two atoms."""
        if coord1 == None or coord2 == None:
            raise Exception("Distance calculator requires two coordinates.")
        tmp = Frame.compute_distance(coord1, coord2)
        if tmp != 0:
            return 1/tmp
        else:
            return -1

    @staticmethod    
    def compute_distance_matrix(FrameSel1, FrameSel2):
        """Compute distance matrix between all atoms in Frame objects"""
        distance_matrix = np.zeros((len(FrameSel1),len(FrameSel2)))
        for i in range(len(FrameSel1)):
            for j in range(len(FrameSel2)):
                distance_matrix[i,j] = Frame.compute_distance(FrameSel1[i], FrameSel2[j])
        return distance_matrix

    # If file exists - no append

    @staticmethod
    def output_distance_matrix(matrix, outstr):
        """Output distance matrix"""
        with open(outstr, "a") as f:
            np.savetxt(f, matrix)
            f.write("\n")
       
