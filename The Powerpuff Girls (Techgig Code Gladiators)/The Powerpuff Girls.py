n = int(input())

quantity_in = list(map(int, input().split()))
quantity_in = quantity_in[:n]

quantity_lab = list(map(int, input().split()))
quantity_lab = quantity_lab[:n]

ppg = []

for i in range(n):
    val = int(quantity_lab[i] / quantity_in[i])
    ppg.append(val)
    
print(min(ppg))    