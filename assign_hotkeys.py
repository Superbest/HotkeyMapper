options = [
    'Create blank database',
    'Create sample database',
    'Create sample database',
    'Load existing database',
    'Create empty database'
]

# ---

from collections import OrderedDict
import string

hotkeys = {}

for i in options:
    words = i.lower().split(' ')

    # Letters that begin a word
    heads = ''.join(OrderedDict.fromkeys(''.join([w[0] for w in words])).keys())

    # Other letters
    tails = ''.join(OrderedDict.fromkeys(''.join([w[1:] for w in words])).keys())

    # Pick the hotkey
    all_keys = heads + tails
    best_key = ''
    for c in all_keys:
        if (c in string.ascii_lowercase) and not (c in hotkeys):
            best_key = c
            break

    # Contingency in case no key was found
    #if best_key == '':

    hotkeys[best_key] = i

for k in hotkeys:
    print(k + ':', hotkeys[k])
