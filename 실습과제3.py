class Stack :
    def __init__( self ):   
        self.top = []       

    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        return str(self.top[::-1])

maze = [['e','0','1','1','1','1','1','1','1','1'],
        ['0','0','0','1','1','1','1','1','1','1'],
        ['0','0','0','0','1','1','1','1','1','1'],
        ['0','1','1','0','0','1','1','1','1','1'],
        ['0','1','0','1','0','0','1','1','1','1'],
        ['0','1','1','1','1','0','0','1','1','1'],
        ['0','1','1','1','1','1','0','0','1','1'],
        ['0','1','1','1','1','1','1','0','0','1'],
        ['0','1','1','1','1','1','1','1','0','0'],
        ['0','0','0','0','0','0','0','0','0','x']]
MAZE_SIZE = 10

def isValidPos(x, y) :		
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False		
    else :			        
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS() :			   
    stack = Stack()		
    stack.push( (0,1) )
    print('DFS: ')

    while not stack.isEmpty(): 	
        here = stack.pop()	    
        print(here, end='->')
        (x, y) = here		     
        if (map[y][x] == 'x') :	
            return True
        else :
            map[y][x] = '.'	
            
            if isValidPos(x, y - 1): stack.push((x, y - 1)) 
            if isValidPos(x, y + 1): stack.push((x, y + 1)) 
            if isValidPos(x - 1, y): stack.push((x - 1, y)) 
            if isValidPos(x + 1, y): stack.push((x + 1, y)) 
        print(' 현재 스택: ', stack)	
    return False	

import copy
map = copy.deepcopy(maze)
result = DFS()
if result : print(" --> 미로탐색 성공")
else : print(" --> 미로탐색 실패")

################################################################################################################
MAX_QSIZE = 10				    
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def enqueue( self, item ):
        if not self.isFull():			            
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		    

    def dequeue( self ):
        if not self.isEmpty():			            
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front]	        

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)


def BFS() :			    	
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')			

    while not que.isEmpty(): 
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.enqueue((x, y - 1))	
            if isValidPos(x, y + 1) : que.enqueue((x, y + 1))	
            if isValidPos(x - 1, y) : que.enqueue((x - 1, y))	
            if isValidPos(x + 1, y) : que.enqueue((x + 1, y))	
    return False

map = copy.deepcopy(maze)
result = BFS()
if result : print(" --> 미로탐색 성공")
else : print(" --> 미로탐색 실패")
####################################################################################################################

class PriorityQueue :
    def __init__( self ):					
        self.items = []						

    def isEmpty( self ):					
        return len( self.items ) == 0
    def size( self ): return len(self.items)
    def clear( self ): self.items = []		

    def enqueue( self, item ):				
        self.items.append( item )			

    def findMaxIndex( self ):				
        if self.isEmpty(): return None
        else:
            highest = 0						
            for i in range(1, self.size()) :
                if self.items[i] > self.items[highest] :
                    highest = i	
            return highest		


    def dequeue( self ):		
        highest = self.findMaxIndex()		
        if highest is not None :
            return self.items.pop(highest)	

    def peek( self ):				
        highest = findMaxIndex()	
        if highest is not None :
            return self.items[highest]	


import math				
(ox,oy) = (5, 4)		
def dist(x,y) :			 
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)	



    def findMaxIndex( self ):		
        if self.isEmpty(): return None
        else:
            highest = 0				
            for i in range(1, self.size()) :	
                if self.items[i][2] > self.items[highest][2] :
                    highest = i		
            return highest			


def MySmartSearch() :				
    q = PriorityQueue()				
    q.enqueue((0,1,-dist(0,1)))		
    print('PQueue: ')
    while not q.isEmpty(): 
        here = q.dequeue()
        print(here[0:2], end='->')	
        x,y,_ = here				
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue((x,y-1, -dist(x,y-1)))
            if isValidPos(x, y + 1) : q.enqueue((x,y+1, -dist(x,y+1)))
            if isValidPos(x - 1, y) : q.enqueue((x-1,y, -dist(x-1,y)))
            if isValidPos(x + 1, y) : q.enqueue((x+1,y, -dist(x+1,y)))
        print('우선순위큐: ', q.items)
    return False
map = copy.deepcopy(maze)
result = MySmartSearch()
if result : print(" --> 미로탐색 성공")
else : print(" --> 미로탐색 실패")