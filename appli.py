import re

with open('20200527152905.861802.ig.tum', 'r') as fr:
        #lire les lignes
    lines = fr.read()
    
motif = r"(M.*)(?<!RC)SUVValue = (\d+\.\d+)"
resultat = re.findall(motif, lines)

d = {el[0]: float(el[1]) for el in resultat}
print(d)

