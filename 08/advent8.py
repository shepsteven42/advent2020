f=[i.split()for i in open("i.t")];l=len(f)
def e(f):
	p=a=0;v=[];
	while(p not in v and p<l):v+=[p];c,n=f[p][0][0],int(f[p][1]);p+=[1,n][c=='j'];a+=[0,n][c=='a']
	return p,a
print(e(f),[i for i in[e(f[:i]+[({'a':'a','n':'j','j':'n'}[f[i][0][0]],f[i][1])]+f[i+1:])for i in range(l)]if i[0]==l])
