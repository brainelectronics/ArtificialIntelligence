#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In this exercise, you will help Pacman solve various tasks by implementing 
search algorithms. These exercises are adapted from the UC Berkeley cource on 
AI. You are welcome to also check the descriptions of the problems given there. 
The underlying code is mostly the same, except for small modifications for 
running in the notebook.

Before you start coding your algorithms we strongly recommend you to:
- read through the whole assignment first as some of the search algorithms will 
	be used for the second part of the assignment.
- be aware that you can always test your code with the provided test cases 
	before submitting.
- get familiar with the provided data types and try to use them within your 
	algorithms. We provided a separate notebook file to give you a short 
	introduction to them.
- check the python tutorial for the proper use of standard data types within
	python to prevent relatively easy errors
"""

"""
Setting up the game

The general way to set up a pacman game is shown below. First, a few imports 
from the pac package that contains all the necessary modules are needed 
(Do not modify this part!).
"""

# import pac
# from pac import util
# from pac import search
# from pac import layout
# from pac import pacman
# from pac.searchAgents import SearchAgent
# from pac.searchAgents import PositionSearchProblem
# from pac.game import Actions, Directions
# from pac.pacman_utils import NotebookGraphics
# rules = pacman.ClassicGameRules(timeout=0)

"""
Running the game

This is an example where Pacman plays against two ghosts. You can copy it into 
a new cell and it will run a game. What the single lines do will be discussed 
below:

rules = pac.pacman.ClassicGameRules(0)
from pac.pacmanAgents import GreedyAgent
mr_pacman = GreedyAgent()  # controls the pacman behavior
from pac.ghostAgents import RandomGhost
ghosts = [RandomGhost(1), RandomGhost(2)]  # controls the behavior of two ghosts
gameDisplay = NotebookGraphics()  # initialize the display of the playing field
lay = layout.getLayout('mediumClassic')  # load the layout of the map
# instantiate a Game instance, see below
game = rules.newGame(lay, mr_pacman, ghosts, gameDisplay, False, False)
game.run()  # run the game, until Pacman is caught by a ghost or there is no food left

Layouts
Layouts encode the map on which Pacman moves. You can load different layouts 
with a call to

mylayout = layout.getLayout(layout_name)

Important layouts for the first part of this assignment are tinyMaze, 
mediumMaze, bigMaze, and openMaze.

The Search Agent
The behavior of all characters in the game is controlled by an Agent class 
instance, such as the GreedyAgent or RandomAgent above. In this assignment, the 
SearchAgent class will serve as a container for the algorithms you will 
implement. It needs a search function and the definition of the problem to be 
solved (how the search states are generated, etc.). These are passed as 
arguments fn and prob to the constructor of the SearchAgent.

search_agent = SearchAgent(fn=some_search_function, prob=AProblemClass)

The position search problem
The goal of the first part of this exercise is to implement and compare 
different search algorithms. They are all used to get Pacman from a start 
position to a goal in a typical Pacman world. The definition of the search 
space, in which this problem should be solved, is given as a 
PositionSearchProblem instance.

Here is an example of a very simple, deterministic search function that just 
returns a hardcoded sets of directions, and solves the search problem for the 
tinyMaze layout (but not any other, of course):
"""
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from pac.game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

"""
The search functions receive a problem variable as an argument, which has 
several methods that can be called by your code to get all relevant information. 
This is an example how to retrieve the start state from a search problem and 
how to check if the start state is already also a goal state:

start_state = problem.getStartState()
check_goal = problem.isGoalState(start_state)

The states that are reachable in a single step from the state can be retrieved 
with:

successors = problem.getSuccessors(start_state)

This returns a list of (successor_state, action, cost) tuples, where action is 
the Action that transitions from start_state to successor_state, and cost is 
the cost of taking that action.

Note that the state representation for search problems is not limited to the 
space of positions on a board, as in the Pacman problem. States can be anything, 
positions, abstract symbols, or higher-dimensional objects. You will design a 
state representation for a different problem in the second part of this exercise.

The return value of a search function is, as in the tinyMazeSearch example 
above, a sequence of Actions, as you get from the getSucessors method above.

