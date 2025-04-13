class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        result=self.num1+self.num2
        return result
    def subtraction(self):
        result=self.num1-self.num2
        return result
    def multiplication(self):
        result=self.num1*self.num2
        return result
    def division(self):
        result=self.num1/self.num2
        return result
"""a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
add=Calculator(a,b)
print("The addition for both the numbers is \n\t ", add.addition())
minus=Calculator(a,b)
print("The difference between both the numbers is \n\t ", minus.subtraction())
product=Calculator(a,b)
print("The prpoduct for both numbers is \n\t", product.multiplication())
divide=Calculator(a,b)
print("The division for numbers is \n\t",divide.division())"""