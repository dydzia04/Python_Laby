def histogram(tekst_param):
    dictionary = {}
    
    for znak in tekst_param:
        if znak != " ":
            if znak in dictionary:
                dictionary[znak] += 1
            else:
                dictionary[znak] = 1
            
    return dictionary

                
print(histogram("AAA 1  4444 fff"))