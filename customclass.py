class Rectangle:

    # 1.An instance of the Rectangle class requires length:int and width:int to be initialized.
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
    
    def multiply(self):
        return self.length * self.width
    
    # 2.We can iterate over an instance of the Rectangle class 
    # def __iter__(self):
    #     yield self.length
    #     yield self.width
    
    # 3.When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}



rectangles = Rectangle(length=10, width=20)

print("multiply:", rectangles.multiply())

for rectangle in rectangles:
    print(rectangle)

#  Both __iter__ output deferent

#  1. iter (output)  
#  10 
#  20

# 2. iter (output)  
# {'length': 10}
# {'width': 20}    