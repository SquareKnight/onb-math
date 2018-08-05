l = []              #Lists
l.append(1)
l.append(2.057)
l.append('lala')
l.append(['a', 'b', 'c'])
l.extend(['a', 'b', 'c'])
print(l)

d = {}              #Dictionaries
d['aardvark'] = 'Creature found on the Veldt'
d['ballerina'] = 'Female dancer specialised in classical music'
d['orca'] = 'Big fish'
print(d)

d['python'] = ['Snake', 'Programming language']
d['orca'] = 'Big sea-dwelling mammal'

for k in d:
    print(k, d[k])


t = (10, 20, 30)        #Tuples
print(t)


s = set([1, 1, 3, 5])   #Sets
print(s)


r = range(10, 20)       #Ranges
print(r)
print(list(r))
