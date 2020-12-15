g=sorted(int(i)for i in open('i.t'))
m=max(g)+3;g+=[m];f=[0]+g;w={0:1}
for i in g:w[i]=sum(w[k]for k in w if 0<i-k<4)
a=[sum(j-i==k for i,j in zip(f,g))for k in[1,3]]
print(a[0]*a[1],w[m])