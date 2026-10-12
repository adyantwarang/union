set1 = {'Q', 'S', 'D', 'Z', 'X'}
set2 = {'S', 'P', 'R', 'B', 'H', 'Z'}

union = set1.union(set2)
totalguests = list(union)

print("Total guests are: ", len(totalguests))
print("Guests list: ", totalguests)
