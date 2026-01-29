from calculator import Calculator

class UserInput:
    def __init__(self):
        self._num1 = None
        self._num2 = None
        self._option = None
        self.calc = Calculator()
    
    @property
    def num1(self):
        return self._num1
    
    @num1.setter
    def num1(self, num):
        self._num1 = num

    @property
    def num2(self):
        return self._num2
    
    @num2.setter
    def num2(self, num):
        self._num2 = num

    @property
    def option(self):
        return self._option
    
    @option.setter
    def option(self, num):
        try:
            num = int(num)
            if num <= 5:
                self._option = num
            else:
                print("You have exceed the range of available options")
                self.select_option()
        except ValueError:
            self.select_option()
    
    def select_option(self):
        print(f"{"*"*10}Welcome to Basic Arithmatic Calculator{"*"*10}")
        print("1. Addition")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit Program")
        self.option = input("Please select an option from 1-5: ")
        # print(f"Selected option: {self.option}")
        return self.option
    
    def user_input(self):
        inpt = input("Enter Number: ")
        try:
            inpt = int(inpt)
            return inpt
        except ValueError:
            try:
                inpt = float(inpt)
                return inpt
            except ValueError:
                print("Please select a real number")
                self.user_input()
    
    def set_user_number(self):
        while self.num1 == None or self.num2 == None:
            if self.num1 == None:
                self.num1 = self.user_input()
                self.calc.num1 = self.num1
            else:
                self.num2 = self.user_input()
                self.calc.num2 = self.num2

    def flush_numbers(self):
        self.num1 = None
        self.num2 = None
    
    def match_option(self, option):
        match option:
            case 1: 
                self.set_user_number()
                print(f"Result: {self.calc.add()}")
                self.flush_numbers()
            case 2:
                self.set_user_number()
                print(f"Result: {self.calc.subtract()}")
                self.flush_numbers()
            case 3:
                self.set_user_number()
                print(f"Result: {self.calc.multiply()}")
                self.flush_numbers()
            case 4:
                self.set_user_number()
                if self.calc.division() == -1:
                    self.set_user_number()
                else:
                    print(f"Result: {self.calc.division()}")
                self.flush_numbers()

