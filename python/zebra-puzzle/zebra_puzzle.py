from constraint import *
problem = Problem()

color = ['red', 'green', 'ivory', 'yellow', 'blue']
pet = ['dog', 'snails', 'fox', 'horse', 'zebra']
drink = ['coffee', 'tea', 'milk', 'orange juice', 'water']
cigs = ['Old Gold', 'Kools', 'Chesterfields', 'Parliaments', 'Lucky Strike']
natio = ['Englishman', 'Ukrainian', 'Spaniard', 'Norwegian', 'Japanese']

criteria = natio + pet + cigs + color + drink
problem.addVariables(criteria,[1,2,3,4,5])

problem.addConstraint(AllDifferentConstraint(), natio)
problem.addConstraint(AllDifferentConstraint(), pet)
problem.addConstraint(AllDifferentConstraint(), cigs)
problem.addConstraint(AllDifferentConstraint(), color)
problem.addConstraint(AllDifferentConstraint(), drink)

problem.addConstraint(lambda e, r: e == r, ["Englishman","red"])
problem.addConstraint(lambda s, d: s == d, ("Spaniard","dog"))
problem.addConstraint(lambda c, g: c == g, ("coffee","green"))
problem.addConstraint(lambda u, t: u == t, ("Ukrainian","tea"))
problem.addConstraint(lambda g, i: g-i == 1, ("green","ivory"))
problem.addConstraint(lambda o, s: o == s, ("Old Gold","snails"))
problem.addConstraint(lambda k, y: k == y, ("Kools","yellow"))
problem.addConstraint(InSetConstraint([3]), ["milk"])
problem.addConstraint(InSetConstraint([1]), ["Norwegian"])
problem.addConstraint(lambda c, f: abs(c-f) == 1, ("Chesterfields","fox"))
problem.addConstraint(lambda k, h: abs(k-h) == 1, ("Kools","horse"))
problem.addConstraint(lambda l, o: l == o, ["Lucky Strike","orange juice"])
problem.addConstraint(lambda j, p: j == p, ["Japanese","Parliaments"])
problem.addConstraint(lambda k, h: abs(k-h) == 1, ("Norwegian","blue"))

solution = problem.getSolutions()[0]

def solve(inp):
    for i in range(1,6):
        house = []
        house.append(str(i))
        for x in solution:
            if solution[x] == i:
                house.append(str(x))
        if inp in house:
            return [v for v in house if v in natio][0]

def drinks_water():
    return solve('water')

def owns_zebra():
    return solve('zebra')
