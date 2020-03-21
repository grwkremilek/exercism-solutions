def tally(tournament_results):
    firstline = ('{:30s} | MP |  W |  D |  L |  P'.format('Team'))    
    if tournament_results == '':
        return firstline
    teams = {}
    for line in tournament_results.split('\n'):
        team1, team2, res = line.split(';')
        for t in [team1, team2]:
            if t not in teams:
                teams[t] = {'MP' : 1, 'W' : 0, 'D' : 0, 'L' : 0, 'P' : 0}
            else:
                teams[t]['MP'] += 1
        if res == 'win':
            teams[team1]['W'] += 1
            teams[team2]['L'] += 1
            teams[team1]['P'] += 3
        if res == 'loss':
            teams[team2]['W'] += 1
            teams[team1]['L'] += 1
            teams[team2]['P'] += 3
        if res == 'draw':
            for t in [team1, team2]:
                teams[t]['D'] += 1
                teams[t]['P'] += 1
    sorted_teams = (sorted(teams.items(), key=lambda x: (-x[1]['P'], x[0])))
    table = ['{name:30} | {MP:2} | {W:2} | {D:2} | {L:2} | {P:2}'.format(name=name, **res) for name, res in sorted_teams ]
    return firstline + '\n' + '\n'.join(table)
