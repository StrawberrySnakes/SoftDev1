"""Dessa Shapiro"""

def gcd(a, b):  # greatest common divisor
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

class Fraction:
    __slots__ = ["w", "n", "d"]
    def __init__(self, w=0, n=0, d=1):
        # denominator is not zero
        assert d != 0
        self.w = w
        self.n = n
        self.d = d

    def get_fraction(self):
        return self.w, self.n, self.d
    
    def simplify(self):
        improper_numerator = self.n + self.w * self.d

        common_factor = gcd(improper_numerator, self.d)
        improper_numerator //= common_factor
        denominator = self.d // common_factor

        # make it positive
        if denominator < 0:
            improper_numerator *= -1
            denominator *= -1

        # Convert to a mixed fraction
        new_w = improper_numerator // denominator
        new_n = improper_numerator % denominator

        return Fraction(new_w, new_n, denominator)
    
    def add(self, other):
        common_denominator = self.d * other.d // gcd(self.d, other.d)

        self_numerator = self.n + self.w * self.d
        other_numerator = other.n + other.w * other.d

        new_numerator = self_numerator * (common_denominator // self.d) + other_numerator * (common_denominator // other.d)

        return Fraction(0, new_numerator, common_denominator).simplify()
    
    def subtract(self, other):
        common_denominator = self.d * other.d // gcd(self.d, other.d)

        self_numerator = self.n + self.w * self.d
        other_numerator = other.n + other.w * other.d

        new_numerator = self_numerator * (common_denominator // self.d) - other_numerator * (common_denominator // other.d)

        return Fraction(0, new_numerator, common_denominator).simplify()
    
    def __eq__(self, other):
        return self.simplify().get_fraction() == other.simplify().get_fraction()

    def __lt__(self, other):
        return self.simplify().get_fraction() < other.simplify().get_fraction()

    def __le__(self, other):
        return self.simplify().get_fraction() <= other.simplify().get_fraction()

    def __hash__(self):
        return hash(self.simplify().get_fraction())

    def __str__(self):
        return str("<"+str(self.w)+","+str(self.n)+","+str(self.d)+">")
    
def main():
    fraction = Fraction(3, 5, -2)
    print(fraction)
    print(hash(fraction))

if __name__ == "__main__":
    main()