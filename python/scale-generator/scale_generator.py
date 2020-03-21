class Scale(object):
    sharp_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    
    def __init__(self, tonic):
        self.tonic = tonic
        if self.tonic in ['A', 'B', 'C', 'F#', 'G', 'a', 'f#']:
            ind = self.sharp_scale.index(self.tonic.upper())
            self.tones = self.sharp_scale[ind:] + self.sharp_scale[:ind]
        else:
            ind = self.flat_scale.index(self.tonic.title())
            self.tones = self.flat_scale[ind:] + self.flat_scale[:ind]

    def chromatic(self):
        return self.tones

    def interval(self, intervals):
        result = []
        for i, interv in enumerate(intervals):
            result.append(self.tones[i])
            if interv == 'M':
                del(self.tones[i+1])
            elif interv == 'A':
                del(self.tones[i+1])
                del(self.tones[i+1])
        return result
