# MASContactCalculator
Calculate molecular properties from a dcd file.

## Setup

```
cd MASContactCalculator
pip install -e .
```
Currently only requiring numpy for array usage.

## Example Usage

Note: These instructions are made available 
### Setting up the DCD Reader
Instantiate DCDReader object with the trajectory filename. Will read in header frame.<br/> 
```
dcd = DCDReader("trajectory.dcd")
```

### Using the DCD Reader to read from file

Create an array of empty **Frame** objects. Each **Frame** stores the atomic coordinates of the system at one timestep. For each frame in the trajectory, we will use the `read_DCD_Frame()` function to read the next timestep in. <br/>
```
frames = np.empty(len(dcd), dtype=object)
for frameNum in range(options["nRead"]):
  frames[frameNum] = dcd.read_DCD_Frame()
```

##

## To-Do List
- A `Selection` class: Allow the user to subselect atoms in a frame.
- One class per type of calculation i.e distance calculations should be stored in a `Distance` class w/ static methods to compute properties on a frame.
- Better documentation
- Unit tests? How do you unit test io functions??
