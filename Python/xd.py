personas = {
    'jano':4,
    'tomas':3,
    'richi':4,
    'dani': 4,
    'julian': 3,
    'juanda 1': 3,
    'juanda 2': 3,
    'sneheider': 3,
    
}
paga = 8
p_pagan = []
for i in personas:
    if personas[i] > 3:
        p_pagan.append(i)
paga_persona = paga/len(p_pagan)
print(f' {p_pagan} entre los {len(p_pagan)} pagan {paga_persona:.2f} millones cada uno')