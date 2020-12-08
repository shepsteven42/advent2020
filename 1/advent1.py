l,p=[int(x) for x in open("i.t")],print
for i in l:
	for j in [t for t in l if t==2020-i]:
		p(i*j)
for i in l:
	for j in [t for t in l if t<2020-i]:
		for k in [t for t in l if t==2020-i-j]:
			p(i*j*k)
