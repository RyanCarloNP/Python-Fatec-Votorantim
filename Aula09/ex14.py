matriz = []
print("Digite os elementos da matriz 8x8:")
for i in range(8):
    linha=[]
    for j in range(8):
        elemento=int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
simetrica=True
for i in range(8):
    for j in range(8):
        if matriz[i][j]!=matriz[j][i]:
            simetrica=False
            break
    if not simetrica:
        break
if simetrica:
    print("\nA matriz é simétrica.")
else:
    print("\nA matriz não é simétrica.")