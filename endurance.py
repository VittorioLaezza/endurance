print("inseirisci carburante e consumo orario per calcolare tempo di volo")

g=input("galloni:")
g=int(g)

c=input("consumo\h:")
c=int(c)
r=g/c


h=int(r) #ore

r=(r-h)*60
m=int(r)  #minuti

s=(r-m)*60
s=int(s) #secondi




print("il consumo è",h,"h",m,"m",s,"s")