For experimenting with the state and problem representations used in the search 
functions directly in a notebook cell outside of a search function, you can get 
a problem instance such as the one passed as an argument to the search 
functions like so:

# no search function given here, this Agent is just for experimenting!
sa = SearchAgent(prob=PositionSearchProblem)
lay = layout.getLayout('mediumClassic')
game = rules.newGame(lay, sa, [], None, False, False)
problem = sa.searchType(game.state)
successors = problem.getStartState()
print(successors)

This you can also use to run your search function on a problem with a given 
layout, to get the corresponding path:
tinyMazeSearch(problem)

Visualization and running the game
The call gameDisplay = NotebookGraphics(sleep_time=0.2) initializes a 
visualization of the Pacman playing field that can be shown inside the notebook. 
The playing field will always be displayed in the cell where the 
NotebookGraphics instance is created, even if the game is run in a different 
cell. The speed of the game is regulated by setting the sleep_time parameter 
in the NotebookGraphics class constructor.

The game is started by calling the run method on a Game instance. There might 
be some JavaScript errors that you can ignore as long as the game runs 
(JavaScript programmers who can fix this are very welcome to do so!).
"""
# tiny_maze_layout = layout.getLayout('tinyMaze')  # load the layout of the map

# sa = SearchAgent(fn=tinyMazeSearch, prob=PositionSearchProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.2)  # visualization
# game = rules.newGame(tiny_maze_layout, sa, [], gameDisplay, False, False)
# game.run()
"""
You can stop the game while it is running by interrupting the ipython kernel, 
which you can do either using the menu above or by pressing Escape to get into 
command mode and then the letter i twice. (By the way: You can see all keyboard 
shortcuts the notebook offers if you press h in command mode.)
"""

"""
Data types

For the implementation of the search algorithms, you can use the simple data 
types Stack, Queue and PriorityQueue from the pac.util module provided for 
this, or you can use your own types. You can get more information about the 
provided data types by using the question mark to get documentation, as for 
all other objects of interest.
"""



"""
Depth First Search [6 Points]

Implement depth first search for an arbitrary problem. Note that not only the 
sequence of actions that is returned has to be correct, also the nodes have to 
expanded in the correct order, as it is described by the depth-first search 
paradigm. A node is counted as expanded when you call the getSucessors method 
with it as an argument. For example, expanding a node twice will lead to a 
program execution that is not correct.

Note also that the path that is returned is also a result of the order the 
search algorithm expands the nodes. In order to retrieve the correct path, you 
have to keep track of how the search algorithm arrived at each node.

As a starting hint, we recommend to get familiar with the provided data types 
Stack, Queue and PriorityQueue before starting with implementing any code. In 
addition, you should not hard-code state representation such as (1, 1) and a
ctions, e.g. "North" or "East" into your algorithm. Your submission will be 
checked on arbitrary problems with a different state and action representation,
so your implementation must be independent from this. In addition, please read 
through the second half of the assignment first, to see the requirements of 
your algorithms.

Also, make sure you implement iterative versions of the search algorithms. 
Although they can be implemented in a recursive fashion, this is more error-prone
and very hard to debug. In addition, python does not optimize recursions and 
has a hard limit on recursion level that might be exceeded.

While working on the implementation for the search algorithms, it might happen 
that you create an infinite loop. To prevent this, it could be a good idea to 
put a maximum to the iterations you allow the algorithm to perform. If an 
infinite loop occurs nevertheless, you can try to restart the ipython kernel 
(Escape - i - i) and/or close and reopen the browser tab.
"""
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())  # delete this later, otherwise the start state 
    #                                                                             # will count as expanded twice!

    print 'problem', problem


    myStack = Stack()

    nextOfStart = problem.getStartState()
    myVisited = [nextOfStart] # liste fur alle besuchten positionen
    #print nextOfStart
    myWay = []
    myStack.push((nextOfStart, []))

    #for x in range(50):
    while not myStack.isEmpty():
        currentState, currentPosition = myStack.pop() # ich bin gerade bei z.b. (5, 5)
        #print "i am at", currentState

        if problem.isGoalState(currentState): # found goal
            print "found goal"
            myWay = currentPosition
            break
        # unkomment, because double expaneded
        #if currentState not in myVisited:
        #    myVisited.append(currentState)
        if currentState in myVisited:
            continue
        myVisited.append(currentState)
        nextDirections = problem.getSuccessors(currentState) # alle moglichen richtugnen vom aktuellen stand

        for ele in nextDirections:
            (theNeighbor, theDirection) = ele[0], ele[1]
            if theNeighbor not in myVisited:
                someStuff = (theNeighbor, (currentPosition+[theDirection]))
                #print someStuff
                myStack.push(someStuff) # legt alle weiteren moglichen richtungen auf stack
        
    return myWay

# sa = SearchAgent(fn=depthFirstSearch, prob=PositionSearchProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.2)  # visualization
# game = rules.newGame(tiny_maze_layout, sa, [], gameDisplay, False, False)
# game.run()



"""
Breadth First Search [6 Points]

