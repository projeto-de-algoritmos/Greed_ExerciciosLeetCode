# [Redução de Pratos](https://leetcode.com/problems/reducing-dishes/)

**Nível: Difícil**

Um chef coletou dados sobre o nível de `satisfaction` de seus `n` pratos. Chef pode cozinhar qualquer prato em 1 unidade de tempo.

O **coeficiente de tempo semelhante** de um prato é definido como o tempo necessário para cozinhar esse prato, incluindo pratos anteriores, multiplicado por seu nível de satisfação, ou seja, `time[i] * satisfaction[i]`.

Retorne *a soma máxima do **coeficiente de tempo semelhante** que o chef pode obter após a preparação dos pratos*.

Os pratos podem ser preparados em **qualquer** ordem e o chef pode descartar alguns pratos para obter esse valor máximo.


**Exemplo 1:**

``` bash
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explicação: Depois de remover o segundo e último prato, o coeficiente de tempo igual total máximo será igual a (-1*1 + 0* 2 + 5*3 = 14). Cada prato é preparado em uma unidade de tempo.
```

**Exemplo 2:**

``` bash
Input: satisfaction = [4,3,2]
Output: 20
Explicação: Os pratos podem ser preparados em qualquer ordem, (2*1 + 3*2 + 4*3 = 20)
```

**Exemplo 3:**

``` bash
Input: satisfaction = [-1,-4,-5]
Output: 0
Explicação: As pessoas não gostam dos pratos. Nenhum prato é preparado.
```