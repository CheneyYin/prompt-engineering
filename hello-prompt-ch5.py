from mychat import get_completion

# # 文本翻译
# ## 中文转西班牙语

prompt = f"""
你能从<text>中得到中文文本，你的任务是将它翻译成西班牙语。

中文文本：
<text>
上个月Apple发布了新款iPhone。
</text>

"""

# ## 识别语种

prompt = f"""
你能从<text>中得到文本，你的任务是识别它的语种。
要求：
    1.只输出包含的语种。
    2.如果是多语种，按照语种在文本占有比例从高到低排列。
    3.如果是多语种，输出语种用逗号分隔。

文本：
<text>
上个月Apple发布了新款iPhone。
Who are you?
Hola, me gustaría ordenar una batidora.
</text>

"""

# ## 多语种翻译

prompt = f"""
你能从<text>中得到文本，你的任务是将它分别翻译中文、日语和法语。
要求：
    1.输出JSON对象，key为语种，value为翻译后的文本。

文本：
<text>
My mum said life is like a box of chocolates.
</text>

"""

# ## 翻译+语气调整

prompt = f"""
你能从<text>中得到文本，你的任务是将它分别翻译中文，并且分别展示正式和非正式两种语气。
要求：
    1.输出JSON对象，key为语气类型（正式/非正式），value为翻译后的文本。

文本：
<text>
My mum said life is like a box of chocolates.
</text>

"""

# response = get_completion("deepseek-chat", prompt)
# print(response)

# ## 通用翻译器

user_messages = [
    "我妈妈说，生活就像一盒巧克力。",
    "母は人生はチョコレートの箱のようだと言った。",
    "Ma mère a dit que la vie est comme une boîte de chocolats.",
]

def translate(messages):
    for msg in messages:
        prompt = f"""
        你能从<text>中得到文本，你的任务是识别它的语种。
        要求：
            1.只输出包含的语种。

        文本：
        <text>
        {msg}
        </text>
        """

        language = get_completion("deepseek-chat", prompt)
        print(f"Original message ({language}): {msg}")

        prompt = f"""
        你能从<text>中得到{language}文本，你的任务是将它分别翻译中文、英语。
        要求：
            1.不要将中文翻译成中文，英文翻译成英文。
            2.输出JSON对象，key为语种(中文/英文)，value为翻译后的文本。

        文本：
        <text>
        {msg}
        </text>

        """

        response = get_completion("deepseek-chat", prompt)
        print(response)
        print("==================================================")


# 语气风格调整

prompt = f"""
你能从<text>中得到文本，你的任务是将它翻译成商务信函的格式。
要求：
    1.输出按照markdown格式。

文本：
<text>
兄弟，明天下午找个时间喝喝茶，顺便聊聊上周说的数据平台建设的事。这次主要是谈谈需求和技术难点。
</text>

"""

# 格式转换
import json

data = {
    "restaurant employees": [
        { "name": "jerry", "email": "jerry@gmail.com"},
        { "name": "tom", "email": "tom@hotmail.com"},
        { "name": "goff", "email": "goff@gmail.com"},   
    ]
}

prompt = f"""
你能从<json>中得到JSON格式的数据，将它转换为HTML表格，保留表格的caption和列名。
要求：
    只输出HTML。
    
<json>
{json.dumps(data)}
</json>
"""

# 拼写和语法纠正

prompt = f"""
你能从<text>中得到文本，你的任务是对它校对和更正。
要求：
    1.注意纠正文本保持原始语种，无需输出原始文本。
    2.如果没有发现任何错误，请回答“未发现错误”。

例如：
输入：I are happy.
输出：I am happy.

文本：
<text>
You is an boy. But I is an girl.
</text>

"""

# # 综合样例：文本翻译 + 拼写纠正 + 风格调整 + 格式转换

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""

prompt = f"""
你能从<text>中得到文本，你的任务是执行如下操作：
1. 首先进行拼写和语法纠错。
2. 然后将其翻译为中文。
3. 再将其转换成优质的淘宝评论风格，使用emoji表情。从多角度出发，分别说明产品的优点和缺点，并进行总结。
4. 润色一下描述，使评论更具吸引力。
5. 输出格式：
【优点】：xxx
【缺点】：xxx
【总结】：xxx
注意，只需填写xxx部分，并分段输出。
将结果输出成markdown格式。

<text>
{text}
</text>
"""

response = get_completion("deepseek-chat", prompt)
print(response)