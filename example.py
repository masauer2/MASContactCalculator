from contacts import *
import time
import sys

def main(arg1, arg2, arg3, arg4): 
    sel1 = np.arange(0,50,1)
    sel2 = np.arange(50,150,1)

    options = {
        "topology": str(arg1),
        "trajectory": str(arg2),
        "skipFrames": int(arg3),
        "grp1": sel1,
        "grp2": sel2,
        "outFile": str(arg4)
    }

    start = time.time()

    dcd = DCDReader("data/practice.dcd", 1000, np.arange(0,50,1), np.arange(50,150,1))

    # Read in header - record number of frames and number of atoms
    nFrames, nAtoms = dcd.read_DCD_Header(dcd.file)
    print(f"Read in DCD header for trajectory with {nFrames} frames and {nAtoms} atoms.")
    # Store coordinates to compute contact distances
    coords = np.zeros((nAtoms, 3))

    # Numpy array to store inverse contact distances
    distance_matrix = np.zeros((int(nFrames/dcd.analysisFrame)+1, len(dcd.sel1), len(dcd.sel2)))

    # For each frame
    for j in range(nFrames):
    # Read in the coordinates
        coords = dcd.read_DCD_Frame(dcd.file, j, nAtoms)

        # For each pair of residues 
        if(j % dcd.analysisFrame == 0):
            print("Compute distance matrix for frame %d" % int(j/dcd.analysisFrame))
            for s1 in range(len(dcd.sel1)):
                for s2 in range(len(dcd.sel2)):
                    # Compute the inverse contact distance
                    distance_matrix[int(nFrames/dcd.analysisFrame),s1,s2] = dcd.compute_inverse_distance(coords[dcd.sel1[s1]],coords[dcd.sel2[s2]])
        end = time.time()
    print(f"{end - start} seconds to read")
    DCDReader.output_distance_matrix(distance_matrix, "matrix.out")

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
