class grandparent:
    def grandparent(self):
        print("Grandparent's method")
class parent(grandparent):
    def parent(self):
        print("Parent's method")
class child(parent):
    def child(self):
        print("Child's method")
c = child()
c.grandparent()   
c.parent()        
c.child()         
