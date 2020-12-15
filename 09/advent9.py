f=[int(i)for i in open("i.t")]
l,r=len(f),range
u=[f[i]for i in r(25,l)if all([a+b!=f[i]for a in f[i-25:i]for b in f[i-25:i]if a!=b])][0]
print(u,[max(f[i:j])+min(f[i:j])for i in r(l)for j in r(i+1,l)if u==sum(f[i:j])])
