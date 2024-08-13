from mychat import get_completion_from_messages

messages = [
    {
        "role": "system",
        "content": "你是一个郭德纲一样说话的助手。"
    },
    {
        "role": "user",
        "content": "给我讲个笑话。"
    },
    {
        "role": "assistant",
        "content": "于老师为什么喜欢抽烟？"
    },
    {
        "role": "user",
        "content": "我不知道。"
    }
]

messages = [
    {
        "role": "system",
        "content": "你是一个友好的聊天机器人。"
    },
    {
        "role": "user",
        "content": "好，你能提醒我，我的名字是什么吗？"
    },
]

messages = [
    {
        "role": "system",
        "content": "你是一个友好的聊天机器人。"
    },
    {
        "role": "user",
        "content": "Hi, 我是二狗。"
    },
]


# response = get_completion_from_messages(messages, temperature=1)
# print(response)

messages = [
    {
        "role": "system",
        "content": "你是一个友好的聊天机器人。"
    },
    {
        "role": "user",
        "content": "好，你能提醒我，我的名字是什么吗？"
    },
]

# response = get_completion_from_messages(messages, temperature=1)
# print(response)

messages = [
    {
        "role": "system",
        "content": "你是一个友好的聊天机器人。"
    },
    {
        "role": "user",
        "content": "Hi, 我是二狗。"
    },
    {
        "role": "user",
        "content": "好，你能提醒我，我的名字是什么吗？"
    },
]

response = get_completion_from_messages(messages, temperature=1)
print(response)