Implement breadth first search. The same restrictions with respect to expanding 
states etc. as above apply. Note that you can probably reuse most of your 
depth-first search code; depending on your implementation you might only have 
to change one line in the body of the function.
"""
def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first, and return the corresponding path.
    """
    "*** YOUR CODE HERE ***"
    # reused stuff from above...
    myQueue = Queue()

    myVisited = [] # leere liste fur alle besuchten positionen
    nextOfStart = problem.getStartState()
    #print nextOfStart
    myWay = []
    myQueue.push((nextOfStart, []))

    #for x in range(50):
    while not myQueue.isEmpty():
        currentState, currentPosition = myQueue.pop() # ich bin gerade bei z.b. (5, 5)
        #print "i am at", currentState

        if problem.isGoalState(currentState): # found goal
            print "found goal"
            myWay = currentPosition
            break
        # unkomment, because double expaneded
        #if currentState not in myVisited:
        #    myVisited.append(currentState)
        if currentState in myVisited:
            continue
        myVisited.append(currentState)
        nextDirections = problem.getSuccessors(currentState) # alle moglichen richtugnen vom aktuellen stand

        for ele in nextDirections:
            (theNeighbor, theDirection) = ele[0], ele[1]
            if theNeighbor not in myVisited:
                nextQueueStuff = (theNeighbor, (currentPosition+[theDirection])) 
                #print nextQueueStuff
                myQueue.push(nextQueueStuff) 
        
    return myWay

# sa = SearchAgent(fn=breadthFirstSearch, prob=PositionSearchProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.01)  # visualization
# game = rules.newGame(tiny_maze_layout, sa, [], gameDisplay, False, False)
# game.run()



"""
Uniform Cost Search [6 Points]

Implement uniform cost search, i.e. a search algorithm that expands the node 
with the lowest total path cost leading to it first. Again, the code should 
mostly be the same as in the other search functions.
"""
def uniformCostSearch(problem):
    "Search the node of least total cost first."
    "*** YOUR CODE HERE ***"
    # reused stuff from above...
    myPrioQueue = PriorityQueue()

    myVisited = [] # leere liste fur alle besuchten positionen
    nextOfStart = problem.getStartState()
    #print nextOfStart
    myWay = []
    myPrioQueue.push((nextOfStart, [], 0), 0) #(element, weight)

    #for x in range(50):
    while not myPrioQueue.isEmpty():
        (currentState, currentPosition, costOfThisState) = myPrioQueue.pop() # ich bin gerade bei z.b. (5, 5)
        #print "i am at", currentState

        if problem.isGoalState(currentState): # found goal
            print "found goal"
            myWay = currentPosition
            break
        # unkomment, because double expaneded
        #if currentState not in myVisited:
        #    myVisited.append(currentState)
        if currentState in myVisited:
            continue
        myVisited.append(currentState)
        nextDirections = problem.getSuccessors(currentState) # alle moglichen richtugnen vom aktuellen stand

        for ele in nextDirections:
            (theNeighbor, theDirection, theCost) = ele[0], ele[1], ele[2]
            if theNeighbor not in myVisited:
                nextQueueStuff = (theNeighbor, (currentPosition+[theDirection]), (costOfThisState+theCost)) 
                #print nextQueueStuff
                myPrioQueue.push(nextQueueStuff, (costOfThisState+theCost)) 
        
    return myWay

