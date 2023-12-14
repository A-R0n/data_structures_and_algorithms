from collections import deque
import numpy as np

def queue_practice():
    random_numbers_list = np.random.randint(100, size=100)
    d = QueuePractice(random_numbers_list)
    
    ##############
    print(f'deque init: {d.d}')
    random_number = np.random.randint(100)
    print(f'random number: {random_number}')
    d._append(random_number)
    print(f'deque after append random number: {d.d}')
    d._appendleft(random_number)
    print(f'deque after append left random number: {d.d}')
    d._remove(random_number)
    print(f'deque after removing random number: {d.d}')
    print(f'Notice our random number got removed at the beginning but not at the end!')
    num_random_num = d._count(random_number)
    print(f'num_random_num {num_random_num}')
    idx_random_num = d._index(random_number)
    print(f'idx_random_num {idx_random_num}')
    
    random_iterable = np.random.randint(5, size=5)
    print(f'random iterable: {random_iterable}')
    d._extend(random_iterable)
    print(f'deque extended: {d.d}')
    d._extendleft(random_iterable)
    print(f'deque extended left: {d.d}')
    print(f'notice that the random iterable is in reverse order...')

    last_in_line = d._pop()
    print(f'last_in_line {last_in_line}')
    first_in_line = d._popleft()
    print(f'first_in_line {first_in_line}')
    print(f'Notice that after we popped these values, they no longer exist in queue')
    d._reverse()
    print(f'reversed queue {d.d}')
    d._rotate()
    print(f'queue rotated {d.d}')
    max_len = d._maxlen()
    print(f'max length queue {max_len}')
    print(f"Notice how we don't have a max length to our queue...")
    d._clear()
    print(f'queue cleared {d.d}')


class QueuePractice:
    def __init__(self, l):
        self.d = deque(l)
        # print(f'deque random numbers {self.d}')
    
    def _append(self, x):
        ## appends random number to right side of deque
        self.d.append(x)

    def _appendleft(self, x):
        ## appends random number to left side of deque
        self.d.appendleft(x)

    def _clear(self):
        ## removes all elements from the deque leaving it with length 0
        self.d.clear()

    def _copy(self):
        return self.d.copy()
    
    def _count(self, x):
        return self.d.count(x)
    
    def _extend(self, myIterable):
        ## extend the right side of the deque by appending elements from the iterable argument
        self.d.extend(myIterable)
    
    def _extendleft(self, myIterable):
        ## Note: this results in reversing the order of elements in the iterable argument
        self.d.extendleft(myIterable)
    
    def _index(self, x):
        ## returns the first position of x in the deque or raises value error
        try:
            index_x = self.d.index(x)
            return index_x
        except ValueError:
            return f'x: {x} does not exist in deque'
        
    def _insert(self, i, x):
        ## inserts x into the deque at positon i
        self.d.insert(i, x)

    def _pop(self):
        ## removes and return an element from the right side of the deque.
        try:
            return self.d.pop()
        except IndexError:
            return "No elements present in deque"

    def _popleft(self):
        try:
            return self.d.popleft()
        except IndexError:
            return "No elements present in deque"
        
    def _remove(self, x):
        ## removes first occurance of value. If not found, raises ValueError
        try:
            self.d.remove(x)
        except ValueError:
            print("Value not found in deque")

    def _reverse(self):
        ## reverses the elements of the deque in-place and then returns None
        self.d.reverse()

    def _rotate(self, n=1):
        self.d.rotate(n)

    def _maxlen(self):
        return self.d.maxlen
    
if __name__ == '__main__':
    queue_practice()