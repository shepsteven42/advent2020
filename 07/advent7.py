g={j[0]+j[1]:{j[i+1]+j[i+2]:int(0 if j[i]=='no'else j[i])for i in range(4,len(j),4)}for j in[i.split()for i in open('i.t')]}
s,o='shinygold','otherbags.'
f=lambda i:any([f(k)for k in g[i] if k!=o]+[i==s])
c=lambda i:sum(g[i][k]*(c(k)+1)for k in g[i]if k!=o)
print(sum(f(i)for i in g if i!=s),c(s))
