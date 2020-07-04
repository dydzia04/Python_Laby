import sys
if len(sys.argv) < 2:
    print("Podaj przynajmniej 1 parametr!")
else:
    ilosc = 0
    wyrazy = []
    for x in range(1,len(sys.argv)):
        if(len(sys.argv[x])>=3):
            ilosc+=1
            wyrazy.insert(0,sys.argv[x])
    
    print("Ilość argumentów dłuższych lub równych 3 znaki = "+str(ilosc))
    print("Argumenty dłuższe lub równe 3 od końca = "+" ".join(wyrazy))