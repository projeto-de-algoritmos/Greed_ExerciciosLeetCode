# [Número Mínimo de Flechas para Estourar Balões](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

**Nível Médio**

Existem alguns balões esféricos presos em uma parede plana que representa o plano XY. Os balões são representados como uma matriz de inteiros 2D chamada `points`, onde `points[i] = [xstart, xend]` indica um balão cujo diâmetro horizontal se estende entre `xstart` e `xend`. Você não sabe as coordenadas exatas de y dos balões.

Setas podem ser disparadas diretamente verticalmente (na direção positiva de y) de diferentes pontos ao longo do eixo x. Um balão com `xstart` e `xend` é estourado por uma flecha disparada em `x` se `xstart <= x <= xend`. Não há limite para o número de flechas que podem ser disparadas. Uma flecha disparada continua a subir infinitamente, estourando todos os balões em seu caminho.

Dada a matriz "points", retorne o número mínimo de flechas que devem ser disparadas para estourar todos os balões.

**Example 1:**

``` bash
Entrada: points = [[10,16],[2,8],[1,6],[7,12]]
Saída: 2
Explicação: Os balões podem ser estourados com 2 flechas:
Dispare uma flecha em x = 6, estourando os balões [2,8] e [1,6].
Dispare uma flecha em x = 11, estourando os balões [10,16] e [7,12].
```

**Example 2:**

``` bash
Entrada: points = [[1,2],[3,4],[5,6],[7,8]]
Saída: 4
Explicação: Uma flecha precisa ser disparada para cada balão, totalizando 4 flechas.
```

**Example 3:**

``` bash
Entrada: points = [[1,2],[2,3],[3,4],[4,5]]
Saída: 2
Explicação: Os balões podem ser estourados com 2 flechas:
Dispare uma flecha em x = 2, estourando os balões [1,2] e [2,3].
Dispare uma flecha em x = 4, estourando os balões [3,4] e [4,5].
```

