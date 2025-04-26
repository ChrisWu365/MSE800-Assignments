input_number = input("Enter a number to check if it is a prime number: ")

class Prime:
    def __init__(self, number):
        self.number = number
        self.is_prime = True

    def it_is_prime(self):
        for i in range(2, self.number):
            s = self.number / i
            if type(i) is int:
                return False
        return True

prime = Prime(int(input_number))

print(f"Is it a prime number: {prime.it_is_prime()}")
