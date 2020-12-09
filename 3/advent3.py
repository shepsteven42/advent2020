f,t,p=[x.strip()for x in open("i.t")],1,print
for k in[[3,1],[1,1],[5,1],[7,1],[1,2]]:
	y=x=c=0
	while y<len(f):c+=f[y][x%len(f[0])]=='#';y+=k[1];x+=k[0]
	p(c);t*=c
p(t)
