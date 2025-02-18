# CSC 242-504
# Assign 5 template
# Put your name here

from time import localtime

# Remember that you are not allowed to use online resources
# when completing assignments, including AI tools

# List your collaborator(s) here
# If you did not collaborate with anyone, place a comment in the
# file indicating that

# Files without this information will earn a 0

# Include doc strings for full credit

# A class used in the first question
# Do not change
class NonNegFloat(object):
    'a class representing a non-negative floating point value'

    def isValid(self, num):
        return (type(num) == float or type(num) == int) and num >= 0.0
    
    def __init__(self, val = 0.0):
        if self.isValid(val):
            self.num = float(val)
        else:
            self.num = 0.0
    
    def __repr__(self):
        return f'NonNegFloat({self.num})'

    def __str__(self):
        return f"{self.num:.2f}"

    def get(self):
        return self.num

    def increase(self, value):
        if self.isValid(value):
            self.num += value

# The base class for the first question
# Do not change this class
class Movie(object):

    def __init__(self, title = "Barbie", director = "Greta Gerwig",\
                 year = 2023):
        self.title = title.title()
        self.director = director.title()
        current = localtime()[0]
        if type(year) == int and year >= 1888 and year <= current:
            self.year = year
        else:
            self.year = current
        self.sales = NonNegFloat()

    def getSales(self):
        return self.sales.get()

    def __repr__(self):
        return f"Movie({self.title}, {self.director}, {self.year}, ${self.sales})"

    def registerSales(self, amount):
        self.sales.increase(amount)

# A class to be used in the first question
# Do not change
class Award(object):
    'an award class'

    def __init__(self, name, organization):
        self.name = name.title()
        self.org = organization.title()

    def __repr__(self):
        return f"{self.name} from {self.org}"

# Question 1
# Write this class as described in the assignment
# Add doc strings to each method and to the class
class ShortFilm(Movie):

    """ A subclass of Movie(parent class) representing a short film which has a maximum runtime of 40 minutes."""
    # Write this method
    # Modfiy the header to provide default values
    def __init__(self, title="The Last Repair Shop", director="Ben Proudfoot/Kris Bowers", year=2023, t=39):
        """the initialization block for ShortFilm with their default values.
        Parameters: 
            i. title - must be an string. The default is The Last Repair Shop.
            ii. director - must be an string. The default is Ben Proudfoot/Kris Bowers.
            iii. year - must be an integer. The default is 2023.
            iv. t - the time must be an integer. Must be between 1 to 40 (less than 40)
        
        """
        Movie.__init__(self, title, director, year)
        if isinstance(t, int) and 0 < t < 40:
            self.running_time = t
        else:
            self.running_time = 39
        self.awards = []  # List to store Award objects


    # Write this method 
    def __repr__(self):

        """This method returns the string representation of the entered values."""
        return f"ShortFilm({self.title}, {self.director}, {self.year}, {self.running_time} min)"

    # Write this method
    def __str__(self):

        """This method returns the formatted string representation of the entered/ instance values - title, director and award values."""
        return f"{self.title} directed by {self.director} has these awards: {self.awards}"

    # Write this method
    def addAward(self, descript, org):
        
        """Any new values to the award variable gets added using the append method. So the paramters are as follows: 
            i. descript (str): Award description.
           ii. org (str): Organization giving the award."""
        self.awards.append(Award(descript, org))

    # Write this method
    def __iter__(self):
        
        """So this method returns an iterator over the awards in the reverse order - which means displaying the most recently added ones first"""
        return reversed(self.awards)

# IF NEEDED ITERATOR CLASS GOES HERE
# Do not make it part of the ShortFilm class


# The base class for the second question
# Do not change
class queue(object):
    def __init__(self):
        'the constructor'
        self.q = list()
        
    def dequeue(self):
        'removes and returns the first item in the queue'
        assert len(self.q) > 0, 'cannot dequeue from an empty queue'
        return self.q.pop(0)
    
    def enqueue(self, item):
        'add item to the back of the queue'
        self.q.append(item)
    
    def size(self):
        'returns the number of items in the queue'
        return len(self.q)
    
    def isEmpty(self):
        'return True if the queue is empty'
        return self.size() == 0
    
    def __repr__(self):
        'the representation'
        return repr(self.q)

    def __iter__(self):
        'the iterator'
        return iter(self.q)

# Complete this subclass
class scoreQueue(queue):

    """A subclass of queue that stores (score, name) tuples in sorted order."""
    # Write this method
    def enqueue(self, score, name):
        
        """ this method basically adds a (score, name) tuple to the queue - entering the items into the queue, ensuring the parameters are as follows:
            i.  score is an integer, else raise an assert statement.
            ii. name is a string, else raise an assert statement. 
        
            The fourth line of the code sorts the queue by the scores.
        """
        
        assert isinstance(score, int), f"{score} is not an integer"
        assert isinstance(name, str), f"{name} is not a string"

        self.q.append((score, name.title()))  # Append (score, title-cased name)
        self.q.sort()  # Sort queue in ascending order of scores

    # Write this method
    def dequeue(self):

        """ this method - removes and returns the first item in the queue in the format "Name has a Score".
            The first line of the code Calls the parent class `dequeue()` method. That removes and returns the first item in the queue."""
        assert len(self.q) > 0, 'cannot dequeue from an empty queue'
        item = self.q.pop(0) 
        return f"{item[1]} has a {item[0]}"

    # Do not change this method
    def __iter__(self):
        
        """ so this method basically returns an iterator over the queue."""
        return NameScoreIter(self.q)

# Complete this class
class NameScoreIter(object):
    
    """This class acts as an iterator for scoreQueue class that iterates over (score, name) tuples."""

    # Do not change this method
    def __init__(self, lst):
        """Initialization constructor with the list."""
        self.lst = lst
        self.index = 0

    # Write this method
    def __next__(self):

        """ so this method basically returns the next item in the format that is specified "Name has a Score". It also raises StopIteration if there are no more items."""

        if self.index >= len(self.lst):
            raise StopIteration  

        item = self.lst[self.index]  
        self.index += 1  
        return f"{item[1]} has a {item[0]}"

# Uncomment to test everything except the asserts

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))
