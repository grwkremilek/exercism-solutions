def chain(dominoes):
    if not dominoes:
        return dominoes
    divided_dominoes = [[dominoes[:-1], [dominoes[-1]]]]

    while divided_dominoes:
        group, output = divided_dominoes.pop()
        if not group and output[0][0] == output[-1][1]:
            return output
        for i, domino in enumerate(group):
            if domino[1] != output[0][0]:
                domino = domino[::-1]
            if domino[1] == output[0][0]:
                new_group, new_output = group[:], output[:]
                new_group.pop(i)
                new_output.insert(0, domino)
                divided_dominoes.append([new_group, new_output])
