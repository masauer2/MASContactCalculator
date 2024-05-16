from MASAnalysis import *
import time
import sys

def main(arg1, arg2, arg3): 
    
    sel1 = np.arange(0,253,1)
    sel2 = np.arange(0,253,1)

    options = {
        "trajectory": str(arg1),
        "skipFrames": 1,
        "nRead": int(arg2),
        "outFile": str(arg3)
    }

    start = time.time()

    # Open a DCD file and store the number of frames in var
    dcd = DCDReader(options["trajectory"])
    print(f"Read in DCD header for trajectory with {dcd.nFrames} frames and {dcd.nAtoms} atoms.")
    frames = np.empty(len(dcd), dtype=object)

    # For each frame in the trajectory, read in the coordinates from the dcd file.
    # Compute the distance between two groups of atoms in the trajectory.
    for frameNum in range(options["nRead"]):
        frames[frameNum] = dcd.read_DCD_Frame()
        if(frameNum % options["skipFrames"] == 0):
            print("Compute distance matrix for frame %d" % int(frameNum/options["skipFrames"]))
            distance_matrix = Frame.compute_distance_matrix(frames[frameNum].get_selection(sel1), frames[frameNum].get_selection(sel2))
            Frame.output_distance_matrix(distance_matrix, options["outFile"])
    
    end = time.time()
    print(f"{end - start} seconds to read")

if __name__ == "__main__":
    trajectory = "R1.dcd"
    nRead = 5
    outfile = "frommas.out"
    main(trajectory, nRead, outfile)
