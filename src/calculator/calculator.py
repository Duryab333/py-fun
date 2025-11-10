class Calculator:
    def __init__(self):
        # language mappings for digits and Roman numerals
        self.mapping = {
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
            # German
            "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
            "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
            # Spanish
            "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
            # Russian (Cyrillic)
            "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
            "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
            # Chinese numerals
            "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
            "六": 6, "七": 7, "八": 8, "九": 9,
            # Roman numerals (upper and lower case)
            "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
            "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
            "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
            "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
        }

    

    # Helper to convert any supported input into a number
    def _to_number(self, x):
        if isinstance(x, (int, float)):
            return x
        s = str(x).strip()
        if s.lower() in self.mapping:
            return self.mapping[s.lower()]
        try:
            return float(s)
        except ValueError:
            return 0.0  # fallback

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
