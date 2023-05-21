#5_b: To invert keys and values of dict
d = {1: 'abhi', 2: 'magan', 3: 'Chhagan'}
#l1 = d.keys()
#l2 = d.values()
#d = dict(zip(d.values(), d.keys()))
d = dict(map(reversed, d.items()))
print(d)
