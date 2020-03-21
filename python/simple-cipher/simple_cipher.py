import random
import string

class Cipher(object):
    def __init__(self, key=None):
        if key == None:
            self.key = ''.join([random.choice(string.ascii_lowercase) for n in range(50)])
        elif key == '' or any(k.isupper() for k in key) or not any(k.isalpha() for k in key):
                raise ValueError("Incorrect input")
        else:
            self.key = key

    def encode(self, text):
        out = []
        for i,c in enumerate(text):
            asc = (ord(c) + ord(self.key[i % len(self.key)]) % 97)
            out.append(chr(asc-26)) if asc>ord("z") else out.append(chr(asc))
        return "".join(out)

    def decode(self, text):
        out = [chr((ord(c)-ord(self.key[i % len(self.key)]))%26+97) for i,c in enumerate(text)]
        return "".join(out)
