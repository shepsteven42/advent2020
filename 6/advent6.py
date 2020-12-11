f=[i.split()for i in open('i.t').read().split('\n\n')]
print(sum([(len(set(''.join(i))))for i in f]),sum([len(set(i[0]).intersection(*i))for i in f]))