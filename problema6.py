
somaDoQuadrado = 0
for i in range(1, 101):
  somaDoQuadrado += i*i

quadradoDaSoma = 0
for i in range(1, 101):
  quadradoDaSoma += i
quadradoDaSoma = quadradoDaSoma * quadradoDaSoma

print(quadradoDaSoma - somaDoQuadrado)
