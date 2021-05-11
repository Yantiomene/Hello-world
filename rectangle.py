from math import sqrt

def is_rectangle(a, b, c, d, e):
    dico = {}
    
    liste = [a, b, c, d, e]
    liste.sort() # we sort the list to find smalest values
    
    #here we find the width and the length depending on the dimensions
    if liste[0] >= 1:
        dico["width"] = liste[0]
        dico["length"] = liste[1]
    else:
        dico["length"] = liste[2]
        if liste[2] > 1:
            dico["width"] = liste[0]
        else:
            dico["width"] = liste[1]
    
    # We calculate the diag the area and the perimeter for these value of length and width
    diag= sqrt(dico["width"] ** 2 + dico["length"] ** 2)
    diag = round(diag, 2) #round permet d'arrondir les valeurs calculées afin de ne pas manquer des matchs compte tenu de la precision de la machine
    
    
    
    area = dico["width"] * dico["length"]
    area = round(area, 2)
    
    perim = 2*(dico["width"] + dico["length"])
    perim = round(perim, 2)
    
    
   
    #we check if they match in the rest of list elements
    if diag in liste:
        dico["diagonal"] = diag
    if perim in liste:
        dico["perimeter"] = perim
    if area in liste:
        dico["area"] = area
    
    if (not ("diagonal" in dico.keys())) | (not ("perimeter" in dico.keys())) | (not ("area" in dico.keys())) :
        
        print("It is not a rectangle")
        return {}
    
    else: 
        print("It is a rectangle")
        return dico
    
print(is_rectangle(0.1, 0.2, round(sqrt(0.05), 2), 0.6, 0.02))
print(is_rectangle(0.5, 2, round(sqrt(4.25), 2), 5, 1))
print(is_rectangle(2, 3, round(sqrt(13), 2), 10, 6))
