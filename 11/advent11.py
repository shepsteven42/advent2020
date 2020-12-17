f=[i.strip()for i in open('i.t')]
w=len(f[0])
h=len(f)
g=range
m=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def q(f,x,y,a,b):
	while 1:
		x+=a;y+=b
		if any([x<0,y<0,x>=w,y>=h]):return 0
		if'.'!=f[y][x]:return'#'==f[y][x]
def v(f,r):
	n=[''for i in g(h)]
	for x in g(w):
		for y in g(h):o=[sum(f[y+b][x+a]=='#'for a,b in m if w>x+a>=0<=y+b<h),sum(q(f,x,y,a,b)for a,b in m)][r-3];c=f[y][x];n[y]+=[[[c,'L'][o>r],'#'][o<1],c][c=='.']
	return n
for r in[3,4]:
	i=f;j=v(f,r)
	while j!=i:i=j;j=v(j,r)
	print(sum(k=='#'for k in''.join(j)))


