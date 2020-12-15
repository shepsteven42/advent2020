f,s=[[int(x[0]),int(x[1]),[i==x[2][0] for i in x[3]]] for x in[x.replace('-',' ').split() for x in open("i.t")]],sum
print(s([x[0]<=s(x[2])<=x[1] for x in f]),s([x[2][x[0]-1]^x[2][x[1]-1] for x in f]))
