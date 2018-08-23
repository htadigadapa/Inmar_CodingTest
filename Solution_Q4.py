

class Sample:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def Add(self):
        return (self.x+self.y)
    

def Addition():
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    s=Sample(a,b)
    print("Sum="+str(s.Add()))

Addition()
