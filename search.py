# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    
    openNodesList = Stack()     #Keep nodes which are being explored or will be exlpored
    closedNoseList = []         #Keep Track of visited Nodes
    pathToGoalState = []        #The path selected is being stored in this
    costOfMove = 0              #Cost of each movement towards goal state
    
    initial_move = problem.getStartState()
    openNodesList.push((initial_move, pathToGoalState, costOfMove))
    
    while not openNodesList.isEmpty():
        activeNode = openNodesList.pop()
        nodeObtained = activeNode[0]
        pathToGoalState = activeNode[1]
        
            
        """ Returning the path if it is a Goal State """
        if problem.isGoalState(nodeObtained):
            return pathToGoalState
        else:
            childNodes = problem.getSuccessors(nodeObtained)
            
            """ Appending the active Node to the visited list"""
            if nodeObtained not in closedNoseList:
                closedNoseList.append(nodeObtained)
            
            """ Iterating child Nodes """
            for nodes in childNodes:
                if nodes[0] not in closedNoseList:
                    node = nodes[0]
                    new_path = pathToGoalState + [nodes[1]]
                    openNodesList.push((node, new_path, nodes[2]))
    
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue
    
    openNodesList = Queue()
    closedNoseList = []
    pathToGoalState = []
    costOfMove = 0
    
    initial_move = problem.getStartState()
    openNodesList.push((initial_move, pathToGoalState, costOfMove))
    
    while not openNodesList.isEmpty():
        activeNode = openNodesList.pop()
        nodeObtained = activeNode[0]
        pathToGoalState = activeNode[1]
        
                
        """ Returning the path if it is a Goal State """
        if problem.isGoalState(nodeObtained):
            return pathToGoalState
        else:
            
            """ Appending the active Node to the visited list"""
            if nodeObtained not in closedNoseList:
                closedNoseList.append(nodeObtained)
        
            childNodes = problem.getSuccessors(nodeObtained)
            
            """ Iterating child Nodes """
            for nodes in childNodes:
                if nodes[0] not in closedNoseList and nodes[0] not in (item[0] for item in openNodesList.list):
                    node = nodes[0]
                    new_path = pathToGoalState + [nodes[1]]
                    openNodesList.push((node, new_path, nodes[2]))
        
        
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
   
    from util import PriorityQueue
    
    openNodesList = PriorityQueue()
    closedNoseList = set()
    pathToGoalState = []
    initial_cost = 0
    costOfMove = 0
    
    initial_move = problem.getStartState()
    
    openNodesList.push((initial_move, pathToGoalState, costOfMove), initial_cost)
   
    while not openNodesList.isEmpty():
        activeNode = openNodesList.pop()
        nodeObtained = activeNode[0]
        pathToGoalState = activeNode[1]
        costOfMove = activeNode[2]
        
        """If Goal state then return the path"""
        if problem.isGoalState(nodeObtained): 
            return pathToGoalState
        else:
            """Add the node in visited list if is not added"""
            if nodeObtained not in closedNoseList: 
                closedNoseList.add(nodeObtained)   
                
                """Getting successor of current node"""
                childNodes = problem.getSuccessors(nodeObtained)
                
                """Iterating successor nodes"""
                for nodes in childNodes:
                    node = nodes[0]
                    new_path = pathToGoalState + [nodes[1]]
                    new_cost = costOfMove + nodes[2]
                    openNodesList.push((node, new_path, new_cost), new_cost)
                
    
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    from util import PriorityQueue
    
    openNodesList = PriorityQueue()
    closedNodeList = []
    pathToGoalState = []
    priority = 0
    
    initial_move = problem.getStartState()
    
    openNodesList.push((initial_move, pathToGoalState), priority)
    
    while not openNodesList.isEmpty():
        activeNode = openNodesList.pop()
        nodeObtained = activeNode[0]
        pathToGoalState = activeNode[1]
        
        """Returning goal state if goal state is obtained"""
        if problem.isGoalState(nodeObtained):
            return pathToGoalState
        
        """Add current node in the visited list if not added"""
        if nodeObtained not in closedNodeList:
            closedNodeList.append(nodeObtained)
            
            """Getting the successor of current node"""    
            childNodes = problem.getSuccessors(nodeObtained)
            
            """Iterating successor nodes"""                
            for nodes in childNodes:
                if nodes[0] not in closedNodeList:
                    node = nodes[0]
                    new_path = pathToGoalState + [nodes[1]]
                        
                    """
                        F(n) = G(n) + H(n), 
                           where
                             G(n) is actual distance from node n to the start state, 
                             H(n) is the distance from node n to the goal state
                    """  
                        
                    g = problem.getCostOfActions(new_path)
                    h = heuristic(node, problem)
                        
                    f = g + h
                        
                    openNodesList.push((node, new_path), f)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
