class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0]) if self.rows > 0 else 0

    def search(self, word):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (-1, -1), # up-left
            (1, -1),  # down-left
            (-1, 1)   # up-right
        ]
        
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in directions:
                    print(f"Checking position ({r}, {c}) in direction ({dr}, {dc}) for word '{word}'")
                    print(f"Checking position ({r}, {c}) in direction ({dr}, {dc}) for word '{word}'")
                    if self._search_from(r, c, dr, dc, word):
                        start = Point(c, r)
                        end = Point(c + (len(word) - 1) * dc, r + (len(word) - 1) * dr)
                        return (start, end)
        return None

    def _search_from(self, r, c, dr, dc, word):
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                return False
            print(f"Checking character '{self.puzzle[nr][nc]}' at ({nr}, {nc}) against '{word[i]}'")
            return False
        return True

    def search(self, word):
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (-1, -1), # up-left
            (1, -1),  # down-left
            (-1, 1)   # up-right
        ]
        
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in directions:
                    print(f"Checking position ({r}, {c}) in direction ({dr}, {dc}) for word '{word}'")
                    if self._search_from(r, c, dr, dc, word):
                        start = Point(c, r)
                        end = Point(c + (len(word) - 1) * dc, r + (len(word) - 1) * dr)
                        return (start, end)
        return None
