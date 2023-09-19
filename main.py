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

def busca_elem(hash_tab, ids_to_find):
    resultados = []
    inicio = time.time()
    
    for id_to_find in ids_to_find:
        encontrado = False
        for key, lista in enumerate(hash_tab):
            for i, elem in enumerate(lista):
                if elem['id'] == id_to_find:
                    resultados.append((id_to_find, key, i))
                    encontrado = True
                    break
            if encontrado:
                break
        else:
            resultados.append((id_to_find, -1, -1))

    fim = time.time()
    tempo_formatado_ms = (fim - inicio) * 1000
    print(f'Tempo necessário para buscar 100 números, {tempo_formatado_ms}(ms):')    
    return resultados, tempo_formatado_ms

hash_tab = [[] for _ in range(M)]

for val in vet:
    hash_index = hash_mod(val, M)
    hash_tab[hash_index].append(val)

#Define diversos elementos aleatórios do do array para buscar
ids_to_search = [random.choice(vet)['id'] for _ in range(100)]

# Buscando múltiplos elementos pelos IDs
searche_calls = 5

searches = [busca_elem(hash_tab, ids_to_search) for _ in range(searche_calls)]
times = [search[1] for search in searches]

mean_searches_time = statistics.mean(times)
print(f'Média de tempo de busca {mean_searches_time}')


sizes = []
for key in range(M):
    if len(hash_tab[key]) > 0:
        sizes.append(len(hash_tab[key]))
        
mean_colisions = statistics.mean(sizes)
print('Média de colisões: ', round(mean_colisions))        
        
      
