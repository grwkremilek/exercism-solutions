import re

def grep(pattern, files, flags=''):
    final_results = []
    for fil in files:
        with open(fil) as f:
            res = []
            for ind, line in enumerate(f.readlines(), 1):
                if (flags == '' and re.search(pattern, line)) or (flags == "-i" and re.search(pattern, line, flags = re.I)):
                    if len(files) > 1:
                        res.append(fil + ":" + line)
                    else:
                        res.append(line)
                elif "-l" in flags and re.search(pattern, line, flags = re.I):
                    if fil + "\n" not in res:
                        res.append(fil + "\n")
                elif "-v" in flags and pattern not in line:
                    if len(files) > 1:
                        res.append(fil + ":" + line)
                        continue
                    else:
                        res.append(line)        
                elif "-v" not in flags:
                    if "-i" in flags and re.search(pattern, line, flags = re.I):
                        m = match_xn(pattern, line, ind, flags)
                        if len(files) > 1:
                            res.append(fil + ":" + m)
                        else:
                            res.append(m)
                    elif "-i" not in flags and re.search(pattern, line):
                        m = match_xn(pattern, line, ind, flags)
                        if len(files) > 1:
                            res.append(fil + ":" + m)
                        else:
                            res.append(m)
        final_results += res
    return ''.join(final_results)

def match_xn(pattern, line, ind, flags):
    semi_res = []
    for f in flags.split(' '):
        if f == '-x' and pattern + "\n" == line:
            if not semi_res:
                semi_res.append(line)
        elif f == '-n':
            if not semi_res:
                semi_res.append(str(ind) + ':' + line)
            else:
                semi_res.append(str(ind) + ':' + semi_res)
    return ''.join(semi_res)


