# Deutsch-Josza Algorithm

## Problem 
Consider a black box which takes an `n` bit binary string and 
outputs a single binary bit. The black box is said to be
balanced if it outputs a 1 exactly half of the times and a 0
otherwise. Otherwise if the black box always outputs only a 0 (or only a 1) 
for every input it is said to be constant. We can assume that the black box is 
either constant or balanced (but cannot be something in between) [CHECK TRUE!].
Our requirement is to determine if the black box is constant or balanced.

## Classical Solution
We have the following solution on a classical computer.
Let us check if the black box is balanced.
Then we need to check upto half (+1) of the `n` bit inputs if they all 
output the same value. In other words the algorithm will 
run in $2^(n-1)+1$ executions. If any value is not the same as the previous, 
then we know that it is balanced; otherwise it must be constant (since we assumed 
the black box is either balanced or constant).

Note it is slightly faster to check if the black box is balanced since if we try to check
if it is constant, then we must check all possible `n` bit srings in the worst 
case scenario, however for the balanced case we just need to 
check half+1 of all possible `n` bit strings. 

## Add-ons
- Use streams (to pass some amount of data into it)
- Use threads (to parallel process)
- Can I use machine learning? Clustering problem
- Can I add a stopper/timer... so can stop algorithm 
and it outputs a probability for it being balanced or constant?
- Generate all possible `n` bit inputs. Generate sample of `n` bit inputs....using pseudo random number generator? Or a QRNG? To test a sample.
Use TDD?

## Classical Tests
- read what is the best python test suite, or use something you've used before.

- Generate some black boxes. (start with rudimentary 2 bit case)
- Test different sizes of `n`

To test edge cases we check:
- the output is a 1 bit string
- the inputs are all `n` bits
- if any inputs are missing
- the output and input are strings and binary strings
- the black box is indeed balanced or constant (not something in between)

## Quantum Solution
- Write and run on some different quantum computers?

## Run the Classical program
Requires python3 and git installation.

Run the following commands.
```
git pull
python3 -m venv venv
source venv/bin/activate  # to activate the virtual environment
pip install requirements.txt
```

To deactivate the virtual environment on completion
```

```

## Run the Quantum solution

## Run the tests
run tests with command: 
```python -m unittest tests```



## TO DOS
- check structure
- follow PEP guidelines
    - make into object oriented program?
    - add comments?
- add typing
- compare structure to popular python libraries
- turn into zip file