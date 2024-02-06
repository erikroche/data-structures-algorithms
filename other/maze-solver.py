from typing import List

class Point:

def walk(maze: List(str), wall: str, curr, end, seen: List[bool][bool]) -> bool:
    # base cases
    # off the map
    if (curr.x < 0 or curr.x >= maze[0].length) or (curr.y < 0 or curr.y >= maze.length):
        return False
    
    # on a wall
    if maze[curr.y][curr.x] == wall:
        return False
    
    # at the end
    if curr.x == end.x and curr.y == end.y:
        return True
    
    if seen[curr.y][curr.x]:
        return False


def solve(maze: List(str), wall: str, start, end ) -> List():
