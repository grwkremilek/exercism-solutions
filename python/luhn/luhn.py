class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def is_valid(self):
        if len(self.card_num) <= 1 or ''.join(c for c in self.card_num if not c.isdigit()):
            return False
        numbers = list(map(int, self.card_num))
        semiproduct = []
        for index, num in enumerate(reversed(numbers)):
            if index % 2 != 0:
                num *= 2
                if num > 9:
                    num -= 9
            semiproduct.append(num)
        return sum(semiproduct) % 10 == 0