# sa = SearchAgent(fn=uniformCostSearch, prob=PositionSearchProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.01)  # visualization
# game = rules.newGame(tiny_maze_layout, sa, [], gameDisplay, False, False)
# game.run()


"""
A* Search [9 Points]

Implement A* graph search in the empty function aStarSearch below. A* takes a 
heuristic function as an argument. Heuristics take two arguments: a state in 
the search problem (the main argument), and the problem itself (for reference 
information). The nullHeuristic heuristic function is given below.
"""
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    
    myPrioQueue = PriorityQueue()

    myVisited = [] # leere liste fur alle besuchten positionen
    nextOfStart = problem.getStartState()
    #print nextOfStart
    myWay = []
    myPrioQueue.push((nextOfStart, [], 0), 0) #(element, weight)

    #for x in range(50): # for safety!
    while not myPrioQueue.isEmpty():
        (currentState, currentPosition, costOfThisState) = myPrioQueue.pop() # ich bin gerade bei z.b. (5, 5)
        # print "i am at", currentState

        if problem.isGoalState(currentState): # found goal
            print "found goal"
            myWay = currentPosition
            break
        if currentState not in myVisited:
            myVisited.append(currentState)
            nextDirections = problem.getSuccessors(currentState) # alle moglichen richtugnen vom aktuellen stand

            for ele in nextDirections:
                (theNeighbor, theDirection, theCost) = ele[0], ele[1], ele[2]
                if theNeighbor not in myVisited:
                    nextQueueStuff = (theNeighbor, (currentPosition+[theDirection]), (costOfThisState+theCost)) 
                    # print nextQueueStuff
                    myPrioQueue.push(nextQueueStuff, (costOfThisState+theCost+heuristic(theNeighbor, problem))) 

    return myWay

"""
You can test your A* implementation on the original problem of finding a path 
through a maze to a fixed position using the Manhattan distance heuristic:
"""
# from pac.searchAgents import manhattanHeuristic
# big_maze_layout = layout.getLayout('bigMaze')

# sa = SearchAgent(fn=lambda pb: aStarSearch(pb, manhattanHeuristic), prob=PositionSearchProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.01)  # visualization
# game = rules.newGame(big_maze_layout, sa, [], gameDisplay, False, False)
# game.run()

"""
This example code introduces a new programing concept, a lambda function to 
call the aStarSearch function, which takes two arguments, with only one variable 
argument pb for the problem definition, while the second one for the heuristic 
is bound to manhattanHeuristic. You can read more about lambda functions here.
http://www.secnetix.de/olli/Python/lambda_functions.hawk

You should see that A* finds the optimal solution slightly faster than uniform 
cost search (about 470 vs. 620 search nodes expanded for bigMaze in our
implementation, but ties in priority may make your numbers differ slightly). 
What happens on openMaze for the various search strategies?
"""
# # Abbreviations, please leave these in here!
# bfs = breadthFirstSearch
# dfs = depthFirstSearch
# astar = aStarSearch
# ucs = uniformCostSearch



