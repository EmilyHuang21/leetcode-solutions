class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        indegree = {}
        result = []

        # Step 1: Build graph and in-degree
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        # Step 2: Initialize queue with all available supplies
        queue = deque(supplies)

        # Step 3: BFS - Topological Sort
        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)

        return result
        