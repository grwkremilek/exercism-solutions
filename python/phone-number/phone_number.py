class Phone:
    
    def __init__(self, phone_number):
        self.number = self.format_number(phone_number)
        self.area_code = self.number[:3]
    
    def format_number(self, phone_number):
        formatted_number = ""
        for c in phone_number:
            if c.isdigit():
                formatted_number += c
        if (not 9 < len(formatted_number) < 12) or  formatted_number[-7] in "01":
            raise ValueError("Invalid number!")
        elif len(formatted_number) == 11 and (formatted_number[0] != "1" or formatted_number[1] in "01"):
            raise ValueError("Invalid number!")
        elif len(formatted_number) == 11 and formatted_number[0] == "1":
            formatted_number = formatted_number[1:]
        elif len(formatted_number) == 10 and (formatted_number[0] in "01"):
            raise ValueError("Invalid number!")
        return formatted_number
        
    def pretty(self):
        return "(%s) %s-%s" %(self.number[:3], self.number[3:6], self.number[6:])
