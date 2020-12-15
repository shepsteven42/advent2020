f,q,p=[x.strip()for x in open("i.t")],1,print
for a,b in zip([3,1,5,7,1],[1,1,1,1,2]):
	t=c=0
	while b*t<len(f):c+=f[b*t][a*t%len(f[0])]=='#';t+=1
	p(c);q*=c
p(q)
