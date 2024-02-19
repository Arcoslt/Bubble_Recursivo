from random import sample

def mergesort(A, p, r):
    if p < r:
        q = (p + r) // 2 
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r) 

def merge(A, p, q, r): 
    #facilitando a vida
    esquerda = A[p:q + 1]  
    direita = A[q + 1:r + 1] 
    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            A[p + k] = esquerda[i]  # Atualizando o índice correto em A
            i += 1
        else:
            A[p + k] = direita[j]  # Atualizando o índice correto em A
            j += 1
        k += 1

    while i < len(esquerda):
        A[p + k] = esquerda[i]  # Atualizando o índice correto em A
        i += 1
        k += 1
    while j < len(direita):
        A[p + k] = direita[j]  # Atualizando o índice correto em A
        j += 1
        k += 1

def main():
    tamanho = input('Tamanho do Vetor: ')
    tamanho = int(tamanho)
    vet = sample(range(1, tamanho + 1), tamanho)
    print("Vetor desordenado:", vet)
    mergesort(vet, 0, tamanho - 1)  # Passando o índice correto para o tamanho do vetor
    print("Vetor ordenado:", vet)

if __name__ == "__main__":
    main()

