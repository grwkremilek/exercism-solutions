from enum import Flag, auto
    
class Allergies:
    
    class Allergens(Flag):
        EGGS = auto()
        PEANUTS = auto()
        SHELLFISH = auto()
        STRAWBERRIES = auto()
        TOMATOES = auto()
        CHOCOLATE = auto()
        POLLEN = auto()
        CATS = auto()

    def __init__(self, score):
        self.lst = [allergy.name.lower() for allergy in Allergies.Allergens if allergy.value & score]
        
    def is_allergic_to(self, allergy):
        return allergy in self.lst
