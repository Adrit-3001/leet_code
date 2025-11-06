class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        dic = {}
        for i in range(1,c+1):
            dic[i] = [0]
        for edge in connections:
            # if edge[0] not in dic.keys():
            #     dic[edge[0]] = [0, edge[1]]
            # else:
            if edge[1] not in dic[edge[0]]:
                dic[edge[0]].append(edge[1])
            # if edge[1] not in dic.keys():
            #     dic[edge[1]] = [0, edge[0]]
            # else:
            if edge[0] not in dic[edge[1]]:
                dic[edge[1]].append(edge[0])

        for qu in queries:
            if qu[0] == 2:
                dic[qu[1]][0] = -1
            else:
                
        
        
        # print(dic)
        # return []