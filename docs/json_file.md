# JSON Format

The user can specify the instance as a JSON file. Although JSON is not 
the most common way to describe a MIP, it has some serious advantages. In fact
it is very easy to parse it and it is trivial to write a JSON file.


## Example File

```json
{
    "min" : [1, 1],
    "constrs":[
        {"eq": [1, 1], "ge": 1},
        {"eq": [5, 10], "ge": 5},
        {"eq": [11, 5], "le": 11},
        {"eq": [11, 2], "le": 11}
    ]
}
```

This file describe the problem:

Minimize 
- *x + y*

Subject to 
- *x + y >= 1*
- *5x + 10y >= 5* 
- *11x + 5y <= 11*
- *11x + 2y <= 11* 


## Format

The file must describe the *objective function* and the *constraints*

### Objective Function
This token describes the objective function. 

| KEY | VALUE | MEANING|
|-----|-------|--------|
| *min* | list of *n* numbers| minimize this linear objective function |
| *max* | list of *n* numbers| minimize this linear objective function |

Only one objective function is allowed inside an instance. Only one 
optimization direction is allowed.


### Constraints
This token describes the constraints of the given problem.
This token uses *constrs* as key, the value is a list of JSON object. Each object in 
this list describe a linear constraint. Constraints can be *less or equal then* or *greater or equal then*.

| KEY | VALUE | MEANING|
|-----|-------|--------|
| *eq* | list of *n* numbers| constraint linear expression - mandatory |
| *ge* | a number | constrains the *eq* linear expression to be greater or equal then its value |
| *le* | a number | constrains the *eq* linear expression to be less or equal then its value |

A constraint object can contain only one of *ge*, *le*.
