import networkx as nx


class AStarTraverser:
    def __init__(self):
        # heuristics dictionary is always from point x to Imara Daima.
        self.heuristics = {
            'karen': 21.22,
            'gitaru': 25,
            'loresho': 16,
            'lavington': 12,
            'parklands': 10,
            'kilimani': 11,
            'langata': 15,
            'CBD': 8,
            'donholm': 4,
            'hill view': 12,
            'kasarani': 11,
            'kahawa': 16,
            'imara daima': 0,
            'j1': 19,
            'j2': 14.5,
            'j3': 10,
            'j4': 17,
            'j5': 12,
            'j6': 22,
            'j7': 24,
            'j8': 17,
            'j9': 14,
            'j10': 9,
            'j11': 11.7,
            'j12': 9,
            'j13': 4
        }
        self.visited = []
        self.endSearch = False

    @staticmethod
    def get_min_key(dictionary: dict):
        min_key = None
        min_num = None
        for key in dictionary.keys():
            if min_num is None:
                min_num = dictionary[key]
                min_key = key
            elif float(dictionary[key]) < float(min_num):
                min_num = dictionary[key]
                min_key = key
        return min_key

    def a_star(self, graph: nx.Graph, start_node, goal_node):
        queue = [start_node]
        cost_so_far = 0
        while queue and not self.endSearch:
            fn = {}
            s = queue.pop(0)
            self.visited.append(s)
            print("Drive to", s, " Estate", end="\n")
            for i in list(graph[s]):
                fn[i] = float(self.heuristics.get(i)) + float(graph.get_edge_data(s, i).get('weight')) + cost_so_far
            min_key = self.get_min_key(fn)
            cost_so_far += float(graph.get_edge_data(s, min_key).get('weight'))
            queue.append(min_key)
            print("Goal Node: ", goal_node, "\nCurrent Node: ", min_key)
            print('cost so far', cost_so_far)
            if min_key is goal_node:
                self.endSearch = True
                self.visited.append(min_key)
                break
