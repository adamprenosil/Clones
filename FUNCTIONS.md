# Functions Template

This is a tutorial of how to provide a set of functions that serve as the generator of a clone. 

Each set of functions must be in one file. 

## Format of the files

Line comments must be start with "#". Empty lines are ignored. Example:

```
# This file contains the evil model
```

### Universe of model

The first line should contain each element of universe separated by a space. Example:

```
0 1 2
```

### Operations

A operation should start with a declaration line with the name and arity separated by one space. Next lines sould be one for each tuple in the relation containing a tuple for the graph relation of the operation separated by a space. Example:

```
+ 2
0 0 0
0 1 1
0 2 2
1 0 1
1 1 2
1 2 0
2 0 2
2 1 0
2 2 1
```

*It must contain exactly the same number of tuples for all the domain of the operation*

A constant should be treated as a constant function of arity 1. Example:

```
Zero 1
0 0
1 0
2 0
```
