print("SPISAK NAMIRNICA")

racun2=0
def racun():
  print("\nPotrebno je platiit: ", racun2 ,"KM")


spisaknamirnica=['banane','hljeb','mlijeko','jabuke']
cijena={"banane":3,"hljeb":1,"mlijeko":1.5,"jabuke":1.5}
print("\nPotrebno je kupiti: ",end="")

for stvar in spisaknamirnica:
  print(stvar ,end=" ")
for i in range (len(spisaknamirnica)):
  print("\nKupio sam: ", spisaknamirnica[0])
  del spisaknamirnica[0]
  print("Ostale su sljedece namirnice: ", end=" ")
  for stvar in spisaknamirnica:
    print(stvar,end=" ")
  racun2 =+cijena["banane"]+5*cijena["hljeb"]+cijena["mlijeko"]+3*cijena["jabuke"]
while len(spisaknamirnica)<1:
  print("\nKupili ste sve sto je potrebno! ")
  break

racun()
