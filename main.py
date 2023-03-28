import random
import matplotlib.pyplot as plt
import vk_api
import networkx as nx

MAX_FRIENDS_COUNT = 100

vk_session = vk_api.VkApi(
    token='your_token'
)

vk = vk_session.get_api()

# https://vk.com/bulathelmut
user_id = 410258487

G = nx.DiGraph()


def get_friends_ids(user_id: int):
    friends_ids_list = vk.friends.get(user_id=user_id)['items']
    if len(friends_ids_list) > MAX_FRIENDS_COUNT:
        friends_ids_list = random.sample(friends_ids_list, MAX_FRIENDS_COUNT)
    else:
        friends_ids_list = friends_ids_list
    return friends_ids_list


my_friends_ids_list = get_friends_ids(user_id)
my_friends_names_list = vk.users.get(user_ids=my_friends_ids_list, fields=['first_name', 'last_name'])

for f_id, name in zip(my_friends_ids_list, my_friends_names_list):
    G.add_node(f_id, name=name['first_name'])

for my_friend_id in my_friends_ids_list:
    try:
        friends_of_my_friend_list = get_friends_ids(my_friend_id)
        for friends_of_friend_id in friends_of_my_friend_list:
            G.add_edge(my_friend_id, friends_of_friend_id)
            try:
                friends_of_fof = get_friends_ids(friends_of_friend_id)
                for foff_id in friends_of_fof:
                    G.add_edge(friends_of_friend_id, foff_id)
            except vk_api.exceptions.ApiError:
                continue
    except vk_api.exceptions.ApiError:
        continue

pagerank = nx.pagerank(G)

sorted_pagerank_list = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

pagerank_sum = 0

for id, pagerank in sorted_pagerank_list:
    print(f'https://vk.com/id{id} with rank : {pagerank}')
    pagerank_sum += pagerank

print(pagerank_sum)

fig, ax = plt.subplots(figsize=(30, 30))

nx.draw(G, with_labels=True, ax=ax)

plt.show()
