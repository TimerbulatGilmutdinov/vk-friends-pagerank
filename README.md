### VK friends Pagerank calculating
This is a simple example of calculating pagerank for your friends list with nesting level 3
* For example, you have your VK profile `Me`
* You have your friends list `{Matt, Alex, Peter}`
* They have their own friends list
    * `Matt` : `{Me, Sarah, Alex, Joel`
    * `Alex` : `{Me, Matt, Ellie, Peter}`
    * `Peter`: `{Me, Alex, Bella, Pedro}`
* Then it will calculate Pagerank for every of these people
#### Getting started
1. Open main.py
2. Input your user access key into `token` parameter (see https://dev.vk.com/api/access-token/implicit-flow-user)
3. Input your VK id into `user_id` parameter
4. Run main.py (it may take about an hour, it depends on MAX_FRIENDS_COUNT, by default it equals 100)