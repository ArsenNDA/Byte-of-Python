bri = set(['Brazil', 'India', 'Russia'])

print('India' in bri)
print('USA' in bri)

bric = bri.copy()
bric.add('USA')
bric.add('China')
bric.add('India')

print(bric.issuperset(bri))

bri.remove('India')
print(bri)


# same
print(bri & bric)

print(bri.intersection(bric))