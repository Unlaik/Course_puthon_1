Genome = input()
Guanin= Genome.upper().count("g".upper())
Citozin= Genome.upper().count("c".upper())
NumbersInString=(len(Genome))
GC=Guanin+Citozin
ParcentInGenome=(GC/NumbersInString)*100
print(ParcentInGenome)