"""
Solving problems
Corner Problem [9 Points]
Finding All the Corners

The real power of A* will only be apparent with a more challenging search 
problem. Now, it's time to formulate a new problem and design a heuristic for it.

In corner mazes, there are four dots, one in each corner. Our new search 
problem is to find the shortest path through the maze that touches all four 
corners (whether the maze actually has food there or not). Note that for some 
mazes like tinyCorners, the shortest path does not always go to the closest 
food first! Hint: the shortest path through tinyCorners takes 28 steps.

Note: Make sure to implement breadth first search before trying this problem.

Implement the CornersProblem search problem below. You will need to choose a 
state representation that encodes all the information necessary to detect 
whether all four corners have been reached. Now, your search agent should solve 
the corners problem for the tinyCorners and mediumCorners layouts.

To receive full credit, you need to define an abstract state representation 
that does not encode irrelevant information (like the position of ghosts, where 
extra food is, etc.). In particular, do not use a full Pacman GameState as 
a search state. Your code will be very, very slow if you do (and also wrong).

Hint: The only parts of startingGameState you need to reference in your 
implementation are the starting Pacman position and the location of the four 
corners.

Our implementation of breadthFirstSearch expands just under 2000 search nodes 
on the mediumCorners layout. However, heuristics (used with A* search) can 
reduce the amount of searching required.
"""
class CornersProblem(search.SearchProblem):
    """
    This search problem finds paths through all four corners of a layout.
    You must select a suitable state space and successor function.
    """

    def __init__(self, startingGameState):
        """
        Stores the walls, pacman's starting position and corners.
        """
        self.walls = startingGameState.getWalls()
        self.startingPosition = startingGameState.getPacmanPosition()
        top, right = self.walls.height-2, self.walls.width-2
        self.corners = ((1,1), (1,top), (right, 1), (right, top))
        for corner in self.corners:
            if not startingGameState.hasFood(*corner):
                print 'Warning: no food in corner ' + str(corner)
        self._expanded = 0 # Number of search nodes expanded


        # Please add any code here which you would like to use
        # in initializing the problem     
        self.theStartState = (self.startingPosition, self.corners) #?!   
        
    def getStartState(self):
        "Returns the start state (in your state space, not the full Pacman state space)"
        "*** YOUR CODE HERE ***"
        # raise NotImplementedError
        return self.theStartState

    def isGoalState(self, state):
        "Returns whether this search state is a goal state of the problem"
        "*** YOUR CODE HERE ***"
        # raise NotImplementedError
        isGoal = False
        if state in self.corners:
            isGoal = True
        else:
            isGoal = False
        return isGoal

    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            # x, y = state[:2]
            # dx, dy = Actions.directionToVector(action)
            # nextx, nexty = int(x + dx), int(y + dy)
            # hitsWall = self.walls[nextx][nexty]
            
            "*** YOUR CODE HERE ***" 
            # raise NotImplementedError
            successors = []
            for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
                # Add a successor state to the successor list if the action is legal
                # Here's a code snippet for figuring out whether a new position hits a wall:
                # x, y = state[:2]
                # dx, dy = Actions.directionToVector(action)
                # nextx, nexty = int(x + dx), int(y + dy)
                # hitsWall = self.walls[nextx][nexty]
                
                "*** YOUR CODE HERE ***"
                givenCornersLeft = state[1] # get the corners which are not visited
                #print "cornersLeft", cornersLeft
                
                # angabe
                (x,y) = state[0] # first element of triple
                (dx, dy) = Actions.directionToVector(action)
                (nextx, nexty)= int(x + dx), int(y + dy)
                hitsWall = self.walls[nextx][nexty]
                # ende angabe
                if not hitsWall:
                    # Add a successor state to the successor list if the action is legal
                    thisTimeCornersLeft = []
                    for aCorner in givenCornersLeft:
                        thisTimeCornersLeft.append(aCorner)
                        
                    if (nextx, nexty) in thisTimeCornersLeft:
                        thisTimeCornersLeft.remove((nextx,nexty))
                    stepCost = 1 # ... and a cost of 1
                    newSubSuccessor = ((nextx, nexty), thisTimeCornersLeft) # update with this loop remaining corners
                    newSuccessor = (newSubSuccessor, action, 1)
                    #print "newSuccessor", newSuccessor
                    successors.append(newSuccessor)            
              
            self._expanded += 1 # as done by the already used getSuccessor
            return successors

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999.  This is implemented for you.
        """
        if actions == None: return 999999
        x,y= self.startingPosition
        for action in actions:
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]: return 999999
        return len(actions)

"""
You can get the path which results from searching in your state space like so:
"""
# tiny_corner_layout = layout.getLayout('tinyCorners')
# medium_corner_layout =layout.getLayout('mediumCorners')

# gameState = pacman.GameState()
# gameState.initialize(tiny_corner_layout, 0)

# problem = CornersProblem(gameState)
# path = bfs(problem)

"""
And you can also run the game on a map
"""
# sa = SearchAgent(fn=breadthFirstSearch, prob=CornersProblem)
# gameDisplay = NotebookGraphics(sleep_time=0.01)  # visualization
# game = rules.newGame(tiny_corner_layout, sa, [], gameDisplay, False, False)
# game.run()



"""
Heuristic Solution for the Corners Problem [9 Points]

