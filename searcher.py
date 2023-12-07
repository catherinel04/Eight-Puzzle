#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Catherine Liu
# email:cliu26@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Fiona Wu
# partner's email: fionayw@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ constructs new Searcher object """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """ adds single state object to Searcher's list of untested states """
        self.states += [new_state]
        
    def should_add(self, state):
        """ returns True if called Searcher should add state to its list of
            untested states, and False otherwise """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else: 
            return True
        
    def add_states(self, new_states):
        """ processes the elements of list new_states one at a time """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ performs full state-search that begins at initial state 
            and ends when goal state is found or when no untested states """
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None
            


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ a class that performs BF search """
    def next_state(self):
        """ follows FIFO to choose the next state """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """ a class that performs DF search """
    def next_state(self):
        """ follows LIFO to choose the next state """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ a heuristic functions that computes and estimate how many 
        additional moves needed to get from state to goal state """
    return state.board.num_misplaced()

def h2(state):
    """ a heuristic function that computes and estimates how many
        additional moves through how far displaced """
    return state.board.num_wrong()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def __init__(self, heuristic):
        """ constructor for GreedySearcher object """
        super().__init__(-1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ adds a sublist that is a [priority, state] pair where priority
            is the priority of state that is determined by calling the 
            priority method """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ chooses one of the states with highest priority"""
        s = max(self.states)
        self.states.remove(s)
        return s[1]


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A class for objects that perform an informed search algorithm that assigns
        a priority to each state based on a heuristic function """
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
        
        
        