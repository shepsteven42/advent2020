d,l=[i for i in[{{'byr':0,'iyr':1,'eyr':2,'hgt':3,'hcl':4,'ecl':5,'pid':6,'cid':7}[n]:v for n,v in[j.split(':')for j in i]}for i in[i.split()for i in open("i.t").read().split("\n\n")]]if all([x in i for x in range(7)])],len
q='0123456789'
print(l(d),l([i for i in d if all(['1920'<=i[0]<='2002','2010'<=i[1]<='2020'<=i[2]<='2030',('150cm'<=i[3]<='193cm'and'cm'in i[3])or('59in'<=i[3]<='76in'and'in'in i[3]),i[4][0]=='#',l(i[4])==7,i[5]in['amb','blu','brn','gry','grn','hzl','oth'],l(i[6])==9]+[k in q for k in i[6]]+[k in q+'abcdef'for k in i[4][1:]])]))
