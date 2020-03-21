def measure(bucket_one, bucket_two, goal, start):
    react, steps = 0, 1
    
    if start == "one":
        full_i, full_r = bucket_one, bucket_two
        inicial = bucket_one
        out = 'one'
    else:
        full_i, full_r = bucket_two, bucket_one
        inicial = bucket_two
        out = 'two'
        
    if inicial == goal:
        return (steps, out, react)
    elif full_r == goal:
        return (steps+1, 'two', inicial)
        
    while True:
        if inicial == full_i and react == 0:
            if full_i <= full_r:
                inicial, react = react, inicial
            else:
                react = full_r
                inicial -= full_r
            steps += 1
        elif react == full_r and 0 < inicial < full_i:
            react = 0
            steps += 1
        elif 0 < inicial <= full_i:
            if react > 0 and inicial + react > full_r:
                inicial -= full_r - react
                react = full_r
                steps += 1
            elif react > 0 and inicial + react <= full_r:
                react += inicial
                inicial = 0
                steps += 1
            elif react == 0 and full_r < inicial:
                react = full_r
                inicial -= full_r
                steps += 1
            elif react == 0 and full_r > inicial:
                react += inicial
                inicial = 0
                steps += 1
        elif inicial == 0:
            inicial = full_i
            steps += 1
        if inicial == goal or react == goal:
            break
    return(steps, out, react)
