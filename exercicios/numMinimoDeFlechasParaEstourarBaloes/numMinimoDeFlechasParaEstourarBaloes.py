from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 0
        end = float('-inf')

        for balloon in points:
            if balloon[0] > end:
                arrows += 1
                end = balloon[1]

        return arrows

"""
O código implementa uma solução greedy para o problema de encontrar o 
número mínimo de flechas necessárias para estourar balões. Ele ordena 
os balões com base nos pontos finais, percorre a lista de balões e, para 
cada balão, verifica se a coordenada de início é maior que o valor da 
última coordenada de fim registrada. Se for, incrementa o contador de 
flechas e atualiza o valor da coordenada de fim. No final, retorna o contador 
de flechas. A abordagem greedy é adequada aqui porque a ordem dos balões não 
interfere na solução ótima. (Interval Sheduling)
"""
