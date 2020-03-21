PROTEINS = {'Methionine'    : ['AUG'],
            'Phenylalanine' : ['UUU', 'UUC'],
            'Leucine'       : ['UUA', 'UUG'],
            'Serine'        : ['UCU', 'UCC', 'UCA', 'UCG'],
            'Tyrosine'      : ['UAU', 'UAC'],
            'Cysteine'      : ['UGU','UGC'],
            'Tryptophan'    : ['UGG'],
            'STOP'          : ['UAA', 'UAG', 'UGA']}

def proteins(strand):
    translations = []
    triplets = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for t in triplets:
        for key, val in PROTEINS.items():
            if t in val:
                translations.append(key)
    for index, trans in enumerate(translations):
        if trans == 'STOP':
            translations = translations[:index]
    return translations