Note: Make sure to implement A* search before working on this assignment.

Implement a non-trivial, consistent heuristic for the CornersProblem in 
cornersHeuristic below.

Admissibility vs. Consistency: Remember, heuristics are just functions that 
take search states and return numbers that estimate the cost to a nearest goal. 
More effective heuristics will return values closer to the actual goal costs. 
To be admissible, the heuristic values must be lower bounds on the actual 
shortest path cost to the nearest goal (and non-negative). To be consistent, 
it must additionally hold that if an action has cost c, then taking that action 
can only cause a drop in heuristic of at most c.

Remember that admissibility isn't enough to guarantee correctness in graph 
search — you need the stronger condition of consistency. However, admissible 
heuristics are usually also consistent, especially if they are derived from 
problem relaxations. Therefore it is usually easiest to start out by 
brainstorming admissible heuristics. Once you have an admissible heuristic that 
works well, you can check whether it is indeed consistent, too. The only way to 
guarantee consistency is with a proof. However, inconsistency can often be 
detected by verifying that for each node you expand, its successor nodes are 
equal or higher in in f-value. Moreover, if UCS and A* ever return paths of 
different lengths, your heuristic is inconsistent. This stuff is tricky!

Non-Trivial Heuristics: The trivial heuristics are the ones that return zero everywhere (UCS) and the heuristic which computes the true completion cost. The former won't save you any time, while the latter will timeout the autograder. You want a heuristic which reduces total compute time, though for this assignment the autograder will only check node counts (aside from enforcing a reasonable time limit).

Grading: Your heuristic must be a non-trivial non-negative consistent heuristic to receive any points. Make sure that your heuristic returns 0 at every goal state and never returns a negative value. Depending on how few nodes your heuristic expands, you'll be graded proportional to:

The evaluation is based on the mediumCorners layout.
Number of nodes expanded 	Grade
more than 2000 	0/9
at most 2000 	3/9
at most 1600 	6/9
at most 1200 	9/9

Remember: If your heuristic is inconsistent, you will receive no credit, so be 
careful!

Yet another note: If you are unsure whether your A* implementation is correct, 
you can use a reference implementation to try out your heuristics on the 
testcases of the autograder. To use this, put

USE_REFERENCE_ASTAR = True

in your submission. In that case, 3 points for each of the two heuristics 
exercises will be deducted if you get any points using the reference 
implementation, so you should still try to fix your A* — if it works with the 
reference and not with yours, there is very likely an error.
"""
def cornersHeuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound
    on the shortest path from the state to a goal of the problem; i.e.
    it should be admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"
    return 0  # Default to trivial solution

class AStarCornersAgent(SearchAgent):
    """A SearchAgent for CornersProblem using A* and your cornersHeuristic
    
    No need to change anything here.
    """
    def __init__(self):
        self.searchFunction = lambda prob: aStarSearch(prob, cornersHeuristic)
        self.searchType = CornersProblem
"""
Get the number of expanded states to see how much improvement the heuristic 
provides over the naive heuristic:
"""
# tiny_corner_layout = layout.getLayout('tinyCorners')
# medium_corner_layout = layout.getLayout('mediumCorners')
# big_corner_layout = layout.getLayout('bigCorners')

# gameState = pacman.GameState()
# gameState.initialize(medium_corner_layout, 0)

# problem = CornersProblem(gameState)

# aStarSearch(problem, cornersHeuristic);
# print 'number of expanded states', problem._expanded

# sa = AStarCornersAgent()
# gameDisplay = NotebookGraphics(sleep_time=0.01)  # visualization
# game = rules.newGame(layout.getLayout('bigCorners'), sa, [], gameDisplay, False, False)
# game.run()



"""
Food Search Problem [12+ Points]

