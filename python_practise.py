# WRONG - All functions remember i=4
acts = []
for i in range(5):
    acts.append(lambda x: i ** x)

print()

#print(acts[0](2))  # Prints 16 (4**2), not 0

# # CORRECT - Use defaults to capture current value
# acts = []
# for i in range(5):
#     acts.append(lambda x, i=i: i ** x)

# print(acts[0](2))  # Prints 0 (0**2)