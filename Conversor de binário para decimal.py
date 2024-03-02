n=input("Digite um número em binário: ")
p=len(n)
C=1
c=0
while p>0:
	p=p-1
	if n[p]=="1":
		c=c+C
	C=C*2
print(c)