This is the code we will be working with for this exercise:
"""
class AStarFoodSearchAgent(SearchAgent):
    """A SearchAgent for FoodSearchProblem using A* and your foodHeuristic
    
    No need to change anything here.
    """
    def __init__(self):
        self.searchFunction = lambda prob: aStarSearch(prob, foodHeuristic)
        self.searchType = FoodSearchProblem

class FoodSearchProblem:
    """
    A search problem associated with finding a path that collects all of the
    food (dots) in a Pacman game.

    A search state in this problem is a tuple ( pacmanPosition, foodGrid ) where
      pacmanPosition: a tuple (x,y) of integers specifying Pacman's position
      foodGrid:       a Grid (see pac.game module) of either True or False, specifying remaining food
    """
    def __init__(self, startingGameState):
        self.start = (startingGameState.getPacmanPosition(), startingGameState.getFood())
        self.walls = startingGameState.getWalls()
        self.startingGameState = startingGameState
        self._expanded = 0
        self.heuristicInfo = {} # A dictionary for the heuristic to store information

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state[1].count() == 0

    def getSuccessors(self, state):
        "Returns successor states, the actions they require, and a cost of 1."
        successors = []
        self._expanded += 1
        for direction in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            x,y = state[0]
            dx, dy = Actions.directionToVector(direction)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextFood = state[1].copy()
                nextFood[nextx][nexty] = False
                successors.append( ( ((nextx, nexty), nextFood), direction, 1) )
        return successors

    def getCostOfActions(self, actions):
        """Returns the cost of a particular sequence of actions.  If those actions
        include an illegal move, return 999999"""
        x,y= self.getStartState()[0]
        cost = 0
        for action in actions:
            # figure out the next state and see whether it's legal
            dx, dy = Actions.directionToVector(action)
            x, y = int(x + dx), int(y + dy)
            if self.walls[x][y]:
                return 999999
            cost += 1
        return cost

"""
Eating All The Dots

Now we'll solve a hard search problem: eating all the Pacman food in as few 
steps as possible. For this, we'll need a new search problem definition which 
formalizes the food-clearing problem: FoodSearchProblem as defined below. 
A solution is defined to be a path that collects all of the food in the Pacman 
world. For the present project, solutions do not take into account any ghosts 
or power pellets; solutions only depend on the placement of walls, regular 
food and Pacman. (Of course ghosts can ruin the execution of a solution!). 
If you have written your general search methods correctly, A* with a null 
heuristic (equivalent to uniform-cost search) should quickly find an optimal 
solution on the testSearch layout with no code change on your part 
(total cost of 7).

sa = AStarFoodSearchAgent()
gameDisplay = NotebookGraphics(sleep_time=0.1)
game = rules.newGame(layout.getLayout('testSearch'), sa, [], gameDisplay, False, False)
game.run()

AStarFoodSearchAgent is a shortcut for 
SearchAgent(fn=lambda pb: astar(pb, foodHeuristic), prob=FoodSearchProblem). 
It is implemented above.

You should find that UCS starts to slow down even for the seemingly simple 
tinySearch.

Note: Make sure to implement A* search before working on this assignment.

Our UCS agent finds the optimal solution after exploring over 16,000 nodes.

Any non-trivial non-negative consistent heuristic will receive 1 point. Make 
sure that your heuristic returns 0 at every goal state and never returns a
negative value. Depending on how few nodes your heuristic expands, you'll get 
additional points:
Number of nodes expanded 	Grade (proportional)
more than 15000 	3/12
at most 15000 	6/12
at most 12000 	9/12
at most 9000 	12/12 (full credit; medium)
at most 7000 	15/12 (optional extra credit; hard)

Remember: If your heuristic is inconsistent, you will receive no credit, so be 
careful!

This heuristic must be consistent to ensure correctness.
First, try to come up with an admissible heuristic; almost all admissible 
heuristics will be consistent as well.

If using A* ever finds a solution that is worse than what uniform cost search 
finds, your heuristic is not consistent, and probably not admissible! On the 
other hand, inadmissible or inconsistent heuristics may find optimal solutions, 
so be careful.

The state is a tuple (pacmanPosition, foodGrid) where foodGrid is a game.Grid 
of either True or False. You can call foodGrid.asList() to get a list of food 
coordinates instead.

If you want access to info like walls, capsules, etc., you can query the 
problem. For example, problem.walls gives you a Grid of where the walls are.

