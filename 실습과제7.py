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


class TNode:								
    def __init__ (self, data, left, right):	
        self.data = data 					
        self.left = left					
        self.right = right					
def preorder(n) :				
    if n is not None :
        print(n.data, end=' ')	
        preorder(n.left)		
        preorder(n.right)		

def inorder(n) :				
    if n is not None :
        inorder(n.left)			
        print(n.data, end=' ')	
        inorder(n.right)		

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root) :
    queue = CircularQueue()			
    queue.enqueue(root)		
    while not queue.isEmpty() :		
        n = queue.dequeue()			
        if n is not None :
            print(n.data, end=' ')	
            queue.enqueue(n.left)	
            queue.enqueue(n.right)	


def count_node(n) :
    if n is None : 
        return 0
    else : 			
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :
    if n is None :	
        return 0
    elif n.left is None and n.right is None :
        return 1
    else : 		
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n) :
    if n is None : 					
        return 0
    hLeft = calc_height(n.left)		
    hRight = calc_height(n.right)	
    if (hLeft > hRight) : 			
        return hLeft + 1
    else: 
        return hRight + 1

def full_tree(root):
    if root.left != None and root.right != None:
        return True
    else:
        return False
def is_complete_binary_tree(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.size != 0 :	
        n = queue.dequeue()
        if not full_tree(root): 
            if n.left == None and n.right == None:
                return False
            else:
                if n.left != None:
                    queue.enqueue(n.left)
                queue.dequeue()
                break
        else:
          queue.enqueue(n.left)
          queue.enqueue(n.right)
          queue.dequeue();
    while queue.size != 0:
        n = queue.dequeue()
        if root.left != None and root.right != None:
            return False
        else:
            return True



def is_balanced(root):
    if root == None:
        return True
    leftheigh = calc_height(root.left)
    rightheigh = calc_height(root.right)
    if (leftheigh - rightheigh <2) and (leftheigh - rightheigh > -1):
        return True
    return False



d = TNode('D', None, None)
b = TNode('B', d, None)
g = TNode('G', None, None)
h = TNode('H',None, None)
e = TNode('E', g,h)
f = TNode('F', None, None)
c = TNode('C', f,e)
root = TNode('A', b, c)

a2 = TNode('A', None, None)
b2 = TNode('B', None, None)
sla = TNode('/', a2, b2)
c2 = TNode('C', None, None)
star = TNode('*', sla, c2)
d2 = TNode('D', None, None)
star2 = TNode('*', star, d2)
e2 = TNode('E', None, None)
root2 = TNode('+', star2, e2)

c3 = TNode('C', None, None)
d3 = TNode('D', None, None)
b3 = TNode('B', c3,d3)
f2 = TNode('F',None, None)
e3 = TNode('E', f2, None)
root3 = TNode('A', b3,e3)

print('\n   In-Order : ', end='')
inorder(root)
print('\n  Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print('\n   In-Order : ', end='')
inorder(root2)
print('\n  Pre-Order : ', end='')
preorder(root2)
print('\n Post-Order : ', end='')
postorder(root2)
print('\nLevel-Order : ', end='')
levelorder(root2)
print()

print('\n   In-Order : ', end='')
inorder(root3)
print('\n  Pre-Order : ', end='')
preorder(root3)
print('\n Post-Order : ', end='')
postorder(root3)
print('\nLevel-Order : ', end='')
levelorder(root3)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 단말의 개수 = %d개" % count_leaf(root))
print(" 트리의 높이 = %d" % calc_height(root))
print()
print(" 노드의 개수 = %d개" % count_node(root2))
print(" 단말의 개수 = %d개" % count_leaf(root2))
print(" 트리의 높이 = %d" % calc_height(root2))
print()
print(" 노드의 개수 = %d개" % count_node(root3))
print(" 단말의 개수 = %d개" % count_leaf(root3))
print(" 트리의 높이 = %d" % calc_height(root3))
print()
if is_complete_binary_tree(root3) == True:
    print('완전 이진 트리입니다.')
else:
    print('완전 이진 트리가 아닙니다.')
print()
if is_balanced(root3) == True:
    print('균형잡힌 트리입니다.')
else:
    print('균형이 안 잡힌 트리입니다.')