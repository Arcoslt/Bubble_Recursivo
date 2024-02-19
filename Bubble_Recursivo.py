from random import sample

def mergesort(A,p,r)
    if p<r:
        q = (p+r)/2
        #mergesort(Array da esqueda)
        mergesort(A,p,q)
        #mergesort(Array da direita)
        mergesort(A,q+1,r)
        
        merge(A,p,q,r)
        
def merge(A, p, q, r):
    
    # Facilitando a vida
    esquerda = A[p:q + 1]  
    direita = A[q + 1:r + 1] 
    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            A[p + k] = esquerda[i]  
            i += 1
        else:
            A[p + k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        A[p + k] = esquerda[i]
        i += 1
        k += 1
    while j < len(direita):
        A[p + k] = direita[j]  
        j += 1
        k += 1

def main():
    #Criação do vetor com tamanho desejado e com inteiros aleatórios
    tamanho = input('Tamanho do Vetor: ')
    tamanho = int(tamanho)
    vet = []
    #Sample não repete números, fica mais fácil a visualização dop Bubble
    vet = sample(range(1, tamanho + 1), tamanho)
    print("Vetor desordenado:",vet)

    print("Vetor ordenado:",vet)

if __name__ == "__main__":
    main()
