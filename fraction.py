class Fraction:
    def __init__(self, arg1, arg2):
        if type(arg1) == str:
            exp = arg1
            slash_loc = exp.find('/')
            try:
                self.num = int(exp[slash_loc:])
                self.denom = int(exp[:slash_loc+1])
            except ValueError:
                raise ValueError("Error during conversion to fraction")
        elif type(arg1) == int and type(arg2) == int:
            self.num = arg1
            self.denom = arg2
        else:
            raise ValueError("Invalid type for fraction")

    def value(self):
        if self.denom % self.num == 0:
            return self.num // self.denom
        else:
            return self.num / self.denom

    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            return self.value() == other
        num_ratio, num_rem = divmod(other.num, self.num)
        denom_ratio, denom_rem = divmod(other.num, self.num)
        if num_rem == 0 and denom_rem == 0 and num_ratio == denom_ratio:
            return True
        else:
            return self.num == other.num and self.denom == other.denom

    def __add__(self, other):
        if type(other) == Fraction:
            if self.denom == other.denom:
                return Fraction(self.num + other.num, self.denom)
            else:
                common_denom = self.denom * other.denom
                self_ratio = common_denom // self.denom
                other_ratio = common_denom // other.denom
                return Fraction(self.num * self_ratio + other.num * other_ratio, common_denom)
        if type(other) == int:
            return Fraction(self.num + other * self.denom, self.denom)
        raise ValueError("Invalid fraction operation")

    def __sub__(self, other):
        if type(other) == Fraction:
            if self.denom == other.denom:
                return Fraction(self.num - other.num, self.denom)
            else:
                common_denom = self.denom * other.denom
                self_ratio = common_denom // self.denom
                other_ratio = common_denom // other.denom
                return Fraction(self.num * other_ratio - other.num * self_ratio, common_denom)
        if type(other) == int:
            return Fraction(self.num - other * self.denom, self.denom)
        raise ValueError("Invalid fraction operation")

    def __mul__(self, other):
        if type(other) == Fraction:
            return Fraction(self.num * other.num, self.denom * other.denom)
        if type(other) == int:
            return Fraction(self.num * other, self.denom)
        raise ValueError("Invalid fraction operation")

    def __div__(self, other):
        other = Fraction(other.denom, other.num)
        return self * other

    def __str__(self):
        return f"{self.num}/{self.denom}"