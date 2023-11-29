#============================================ Primero ============================================#
"""
def rob(hab, mon, c):
    q = sum(mon)//hab
    if sum(mon)%hab != 0: return 'Imposible'
    if mon.count(q) != len(mon):
        z = max(mon) - q
        p = z
        mon[mon.index(max(mon))] -= z
        while mon[mon.index(min(mon))] + p > q:
            p -= q - min(mon)
            mon[mon.index(min(mon))] += q - min(mon)
        mon[mon.index(min(mon))] += p
        return rob(hab, mon, c + z)
    return c
print(rob(int(input()), [int(i) for i in input().split()], 0))
"""
#============================================ Segundo ============================================#

juga, juga_ord = {} , {}

for _ in range(int(input())):
    n = input().split()
    n[1] , n[2] = int(n[1]) , str((n[2] + ' ' + n[3]) if len(n) == 4 else n[2])
    if len(n) == 4: n.pop(3)
    if n[2] not in juga:
        juga[n[2]] = {'Australia':[], 'RolandGarros':[], 'USOpen':[], 'Wimbledon':[]}
    juga[n[2]][n[0]].append(n[1])

for i in sorted(juga.keys()):
    juga_ord[i] = juga[i]

for i in juga_ord:
    for j in juga_ord[i].keys():
        juga_ord[i][j].sort()

for i in juga_ord:
    print(i)
    for j in juga_ord[i]:
        juga_ord[i][j] = [str(h) for h in juga_ord[i][j]]
        print(j, ' '.join(juga_ord[i][j]))

#============================================ Tercero ============================================#

def cadena(n, lista):
    mat = []
    if len(lista) == n:
        return 1
    else:
        for i in range(len(lista)):
            mat.append([])
            l = lista
            l.insert(i, 0)
            mat[i].append(l)
    return mat
a = input().split()
n , k = int(a[0]) , int(a[1])
print(cadena(n, [1 for _ in range(k)]))