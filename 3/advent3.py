f,a,t,p=[x.strip() for x in open("i.t")],[[1,1],[3,1],[5,1],[7,1],[1,2]],1,print
for k in a:
	y=x=c=0
	while y<len(f):
		c+=[0,1][f[y][x%len(f[0])]=='#']
		y+=k[1]
		x+=k[0]
	p(c)
	t*=c
p(t)