import itertools

def maximum_value(maximum_weight, items):
    if items == [] or all(d['weight'] > maximum_weight for d in items):
        return 0
    all_values = []
    for comb in range(0, len(items)+1):
        for subset in itertools.combinations(items, comb):
            weights, values = 0,0
            for d in subset:
                values += d['value']
                weights += d['weight']
            if weights <= maximum_weight:
                all_values.append(values)
    return max(all_values)
    


