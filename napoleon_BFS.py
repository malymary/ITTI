
# find Napoleon in family tree

# we create a hashmap (dictionary) which will contain keys (names as nodes) as values (parents as neighbors)

from collections import deque
family_tree = {}
family_tree["me"] = ["Dostoyevsky", "Akhmatova"]
family_tree["Dostoyevsky"] = ["Stalin", "Lenin"]
family_tree["Akhmatova"] = ["Trotsky", "Brodsky"]
family_tree["Stalin"] = ["Napoleon", "Hitler"]
family_tree["Lenin"] = ["Nikolay First", "Yekaterina Second"]
family_tree["Trotsky"] = []
family_tree["Brodsky"] = []
family_tree["Napoleon"] = []
family_tree["Hitler"] = []
family_tree["Nikolay First"] = []
family_tree["Yekaterina Second"] = []


def is_napoleon(name):
    return name == "Napoleon"


def napoleon_search(name, graph):
    path = []
    checked = []
    queue = deque([(name, path)])

    while queue:
        person, path = queue.popleft()

        if person not in checked:
            if is_napoleon(person):
                print(name, "is Napoleon's heir!")
                return path + [person]
            else:
                checked.append(person)
                for friend in graph[person]:
                    queue.append((friend, path+[person]))
    return False


print(napoleon_search("me", family_tree))
