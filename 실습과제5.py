class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link

class LinkedList:			
    def __init__( self ):			
        self.head = None			

    def isEmpty( self ): return self.head == None	
    def clear( self ) : self.head = None		    

    def size( self ):			
        node = self.head		
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedList:'): 
        print(msg, end='')		        
        node = self.head			    
        while not node == None :		
            print(node.data, end=' ')	
            node = node.link		    
        print()

    def getNode(self, pos) :		     
        if pos < 0 : return None
        node = self.head;			     
        while pos > 0 and node != None :
            node = node.link		     
            pos -= 1			         
        return node	

    def getEntry(self, pos) :		    
        node = self.getNode(pos)		
        if node == None : return None	
        else : return node.data		    

    def replace(self, pos, elem) :	    
        node = self.getNode(pos)		
        if node != None: node.data = elem	

    def find(self, data) :		    
        node = self.head;
        while node is not None:		
            if node.data == data : return node	
            node = node.link
        return node			

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)		    
        if before == None :         		    
            self.head = Node(elem, self.head)	
        else :					                
            node = Node(elem, before.link)		
            before.link = node		


    def delete(self, pos) :
        before = self.getNode(pos-1)		
        if before == None :         		
            if self.head is not None :		
                self.head = self.head.link	
        elif before.link != None :		    
            before.link = before.link.link	


class Term:
    def __init__(self, expon, coeff):
        self.expon = expon
        self.coeff = coeff
class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()
    def degree(self):
        if self.head == None : return 0
        else : return self.head.data.expon
    def display(self, msg = ""):
        print("\t", msg, end = '')

        node = self.head
        while node is not None:
            print("%5.1f x^%d + " % (node.data.coeff, node.data.expon), end = '')
            node = node.link
        print()
    def read(self):
        self.clear()
        while True:
            token = input("계수 차수 입력(종료:-1): ").split(" ")
            if token[0] == '-1':
                self.display("입력 다항식: ")
                return 
            self.insert(self.size(), Term(int(token[1]), float(token[0])))
    def add(self, b):
        nodea = self.head
        nodeb = b.head
        sum = 0
        p  = SparsePoly()
        while nodea and nodeb:
            if(nodea.data.expon == nodeb.data.expon):
                sum = nodea.data.coeff + nodeb.data.coeff
                p.insert(p.size(), Term(int(nodea.data.expon), float(sum)))
                nodea = nodea.link
                nodeb = nodeb.link
            elif(nodea.data.expon > nodeb.data.expon):
                p.insert(p.size(), Term(int(nodea.data.expon), float(nodea.data.coeff)))
                nodea = nodea.link
            else:
                p.insert(p.size(), Term(int(nodeb.data.expon), float(nodeb.data.coeff)))
                nodeb = nodeb.link
        while nodea is not None:
            p.insert(p.size(), Term(int(nodea.data.expon), float(nodea.data.coeff)))
            nodea = nodea.link
        while nodeb is not None:
            p.insert(p.size(), Term(int(nodeb.data.expon), float(nodeb.data.coeff)))
            nodeb = nodeb.link

        return p
        
a = SparsePoly()
b = SparsePoly()
a.read()
b.read()
c = a.add(b)
a.display(" A = ")
b.display(" B = ")
c.display(" C = ")