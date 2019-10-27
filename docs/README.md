# Feasibility-Pump 

[![Build Status](https://travis-ci.com/FilippoRanza/Feasibility-Pump.svg?branch=master)](https://travis-ci.com/FilippoRanza/Feasibility-Pump)

Feasibility Pump - find feasible solution for a Binary Programming
problem. 

## Rationale

The Feasibility Pump(FP) is a heuristic useful to find a feasible solution 
to Mixed Integer Programming problem. This implementation is specifically designed to work with Binary Programming problems. FP is not defined to 
find optimal solution nor a good one, it's only purpose is to find
a  feasible solution in a small amount of time, even for those problem 
where a greedy algorithm cannot produce feasible result.  

For a more detailed explanation please read [the original paper](http://www.dei.unipd.it/~fisch/papers/feasibility_pump.pdf)

## Usage
This project can be use as a stand alone application or
as a library.

### Stand Alone
In order to find a feasible solution to a given 01MIP instance 
simply run
```
    fp.py -i instance
```

the extension of the instance file will drive the back-end library to 
use the correct loader. 

Available loaders can be obtained using:
```
    fp.py -l
```

For more information about the usage you can:
```
    fp.py -h
```

Read this docs to get more information about the currently know file formats:
* [json](json_file.md)

### Library
this feature is not implemented at the current stage
