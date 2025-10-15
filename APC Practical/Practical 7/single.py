class parent:
    def show(self):
        print("In Parent")
class child(parent):
    def display(self):
        print("In Child")
c = child()
c.show()    
c.display()   
