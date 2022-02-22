class Minus:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def sum(self):
        """
        :returns substract of two numbers
        """
        return self.num_1 - self.num_2


operation = Minus(5, 2)
print(operation.sum())