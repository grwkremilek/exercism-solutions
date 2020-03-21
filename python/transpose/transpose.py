def transpose(input_lines):
    lines = [l.replace(' ', '_') for l in input_lines.splitlines()]
    lines = [l.ljust(len(max(lines, key=len))) for l in lines]
    lines = [''.join(l) for l in zip(*lines)]
    lines = [l.rstrip().replace('_', ' ') for l in lines]
    return '\n'.join(lines)
