g,s,o={i[0][:2]+i[1][:4]:{i[k+1][:2]+i[k+2][:4]:int(0 if i[k]=='no'else i[k])for k in range(4,len(i),4)}for i in[j.translate({44:None,46:None}).split()for j in open('i.t')]},'shgold','otbags'
f=lambda i:any([f(k)for k in g[i] if k!=o]+[i==s])
c=lambda i:sum(g[i][k]*(c(k)+1)for k in g[i]if k!=o)
print(sum([f(i)for i in g if i!=s]),c(s))