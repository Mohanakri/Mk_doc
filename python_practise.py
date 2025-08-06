keys = ['app', 'script', 'program']
vals = [1, 3, 5]

# Method 1: Loop
D2 = {}
for (k, v) in zip(keys, vals): 
    D2[k] = v

# Method 2: dict constructor (preferred)
D3 = dict(zip(keys, vals))

# Method 3: Dictionary comprehension
D4 = {k: v for (k, v) in zip(keys, vals)}
print(D2,D3,D4,sep='\n')