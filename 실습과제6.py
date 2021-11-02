class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	

    def display(self, msg):		
        print(msg, self.items)	

    def contains(self, item) :
        return item in self.items

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)

    def insert(self, elem) :                
        if elem in self.items : return      
        for idx in range(len(self.items)) : 
            if elem < self.items[idx] :     
                self.items.insert(idx, elem)
                return
        self.items.append(elem)             

    def __eq__( self, setB ):       	
        if self.size() != setB.size() :	
            return False
        for idx in range(len(self.items)): 			
            if self.items[idx] != setB.items[idx] :	
                return False
        return True

    def union( self, setB ):        	
        newSet = Set()					
        a = 0							
        b = 0							
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            if valueA < valueB :		
                newSet.items.append( valueA )	
                a += 1					
            elif valueA > valueB :		
                newSet.items.append( valueB )	
                b += 1			
            else : 				
                newSet.items.append( valueA )	
                a += 1					
                b += 1
        while a < len( self.items ):	
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :	
             newSet.items.append( setB.items[b] )
             b += 1
        return newSet
    
    def intersect(self, selfB):
        newSet = Set()
        a= 0
        b= 0
        listA = []
        listB = []
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            listA.append(valueA)
            listB.append(valueB)
            a+=1
            b+=1
        while a < len( self.items ):	
             listA.append( self.items[a] )
             a += 1
        while b < len( setB.items) :	
             listB.append( setB.items[b] )
             b += 1
        for ch in listB:
            if ch in listA:
                newSet.items.append(ch)
        return newSet
    def difference(self, selfB):
        newSet = Set()
        a= 0
        b= 0
        listA = []
        listB = []
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]		
            valueB = setB.items[b]		
            listA.append(valueA)
            listB.append(valueB)
            a+=1
            b+=1
        while a < len( self.items ):	
             listA.append( self.items[a] )
             a += 1
        while b < len( setB.items) :	
             listB.append( setB.items[b] )
             b += 1
        for ch in listA:
            if ch not in listB:
                newSet.items.append(ch)
        return newSet
setA = Set()
setA.insert("휴대폰")
setA.insert("지갑")
setA.insert("손수건")
setA.display('SetA : ')

setB =Set()
setB.insert("빗")
setB.insert("파이썬 자료구조")
setB.insert("야구공")
setB.insert("지갑")
setB.display('SetB : ')

setB.insert("빗")
setA.delete("손수건")
setA.display('SetA : ')
setB.display('SetB : ')

setA.union(setB).display('A U B : ')
setA.intersect(setB).display('A ^ B : ')
setA.difference(setB).display('A - B : ')