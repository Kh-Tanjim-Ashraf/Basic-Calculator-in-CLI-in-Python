class Calculator:
    def __init__(self):
        self._num1 = None
        self._num2 = None

    @property
    def num1(self):
        return self._num1
    
    @num1.setter
    def num1(self, num1):
        self._num1 = num1
    
    @property
    def num2(self):
        return self._num2
    
    @num2.setter
    def num2(self, num2):
        self._num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2

    def division(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return -1
    