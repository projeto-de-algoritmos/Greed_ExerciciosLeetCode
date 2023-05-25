from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = nums[0]
        max_seen = nums[0]
        partition_idx = 0

        for i in range(1, n):
            if nums[i] < max_left:
                max_left = max_seen
                partition_idx = i
            else:
                max_seen = max(max_seen, nums[i])

        return partition_idx + 1
    
"""
O algoritmo utiliza a técnica de intervalo de particionamento. 
Ele itera pela lista, acompanhando o maior valor visto até o momento 
(max_seen) e o maior valor na sub-lista left (max_left). 
Quando um elemento menor que max_left é encontrado, atualiza-se max_left 
para max_seen e registra-se o índice de partição (partition_idx). 
Caso contrário, atualiza-se max_seen. No final, retorna-se partition_idx + 1, 
o tamanho de left. Essa abordagem é eficiente, pois percorre a lista 
apenas uma vez, mantendo o controle dos maiores valores e encontrando o 
ponto de divisão ótimo.
"""