If you want to store information to be reused in other calls to the heuristic, 
there is a dictionary called problem.heuristicInfo that you can use. For 
example, if you only want to count the walls once and store that value, try:

  problem.heuristicInfo['wallCount'] = problem.walls.count()

Subsequent calls to this heuristic can access problem.heuristicInfo['wallCount'].

Remember that you can also use the reference A* implementation for this 
exercise as described above; however, if you do, you will get 3 points less 
than with your own A* implementation.
"""
def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    
    return 0  # Default to trivial solution

"""
Fill in foodHeuristic below with a consistent heuristic for the 
FoodSearchProblem. Try your agent on the trickySearch board:
"""
# sa = AStarFoodSearchAgent()
# gameDisplay = NotebookGraphics(sleep_time=0.1)  # visualization
# game = rules.newGame(layout.getLayout('trickySearch'), sa, [], gameDisplay, False, False)
# game.run()



"""
Suboptimal Search [6 Points]

Sometimes, even with A* and a good heuristic, finding the optimal path through 
all the dots is hard. In these cases, we'd still like to find a reasonably 
good path, quickly. In this section, you'll write an agent that always greedily 
eats the closest dot. ClosestDotSearchAgent is implemented for you below, but 
it's missing a key function that finds a path to the closest dot.
"""
class ClosestDotSearchAgent(SearchAgent):
    "Search for all food using a sequence of searches"
    def registerInitialState(self, state):
        self.actions = []
        currentState = state
        while(currentState.getFood().count() > 0):
            nextPathSegment = self.findPathToClosestDot(currentState) # The missing piece
            self.actions += nextPathSegment
            for action in nextPathSegment:
                legal = currentState.getLegalActions()
                if action not in legal:
                    t = (str(action), str(currentState))
                    raise Exception, 'findPathToClosestDot returned an illegal move: %s!\n%s' % t
                currentState = currentState.generateSuccessor(0, action)
        self.actionIndex = 0
        print 'Path found with cost %d.' % len(self.actions)

    def findPathToClosestDot(self, gameState):
        "Returns a path (a list of actions) to the closest dot, starting from gameState"
        # Here are some useful elements of the startState
        startPosition = gameState.getPacmanPosition()
        food = gameState.getFood()
        walls = gameState.getWalls()
        problem = AnyFoodSearchProblem(gameState)

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

class AnyFoodSearchProblem(PositionSearchProblem):
    """
      A search problem for finding a path to any food.

      This search problem is just like the PositionSearchProblem, but
      has a different goal test, which you need to fill in below.  The
      state space and successor function do not need to be changed.

      The class definition above, AnyFoodSearchProblem(PositionSearchProblem),
      inherits the methods of the PositionSearchProblem.

      You can use this search problem to help you fill in
      the findPathToClosestDot method.
    """

    def __init__(self, gameState):
        "Stores information from the gameState.  You don't need to change this."
        # Store the food for later reference
        self.food = gameState.getFood()

        # Store info for the PositionSearchProblem (no need to change this)
        self.walls = gameState.getWalls()
        self.startState = gameState.getPacmanPosition()
        self.costFn = lambda x: 1
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def isGoalState(self, state):
        """
        The state is Pacman's position. Fill this in with a goal test
        that will complete the problem definition.
        """
        x, y = state

        "*** YOUR CODE HERE ***"
        raise NotImplementedError

"""
Implement the method findPathToClosestDot. Our agent solves this maze 
(suboptimally!) with a path cost of 350:

Hint: The quickest way to complete findPathToClosestDot is to fill in the 
AnyFoodSearchProblem, which is missing its goal test. Then, solve that problem 
with an appropriate search function. The solution should be very short!

Your ClosestDotSearchAgent won't always find the shortest possible path through 
the maze. Make sure you understand why and try to come up with a small example 
where repeatedly going to the closest dot does not result in finding the 
shortest path for eating all the dots.
"""
# sa = ClosestDotSearchAgent()
# gameDisplay = NotebookGraphics(sleep_time=0.05)  # visualization
# game = rules.newGame(layout.getLayout('bigSearch'), sa, [], gameDisplay, False, False)
# game.run()

