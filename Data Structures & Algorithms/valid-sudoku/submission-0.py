import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # Create our empty VIP clubs (Sets)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Key will be a tuple: (r//3, c//3)
        
        # Loop through every single cell on the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # If the cell is empty, skip it
                if val == ".":
                    continue
                    
                # THE BOUNCER CHECK
                # If this number is already in the current row's set, 
                # column's set, or square's set, the Sudoku is invalid!
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                    
                # If it's a new number, add it to all 3 VIP clubs so we remember it
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                
        # If we checked the whole board and found no duplicates, it's valid!
        return True