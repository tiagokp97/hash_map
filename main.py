import numpy as np
import time
import statistics
import random
from array_de_5000 import vet as vet_5000
from array_de_20000 import vet as vet_20000
from array_de_100000 import vet as vet_100000
    
M = 1000  # quantidade de arrays
vet = vet_5000 #array a ser buscado

print(f'Modular: {M}')
print(f'Número de registros: {len(vet)}')

def hash_mod(data, M):
    key = data['id'] % M
    return key

def busca_elem(hash_tab, id_to_find):
    inicio = time.time()
    for key, lista in enumerate(hash_tab):
        for i, elem in enumerate(lista):
            if elem['id'] == id_to_find:
                fim = time.time()
                tempo_formatado_ms = (fim - inicio) * 1000
                print('Tempo de execução (ms):', tempo_formatado_ms)
                return key, i
    fim = time.time()
    tempo_formatado_ms = (fim - inicio) * 1000
    print('Tempo de execução (ms):', tempo_formatado_ms)    
    return -1, -1

hash_tab = [[] for _ in range(M)]

for val in vet:
    hash_index = hash_mod(val, M)
    hash_tab[hash_index].append(val)

#Define um elemento aleatório do array para buscar
random = random.choice(vet) 
# Buscando um elemento pelo ID
id_to_search = random['id']
index = busca_elem(hash_tab, id_to_search)

if index != -1:
    print("Elemento encontrado na posição:", index)
else:
    print("Elemento não encontrado.")

sizes = []
for key in range(M):
    if len(hash_tab[key]) > 0:
        sizes.append(len(hash_tab[key]))
        
mean_colisions = statistics.mean(sizes)
print('Média de colisões: ', round(mean_colisions))        
        
      
