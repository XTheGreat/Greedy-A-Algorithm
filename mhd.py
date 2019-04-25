import copy, time

# Manhattan Distance Heuristics

class Puzzle(object):
    """A sliding-block puzzle."""
  
    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid) # No aliasing!
    
    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print number,
            print
        print

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN

        currentState = self.grid

        # For array instance of Puzzle
        def returnAsArray(state):
            grid = []
            for i in range(0, len(state)):
                row = self.grid[i]
                for j in range(0, len(row)):
                    node = row[j]
                    if (node == ' '):
                        node = 0
                    grid.append(node)
            return grid

        # For possible moves from Puzzle
        def possibleMoves(state):
            # Get possible moves
            possibleMoves = [] 
            curposMoves = []
            for i in range(0, len(state)):
                row = state[i]
                for j in range(0, len(row)):
                    node = row[j]
                    if (node == ' '):
                        x = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                        for i in range (0, len(x)):
                            nextMove = x[i]
                            r = nextMove[0]
                            c = nextMove[1]
                            if (r >= 0 and r <= 2):
                                if (c >= 0 and c <= 2):
                                    possibleMoves.append(nextMove)

            for x in range(0, len(possibleMoves)):
                nextMove = possibleMoves[x]
                r = int(nextMove[0])
                c = int(nextMove[1])
                for i in range(0, len(state)):
                    row = state[i]
                    for j in range(0, len(row)):
                        node = row[j]
                        if (r == i and j == c):
                            if(len(nodes) == 0):
                                curposMoves.append(node)
                            if(len(nodes) > 0):
                                pop =  len(nodes) - 1
                                if (nodes[pop] == node):
                                    silence = "Silence is golden"
                                else:
                                    curposMoves.append(node)
                            
            return curposMoves

        def forecast(moves):
            distances = []
            for i in range (0, len(moves)):
                state = returnAsArray(self.grid)
                for j in range(0, len(state)):
                    node = state[j]
                    if (node == moves[i]):
                        state[j] = 'X'
                    if (node == 0):
                        state[j] = moves[i]
                for j in range(0, len(state)):
                    node = state[j]
                    if (node == 'X'):
                        state[j] = 0
                distance = self.h(state)
                distances.append(distance)
            return  distances

        def getMove(moves, distances):
            # Remove Repetitive values from move
            def repetition(gridMoves, repeatingMoves):
                moves = set(gridMoves) - set(repeatingMoves)
                if (len(moves) == 0):
                    moves = gridMoves
                distances = forecast(list(moves))
                return list(moves), distances

            #detect repetition in moves and make a different move
            if(len(nodes) > 6):
                arrayreverse = nodes[::-1]
                lastFour = []
                for i in range(0, len(arrayreverse)):
                    if (i < 5):
                        lastFour.append(arrayreverse[i])
                    else:
                        #Do Nothing
                        silence = "Silence is Golden"
                arrayString = str(arrayreverse)
                last4Str = str(lastFour).replace('[', '').replace(']', '')
                occurrence = arrayString.count(last4Str)
                if(occurrence > 1):
                    moves, distances = repetition(moves, lastFour)

            shortest = distances[0]
            nextMove = moves[0]

            if(len(moves) > 1):
                for i in range(1, len(distances)):
                    distance = distances[i]
                    if (distance <= shortest):
                        shortest = distances[i]
                        nextMove = moves[i]
                        if (len(nodes) > 0):
                            pop = len(nodes) - 1
                            if (nextMove == nodes[pop]):
                                if(i == (len(distances) - 1)):
                                    shortest = distances[i-1]
                                    nextMove = moves[i-1]
                                else:
                                    shortest = distances[i-1]
                                    nextMove = moves[i-1]

            

            return nextMove

        currentStateArray = returnAsArray(currentState)
        currentPossibleMoves = possibleMoves(currentState)

        if(currentStateArray != goalArray):
            distanceHeuristics = forecast(currentPossibleMoves)
            nextMove = getMove(currentPossibleMoves, distanceHeuristics)
            nodes.append(nextMove)

            self.neighbor(nextMove)

        else:
            print "GOAL!!!!!!!!!!!"
    
    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        # YOU FILL THIS IN
        for i in range(0, len(self.grid)):
            row = self.grid[i]
            for j in range(0, len(row)):
                node = row[j]
                if (node == move):
                    self.grid[i][j] = 0
                if (node == ' '):
                    self.grid[i][j] = 'X'
        for i in range(0, len(self.grid)):
            row = self.grid[i]
            for j in range(0, len(row)):
                node = row[j]
                if (node == 0):
                    self.grid[i][j] = ' '
                if (node == 'X'):
                    self.grid[i][j] = move

        puzzle.display()
        time.sleep(1)
        puzzle.moves()

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
        gridValue = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        distance = 0
        for i in range(0, len(goal)):
            currGrid = goal[i]
            for j in range(0, len(goalArray)):
                if(goal[i] == goalArray[j]):
                    r1 = gridValue[i][0]
                    c1 = gridValue[i][1]
                    r2 = axes[j][0]
                    c2 = axes[j][1]
                    distance += (abs(r1 - r2)) + (abs(c1 - c2))
        return distance

class Agent(object):
    """Knows how to solve a sliding-block puzzle with A* search."""
    
    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN
        print "List of moves to get the puzzle to match the goal: ", nodes
        print "Total steps:\n{}\n\n\n".format(len(nodes))


def main():
    """Create a puzzle, solve it with A*, and console-animate."""

    global puzzle, nodes, axes, goalArray
    nodes = []
    axes = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    goalArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    #puzzle = Puzzle([[3, 1, 4], [2, 7, 6], [5, 8, ' ']])
    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()
    puzzle.moves()

    agent = Agent()
    #orig
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)
    
    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()

if __name__ == '__main__':
    main()
