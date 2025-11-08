# num_converter.py

class NumConverter:
    def __init__(self):
        self.mapping = {
            # English words
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            # Roman numerals
            "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
            "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
            # Spanish
            "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
            # Russian
            "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
            # Chinese (example)
            "三": 3, "四": 4, "五": 5
        }

    def to_number(self, value):
        """Convert value (string, int, float, or word) to a number."""
        if isinstance(value, (int, float)):
            return value

        try:
            return float(value)
        except (ValueError, TypeError):
            val = str(value).strip().lower()
            if val in self.mapping:
                return self.mapping[val]
            raise ValueError(f"Invalid numeric value: {value}")
