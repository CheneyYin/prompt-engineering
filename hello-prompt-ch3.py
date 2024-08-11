from mychat import get_completion

# # 单一文本概括

prod_review_zh = f"""
这个熊猫公仔是我给女儿的生日礼物，她很喜欢，去哪都带着。
公仔很软，超级可爱，面部表情也很和善。但是相比于价钱来说，
它有点小，我感觉在别的地方用同样的价钱能买到更大的。
快递比预期提前了一天到货，所以在送给女儿之前，我自己玩了会。
"""

# ## 首次尝试

prompt = f"""
你能从<review>中提取到一个来自用户的产品评论。
你的任务是为这个产品评论生成一个简短摘要。
要求：
    最多使用50个token。

产品评论：
<review>
{prod_review_zh}
</review>

"""


# ## 关键角度侧重

prompt = f"""
你能从<review>中提取到一个来自用户的产品评论。
你的任务是为这个产品评论进行概括，并且侧重在产品运输上。
要求：
    最多使用50个token。

产品评论：
<review>
{prod_review_zh}
</review>

"""

prompt = f"""
你能从<review>中提取到一个来自用户的产品评论。
你的任务是为这个产品评论进行概括，并且侧重在产品价格和质量。
要求：
    最多使用50个token。

产品评论：
<review>
{prod_review_zh}
</review>

"""

# ## 关键信息提取

prompt = f"""
你能从<review>中提取到一个来自用户的产品评论。
你的任务是从这个产品评论提取产品运输相关的信息。
要求：
    最多使用30个token。

产品评论：
<review>
{prod_review_zh}
</review>

"""

# # 多条文本概括
review_1 = f"""
很喜欢用小米的东西。，是的，是质量很好，清洁效果也还行，不错，以后还会回购。颜值很高的，包装也非常的简洁，4个清洁模式很好。
"""

review_2 = f"""
这款电动牙刷非常好用，以前给孩子买了个真的是半年充一次电，觉得好用，所以这次也给自己买了一件，待机时间确实久，而且有四种模式可以切换使用
"""

review_3 = f"""
再不买小米，盒子里连个充电插头都没有，还得自己备。
"""

review_4 = f"""
动力太小了，外观话是挺好看的。
"""

reviews = [review_1, review_2, review_3, review_4]

# for idx, review in enumerate(reviews):
#     prompt = f"""
#     你能从<review>中得到来自用户的产品评论。
#     你的任务是为产品评论进行概括。
#     要求：
#         最多使用50个token。

#     产品评论：
#     <review>
#     {review}
#     </review>

#     """

#     response = get_completion("deepseek-chat", prompt)
#     print(idx, response)


reviews = ",".join(
    [
    '''
    {{
        "id": {},
        "content": "{}"
    }}'''.format(idx, review) for idx, review in enumerate(reviews)
    ]
)

prompt = f"""
你能从JSON数组中得到多条来自用户的产品评论，每条评论包括评论ID和评论内容。
你的任务是为每个产品评论进行概括。
要求：
    每个评论概括最多使用50个token。
    输出时，请使用JSON数组格式，每个JSON对象包括id、content和summary三个键。

产品评论：
```json
[
{reviews}
]
```
"""

print(prompt)
response = get_completion("deepseek-chat", prompt)
print(response)