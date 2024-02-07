print("Indique quantos numeros da sequencia Fibonacci deseja ver:\n")
num = int(input("-> "))
text = "0 - 1 - "
seq1 = 0
seq2 = 1
result = 0
for i in range(1, num-1):
    result = seq1 + seq2
    seq1 = seq2
    seq2 = result

    if i == num:
        text = text + str(result)
    else:
        text = text + str(result) + " - "

print(f"{text}")
