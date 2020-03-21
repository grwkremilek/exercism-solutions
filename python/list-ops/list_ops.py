import operator

def append(xs, ys):
    return xs + ys

def concat(lists):
    return [i for sub in lists for i in sub]

def filter_clone(function, xs):
    return [i for i in xs if function(i)]

def length(xs):
    return sum(1 for x in xs)

def map_clone(function, xs):
    return [function(x) for x in xs]

def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc

def foldr(function, xs, acc):
     return foldl(lambda x, acc: function(acc, x), reverse(xs), acc)

def reverse(xs):
    return foldl(lambda acc, x: append([x], acc), xs, [])
