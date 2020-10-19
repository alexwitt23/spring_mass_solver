# Spring-Mass System Solver

This project was written for Project #1 in COE 352 taught by Dr. Trahan.

The goal is a python script which allows the user to enter a certain type of spring-mass
system to be solved.

## Setup
The only requirement for the python code is `numpy`:
```
python3 -m pip install numpy
```

## Usage
To see the full range of arguments on the python script, run:
```
python/main.py --h
```

An example system with a fixed top and 5 springs and 5 masses:
```
python/main.py \
    --fix_top \
    --masses "1.5,2.4,3.3,4.2,5.1" \
    --spring_constants "5.5,4.4,3.3,2.2,1.1"
```