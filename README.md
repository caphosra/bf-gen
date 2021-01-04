# bf-gen (Brainf\*\*k generator)

[![Test](https://github.com/capra314cabra/bf-gen/workflows/Test/badge.svg)](https://github.com/capra314cabra/bf-gen)
[![PyPI](https://img.shields.io/pypi/v/bf-gen)](https://pypi.org/project/bf-gen/)

<p align="center">
    <img width="500px" src="https://raw.githubusercontent.com/capra314cabra/bf-gen/master/img/bf-gen-icon.png" alt="Icon" title="bf-gen icon">
</p>

With this library, you can get Brainf\*\*k source code by just calling functions.  
Why don't we write Brainf**k with your brain clear!

## Features

- Easy to use
- Readable
- Various functions
- Also can be used for Brainf**k-like languages such as Blub, Ook!
- Inspired by LLVM IRBuilder

## Why use this library

Some people think that writing Brainf**k is interesting since it is unreadable and there are no reasons to use this library.  
Actually, **I agree** with this idea.

But there are others who want to learn Brainf**k but don't know how to do.  
I hope this library supports them to drive into crazy as speedily as possible without prejudice.

## Examples

### Hello World

``` python
from bf_gen import BFBuilder

builder = BFBuilder() # Initialize Brainf**k builder

builder.init_with_letter('H') # Fill current cell by 'H'
builder.output()              # Print a value of current cell
builder.init_with_letter('e') # Fill current cell by 'e'
builder.output()              # Print a value of current cell
builder.init_with_letter('l') # Fill current ...
builder.output()              # Print a value ...
builder.init_with_letter('l') # Fill ...
builder.output()              # Print ...
....

bf_source = builder.generate() # Get Brainf**k code
```

Of course, it is far from smart.  
This is one of good examples for showing "Hello World":

``` python
from bf_gen import BFBuilder

builder = BFBuilder() # Initialize Brainf**k builder

for letter in 'Hello World':
    builder.init_with_letter(letter) # Fill current cell by letter given
    builder.output()                 # Print a value of current cell

bf_source = builder.generate() # Get Brainf**k code
```

### Triangle

``` python
from bf_gen import BFBuilder

builder = BFBuilder() # Initialize Brainf**k builder
triangle_size = 5

#
# <Memory layout>
#
# [ ][ ][ ][ ]
#
# 0: Descending counter
# 1: Ascending counter
# 2: Symbol counter
# 3: Temporary value
#

DESCENDING = 0
ASCENDING = 1
SYMBOL = 2
TEMP = 3

builder.move(DESCENDING)             # Move to cell 0
builder.init_with_num(triangle_size) # Initialize cell 0 with the size of triangle

with builder.loop():
    builder.add(-1) # Decrement cell 0

    builder.move(TEMP)       # Move to cell 3
    builder.init_with_zero() # Initialize cell 3

    builder.move(ASCENDING)    # Move to cell 1
    builder.add(1)             # Increment cell 1
    builder.copy(SYMBOL, TEMP) # Copy a value of ascenfing counter to symbol counter

    builder.move(SYMBOL) # Move to cell 2

    with builder.loop():
        builder.add(-1) # Decrement cell 2

        builder.move(TEMP)            # Move to cell 3
        builder.init_with_letter('#') # Initialize cell 3 with "#"
        builder.output()              # Print "#"

    builder.move(TEMP)             # Move to cell 3
    builder.init_with_letter('\n') # Initialize cell 3 with new line character
    builder.output()               # Print new line character

bf_source = builder.generate() # Get Brainf**k code
```

After executing Brainf**k code, you will see following:

```
#
##
###
####
#####

```

Wow! Beatiful!

## Installation

I recommend you to install from PyPI.

```bash
$ pip install bf-gen
```

## License

This library is released under [MIT License](https://github.com/capra314cabra/bf-gen/blob/master/LICENSE).
