graph = {
    "A": [["B","C"],["D"]],
    "B": [ ["G"], ["H"]],
    "D": [["E","F"]]
}

nodeCost = {
    "B":6,"C":12,"D":10,"E":4,"F":4,"G":4,"H":7
}

edgeCost = 1
headNode = ["A"]

def solve(currs):
    flag = 0
    for curr in currs:
        if curr in graph.keys():
            flag=1

    if not flag:
        return 0

    minCost = 10000000
    for curr in currs:
        if curr in graph.keys():
            for path in graph[curr]:
                cost = 0
                for node in path:
                    cose = cost + nodeCost[node] + edgeCost
                if minCost > cost:
                    minCost = cost
                    nextNodes = path
    print(f"{nextNodes},{minCost}")
    return [nextNodes,minCost]

def driver():
    cost = 0
    curr = headNode
    print("dfjksdf")
    moves = 0
    while True:
        for node in curr:
            result  = solve(node)
            if not result:
                print(f"moves: {moves}")
                print(f"cost : {cost}")
                return cost
            cost + result[1]
            curr = result[0]
        moves += 1

if __name__ == "__main__":
    driver()