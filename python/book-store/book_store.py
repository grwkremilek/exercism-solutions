from copy import deepcopy

BOOKCOST = 800
DISCOUNTS = { n_books: n_books * BOOKCOST * discount for
             n_books, discount in enumerate((0, 1, .95, .90, .80, .75)) }

def calculate_total(books):
    groups = []
    for book in books:
        cheap_group = None
        groups.append([])
        for g, group in enumerate(groups):
            if book not in group:
                new_groups = deepcopy(groups)
                new_groups[g].append(book)
                cheap_group = min(new_groups, cheap_group  or new_groups, key=_cost)
        groups = [c for c in cheap_group if c]
    return _cost(groups)

def _cost(groups):
    return sum(DISCOUNTS[len(group)] for group in groups)
