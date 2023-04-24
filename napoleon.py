
# find Napoleon in family tree

# we create a hashmap (dictionary) which will contain keys (nodes) and values (neighbors)

from collections import deque
family_tree = {}
family_tree["me"] = ["Dostoyevsky", "Akhmatova"]
family_tree["Dostoyevsky"] = ["Stalin", "Lenin"]
family_tree["Akhmatova"] = ["Trotsky", "Brodsky"]
family_tree["Stalin"] = ["Napoleonis", "Hitler"]
family_tree["Lenin"] = ["Nikolay First", "Yekaterina Second"]
family_tree["Trotsky"] = []
family_tree["Brodsky"] = []
family_tree["Napoleonis"] = []
family_tree["Hitler"] = []
family_tree["Nikolay First"] = []
family_tree["Yekaterina Second"] = []


def is_napoleon(name):
    return name == "Napoleon"


def napoleon_search(key, graph):
    checked = []
    queue = deque()
    queue += graph[key]

    while queue:
        person = queue.popleft()
        if person not in checked:
            if is_napoleon(person):
                print("I am Napoleon's heir!")
                return True
            else:
                checked.append(person)
                queue += graph[person]
    return False


print(napoleon_search("me", family_tree))
