from collections import deque
import numpy as np
import sys

WIDTH_AND_HEIGHT_CHESSBOARD = 8
KNIGHT_MOVEMENTS = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]

def get_random_spots_on_board():
    return np.random.randint(1, WIDTH_AND_HEIGHT_CHESSBOARD+1, size=4)

def solution():
    s = Solution()
    return s._min_steps_to_reach_target()

class Solution:
    def __init__(self):
        random_numbers = get_random_spots_on_board()
        self.KnightPos = [random_numbers[0], random_numbers[1]]
        self.TargetPos = [random_numbers[2], random_numbers[3]]
        print(f'KIGHT POSITION: {self.KnightPos}')
        print(f'TARGET POSITION: {self.TargetPos}')
        self.N = WIDTH_AND_HEIGHT_CHESSBOARD
        self.visited_positions = set()
        self._index_board_0()

    def _index_board_0(self):
        self.source_row = self.KnightPos[0] - 1
        self.source_col = self.KnightPos[1] - 1
        self.target = (self.TargetPos[0] - 1, self.TargetPos[1] - 1)
        self.queue = deque([(self.source_row, self.source_col, 0)])
        
    def _get_first_in_line(self):
        self.row, self.col, self.step = self.queue.popleft()

    def _get_new_position(self):
        self.x = self.dx + self.row
        self.y = self.dy + self.col
        self.new_position = self.x, self.y

    def _validate_boundaries(self):
        self.x_inbound = 0 <= self.x < self.N
        self.y_inbound = 0 <= self.y < self.N

    def _is_move_not_on_board(self) -> bool:
         if not self.x_inbound or not self.y_inbound:
              return True
         return False
    
    def _append_new_position_to_queue(self):
        self.queue.append((self.x, self.y, self.step + 1))

    def _add_new_position_to_positions_visited(self):
        self.visited_positions.add(self.new_position)

    def _min_steps_to_reach_target(self):
        while self.queue:
            self._get_first_in_line()
            if (self.row, self.col) == self.target:
                return self.step
            for dx, dy in KNIGHT_MOVEMENTS:
                self.dx, self.dy = dx, dy
                self._get_new_position()
                self._validate_boundaries()
                if self._is_move_not_on_board():
                        continue
                if self.new_position not in self.visited_positions:
                        self._append_new_position_to_queue()
                        self._add_new_position_to_positions_visited()
	        
if __name__ == '__main__':
    s = solution()
    print(s)
