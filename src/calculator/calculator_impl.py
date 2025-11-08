class Calculator():
    def __init__(self):
        pass

   # Arithmetic operations
    def add(self, a, b): return self._to_number(a) + self._to_number(b)
    def sub(self, a, b): return self._to_number(a) - self._to_number(b)
    def mul(self, a, b): return self._to_number(a) * self._to_number(b)
    def div(self, a, b): return self._to_number(a) / self._to_number(b)

    # Prime factorization
    def factorize(self, n):
        n = int(self._to_number(n))
        i, factors = 2, []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def add(self, a, b):
        a, b = self._to_number(a), self._to_number(b)
        return a + b

    def _to_number(self, x):
        if isinstance(x, (int, float)):
            return x
        try:
            return float(x)
        except ValueError:
            mapping = {
                "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,
                "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
                "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
                "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
                "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
                "三": 3, "四": 4, "五": 5
            }
            return mapping.get(str(x).strip().lower(), 0)

