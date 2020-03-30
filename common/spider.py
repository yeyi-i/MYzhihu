from __future__ import unicode_literals, print_function

import os
from . import
from zhihu_oauth import ZhihuClient


def get_question_num(url):
    url_question = ""

    for i in url.replace("https://www.zhihu.com/question/", ''):
        if i == "/":
            break
        url_question += i

    return int(url_question)


# 爬取答案：
# answer = client.answer(1071790931)
# print(answer.content)
# print(answer.can_comment)
# for i in answer.comments:
#     print("作者： " + str(i.author.name))
#     print("内容： " + i.content)

def main(url):
    content={}
    client = ZhihuClient()
    TOKEN_FILE = '../static/token.pkl'
    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        print("You will need a token file about your account to get all information.")

    # 由于提供的通常都是指定回答的连接，直接使用OAUTH库里的自动提取from_url函数的话，
    # 无法直接提取答案的ID，只能再用一下自己写的截取答案ID函数。
    question = client.question(get_question_num(url))
    answer = client.from_url(url) # 自动提取函数提取回答ID
    content = {'question_title':question.title, 'question_author':question.author.name}


