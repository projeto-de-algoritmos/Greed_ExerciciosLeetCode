# [Número Máximo de Tarefas que Você Pode Atribuir](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/)

**Nível: Difícil**

Você tem `n` tarefas e `m` trabalhadores. Cada tarefa tem um requisito de força armazenado em uma matriz inteira **indexada por 0** `tasks`, com a tarefa `iᵗʰ` exigindo força `tasks[i]` para ser concluída. A força de cada trabalhador é armazenada em uma matriz inteira **indexada por 0** `workers`, com o `jᵗʰ` trabalhador com força `workers[j]`. Cada trabalhador só pode ser designado para uma **única** tarefa e deve ter uma força **maior ou igual** ao requisito de força da tarefa (ou seja, `workers[j] >= tasks[i]`).

Além disso, você tem `pills` pílulas mágicas que **aumentam a força de um trabalhador** em `strength`. Você pode decidir quais trabalhadores recebem as pílulas mágicas, no entanto, você só pode dar a cada trabalhador **no máximo uma** pílula mágica.

Dadas as matrizes inteiras **indexadas por 0** `tasks` e `workers`e os inteiros `pills` e `strength`, *retorne o número **máximo** de tarefas que podem ser concluídas.*


**Exemplo 1:**

``` bash
Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explicação:
Podemos atribuir a pílula mágica e as tarefas da seguinte forma: 
- Dê a pílula mágica para o trabalhador 0. 
- Atribuir o trabalhador 0 à tarefa 2 (0 + 1 >= 1) 
- Atribuir o trabalhador 1 à tarefa 1 (3 >= 2) 
- Atribuir o trabalhador 2 à tarefa 0 (3 >= 3)
```

**Exemplo 2:**

``` bash
Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explicação:
Podemos atribuir a pílula mágica e as tarefas da seguinte forma: 
- Dê a pílula mágica ao trabalhador 0. 
- Atribuir trabalhador 0 à tarefa 0 (0 + 5 >= 5)
```

**Exemplo 3:**

``` bash
Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explicação:
Podemos atribuir as pílulas mágicas e tarefas da seguinte forma: 
- Dê a pílula mágica ao trabalhador 0 e ao trabalhador 1. 
- Atribua o trabalhador 0 à tarefa 0 (0 + 10 >= 10) 
- Atribua o trabalhador 1 à tarefa 1 (10 + 10 >= 15) 
A última pílula não é dada porque irá não tornar nenhum trabalhador forte o suficiente para a última tarefa.
```