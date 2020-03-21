def encode(numbers):
    out = []
    for number in numbers[::-1]:
        out.insert(0, 0x00)
        while number:
            out[0] |= number & (0x80 - 1)
            number >>= 7
            if number > 0:
                out.insert(0, 0x80)
    return out


def decode(bytes_):
    out = []
    value = 0
    for byte in bytes_:
        value = (value << 7) | byte & ~(0x80)
        if byte & 0x80 <= 0:
            out.append(value)
            value = 0
    if byte & 0x80:
        raise ValueError('Incomplete sequence')
    return out
