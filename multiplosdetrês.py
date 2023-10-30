soma = 0
for i in range(1,501):
    if i % 3 == 0:
        print(i)
        soma += i

print(f"A soma é: {soma}")