from cmath import log
import heapq as pq

def mochila(cap: int, weight: list, benef: list):
    assert len(weight) == len(benef)
    n = len(weight)
    items = [(weight[i], benef[i]) for i in range(n)]
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    cola = [(0, -cap, 0)]
    sol = -1
    
    def sup(pos: int, cap: int):
        rest, benef = cap, 0
        while pos < n and rest >= items[pos][1]:
            rest -= items[pos][0]
            benef += items[pos][1]
            pos += 1
        if pos < n and rest > 0:
            benef += (items[pos][1] / items[pos][0]) * rest
        return benef

    while len(cola):
        benef, cap, i = pq.heappop(cola)
        benef, cap = -benef, -cap
        sol = max(sol, benef)

        if benef + sup(i, cap) <= sol: continue
        act_weight, act_benef = items[i]

        if i < n:
            if cap >= act_weight and benef + sup(i, cap) > sol:
                pq.heappush(cola, (-benef-act_benef, -cap + act_weight, i+1))
            if benef + sup(i+1, cap) > sol:
                pq.heappush(cola, (-benef, -cap, i+1))
        print("Producto: " + "(" + str(act_weight) +"kg" + "," + str(act_benef) + "$" + ")")
    return sol


def run(): 
    weight = [1, 2, 4, 5, 7, 8]
    benef = [2,5,6,10,13,16]
    m = 8
    print("Productos Escogidos: ")
    print("Se obtendrá una ganancia de:", mochila(m, weight, benef), "$")
   
run()
