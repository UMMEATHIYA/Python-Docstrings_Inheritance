# CSC 242-504 - Assignment 5

## Overview

This assignment involves implementing classes and methods for managing a movie catalog with awards and handling a queue that stores score-name tuples in sorted order. Specifically, it focuses on creating a subclass for short films and implementing a custom queue class for score management. The assignment also requires the use of iterators and ensures that the code adheres to strict requirements on syntax and functionality.

### Key Features

- **Movie Class**: Represents a movie with attributes such as title, director, year, and sales.
- **ShortFilm Class**: Inherits from `Movie` and represents a short film with a runtime limit of 40 minutes. It includes additional functionality for awards.
- **Queue Class**: A base queue implementation for handling elements with basic enqueue and dequeue operations.
- **ScoreQueue Class**: A subclass of the `Queue` class that handles (score, name) tuples, ensuring they are sorted by score.
- **Iterator Class**: Implements an iterator for iterating over the score queue in the correct order.

## Requirements

1. **ShortFilm Class**:
    - Must inherit from `Movie`.
    - Should allow setting attributes like title, director, year, and runtime (between 1 and 40).
    - Should allow adding awards and provide a method to list awards in reverse order.

2. **Queue Class**:
    - Provides basic queue operations such as enqueue, dequeue, size, and isEmpty.

3. **ScoreQueue Class**:
    - Inherits from `Queue` and manages a queue of (score, name) tuples sorted by score.
    - Ensures the (score, name) tuples are sorted in ascending order.
    - Implements a custom iterator to return formatted strings for each score-item pair.

4. **Iterator Class**:
    - Implements an iterator for the `scoreQueue` class to iterate over items in a sorted queue, displaying each tuple in the format "Name has a Score".

## Code Description

- **NonNegFloat Class**: Represents a non-negative floating-point number used for movie sales.
- **Movie Class**: A base class representing a movie, including methods to get sales and register new sales.
- **Award Class**: A class to represent an award with a name and the organization that presented it.
- **ShortFilm Class**: A subclass of `Movie` that includes an additional `running_time` attribute and a list of awards. It also includes methods for adding and iterating over awards.
- **queue Class**: A base class implementing basic queue functionality.
- **scoreQueue Class**: A subclass of `queue` that ensures the (score, name) tuples are sorted by score.
- **NameScoreIter Class**: Implements an iterator to traverse the scoreQueue in a specific format.

## Usage

You can test the functionality by running the script. Ensure you have the necessary testing file (`hw5TEST.py`) to validate your implementation. You can run the test suite using the `doctest` module:

```bash
python csc242hw5.py
