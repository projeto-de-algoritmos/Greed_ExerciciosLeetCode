from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        sorted_tasks = sorted(tasks)  # Ordena as tarefas em ordem crescente
        sorted_workers = sorted(workers)  # Ordena os trabalhadores em ordem crescente

        completed_tasks = 0
        i, j = 0, 0  # Ponteiros para tarefas e trabalhadores, respectivamente

        while i < len(sorted_tasks) and j < len(sorted_workers):
            if sorted_workers[j] >= sorted_tasks[i]:
                # Atribui o trabalhador j à tarefa i
                completed_tasks += 1
                i += 1
                j += 1
            elif pills > 0 and sorted_workers[j] + strength >= sorted_tasks[i]:
                # Atribui o trabalhador j à tarefa i com a ajuda de um comprimido
                completed_tasks += 1
                i += 1
                j += 1
                pills -= 1
            else:
                j += 1

        return completed_tasks
