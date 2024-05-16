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

` dcd = DCDReader("trajectory.dcd") `
## To-Do List
- A `Selection` class: Allow the user to subselect atoms in a frame.
- One class per type of calculation i.e distance calculations should be stored in a `Distance` class w/ static methods to compute properties on a frame.
- Better documentation
- Unit tests? How do you unit test io functions??
