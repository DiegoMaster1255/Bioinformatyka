
# leci po tablicy odległości i szuka następnego słowa, po czym dopisuje ostatnią literę
def checkNext(index, dist, dna, result):
    for j in range(len(dist[index])):
        if dist[index][j] == 9:
            result += dna[j][len(dna[j]) - 1]
            result = checkNext(j, dist, dna, result)
            break
    return result

def checkPrev(index, distPrev, dna, result):
    for j in range(len(dist[index])):
        if distPrev[index][j] == 9:
            result = dna[j][0] + result
            result = checkPrev(j, distPrev, dna, result)
            break
    return result


file = open("temp.txt", "r")

dna = file.readlines()



# Usunięcie \n z końca każdego słowa
for i in range(len(dna) - 1):
    dna[i] = dna[i][:-1]
print(dna)

dist = [[0 for i in range(len(dna))] for j in range(len(dna))]

index = 0
#porównuje każde słowo z każdym, wyliczając maksymalne pokrycie
for d1 in dna:
    count = 0
    for d2 in dna:
        for i in range(len(d1)):
            # jeśli litera pokrywa się z pierwszą literą drugiego słowa, zaczyna sprawdzać ile kolejnych też się pokrywa
            if d1[i] == d2[0]:
                current = 1
                for j in range(i+1, len(d1)):
                    if d1[j] == d2[current]:
                        current += 1
                    else:
                        if dist[index][count] < current:
                            dist[index][count] = current
                        break
                if dist[index][count] < current:
                    dist[index][count] = current
        count += 1
    index += 1

print(dist)

distPrev = [[0 for i in range(len(dna))] for j in range(len(dna))]

print(len(d1))

index = 0
#porównuje każde słowo z każdym, wyliczając maksymalne pokrycie
for d1 in dna:
    count = 0
    for d2 in dna:
        for i in range(len(d1) - 1, -1, -1):
            # jeśli litera pokrywa się z pierwszą literą drugiego słowa, zaczyna sprawdzać ile kolejnych też się pokrywa
            if d1[i] == d2[len(d2) - 1]:
                current = 1
                for j in range(i-1, -1, -1):
                    if d1[j] == d2[len(d2) - 1 - current]:
                        current += 1
                    else:
                        if distPrev[index][count] < current:
                            distPrev[index][count] = current
                        break
                if distPrev[index][count] < current:
                    distPrev[index][count] = current
        count += 1
    index += 1

print(distPrev)


result = dna[0]
result = checkNext(0, dist, dna, result)
print(result)

result = checkPrev(0, distPrev, dna, result)

print(result)
