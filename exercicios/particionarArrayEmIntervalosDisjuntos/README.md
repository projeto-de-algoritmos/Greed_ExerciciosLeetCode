# [Particionar Array em Intervalos Disjuntos](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)

Dado um array de inteiros `nums`, particione-o em dois subarrays (contíguos) `esquerda` e `direita` de forma que:

- Cada elemento em `esquerda` seja menor ou igual a cada elemento em `direita`.
- `esquerda` e `direita` não estão vazios.
- `esquerda` tem o tamanho mínimo possível.

Retorne o tamanho de `esquerda` após essa partição.

Os casos de teste são gerados de forma que a partição exista.

**Example 1:**

``` bash
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

**Example 2:**

```bash
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```
