class Complex():

    def __init__(self, real, imag = 0):
        self.real = real
        self.imag = imag

    def __str__(self):

        if self.imag > 0:
            printable_line = f"{self.real}+{self.imag}j"
        elif self.imag == 0:
            printable_line = f"{self.real}"
        else:
            printable_line = f"{self.real}{self.imag}j"

        return printable_line

    def __add__(self, other):
        add_real = self.real + other.real
        add_imag = self.imag + other.imag
        return Complex(add_real, add_imag)

    def __sub__(self, other):
        sub_real = self.real - other.real
        sub_imag = self.imag - other.imag
        return Complex(sub_real, sub_imag)
    
    def __mul__(self, other):
        mul_real = self.real * other.real - self.imag * other.imag
        mul_imag = self.real * other.imag + self.imag * other.real
        return Complex(mul_real, mul_imag)

    def __truediv__(self, other):
        div_real = (self.real * other.real + self.imag * other.imag)/(other.real**2 + other.imag**2)
        div_imag = (self.imag * other.real - self.real * other.imag)/(other.real**2 + other.imag**2)
        return Complex(div_real, div_imag)


first = Complex(3, 4)
second = Complex(5, -6)

third = first / second

print (third)

#print (first)
