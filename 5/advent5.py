f=[int(i.translate({66:49,70:48,76:48,82:49}),2) for i in open('i.t')]
print(max(f),[x for x in range(min(f),max(f)+1) if x not in f])