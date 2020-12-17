x=y=w=z=0;s=10;t=d=1
for a,n in[({a:b for a,b in zip('NESWFLR',range(7))}[i[0]],int(i[1:]))for i in open('i.t')]:
	b=a<4
	if a>5:n=360-n
	if a>4:
		d=(d-n/90)%4
		while n:p=s;s=-t;t=p;n-=90
	if a>3:a=d;w+=s*n;z+=t*n
	if a>1:n=-n
	if(1+a)%2:y+=n;t+=n*b
	if a%2:x+=n;s+=n*b
a=abs;print(a(x)+a(y),a(w)+a(z))