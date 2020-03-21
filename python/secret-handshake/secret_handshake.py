d = {   8 : 'jump',
        4 : 'close your eyes',
        2 : 'double blink',
        1 : 'wink'  }

def handshake(code):
    actions = [d[key] for key in d.keys() if code & key == key]
    return actions[::-1] if code < 16 else actions

def secret_code(actions):
    d_reversed = {v:k for k,v in d.items()}
    code = [d_reversed[a] for a in actions]
    return sum(code) if code == sorted(code) else sum(code) + 16
