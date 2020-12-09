l=[int(x) for x in open("i.t")]
print([i*j for i in l for j in l if i+j==2020],[i*j*k for i in l for j in l for k in l if i+j+k==2020])
