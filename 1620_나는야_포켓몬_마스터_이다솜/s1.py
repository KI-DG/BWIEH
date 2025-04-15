"""
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

Pikachu
26
Venusaur
16
14
"""

n, m = map(int, input().split())

poketmon_dict = {}

for i in range(n):
    poketmon = str(input())
    poketmon_dict[str(i + 1)] = poketmon
    poketmon_dict[poketmon] = str(i + 1)
result = []
for _ in range(m):
    a = str(input())
    result.append(a)

for j in result:
    print(poketmon_dict[j])
