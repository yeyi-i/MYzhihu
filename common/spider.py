from __future__ import unicode_literals, print_function

import os
from datetime import datetime

from zhihu_oauth import ZhihuClient

author_name = []
data = []


def conversation(replies_object):
    global author_name
    global data
    if replies_object is not None:
        num = 0
        for r in replies_object:
            if num == 3:
                break
            if num > 0:
                author_name.append(r.author.name)
                conversation(r.replies)
                # print("  " + r.author.name + " replied "
                #       + author_name[len(author_name) - 2]
                #       + ": " + r.content + "\n")
                data.append({"name": author_name[len(author_name) - 2],
                             "replied by": r.author.name,
                             "content": r.content})
                author_name.pop(len(author_name) - 1)
            num += 1
        return data


def get_question_num(url):
    url_question = ""

    for i in url.replace("https://www.zhihu.com/question/", ''):
        if i == "/":
            break
        url_question += i

    return int(url_question)


def get_answer_num(url):
    url_answer = ""

    for i in url.replace("https://www.zhihu.com/question/"
                         + str(get_question_num(url))
                         + "/answer/", ''):
        url_answer += i

    return int(url_answer)


def timestamp_to_datetime(date_num):
    d = datetime.fromtimestamp(date_num)
    str1 = d.strftime("%Y-%m-%d %H:%M")

    return str1


# 爬取答案：
# answer = client.answer(1071790931)
# print(answer.content)
# print(answer.can_comment)
# for i in answer.comments:
#     print("作者： " + str(i.author.name))
#     print("内容： " + i.content)

def main(url):
    try:
        content = {}
        client = ZhihuClient()
        TOKEN_FILE = './static/token.pkl'
        if os.path.isfile(TOKEN_FILE):
            client.load_token(TOKEN_FILE)
        else:
            print("No token file.")

        # 由于提供的通常都是指定回答的连接，直接使用OAUTH库里的自动提取from_url函数的话，
        # 无法直接提取答案的ID，只能再用一下自己写的截取答案ID函数。
        question = client.question(get_question_num(url))
        answer = client.from_url(url)  # 自动提取函数提取回答ID
        content = {'question_id': get_question_num(url), 'question_title': question.title,
                   # 'question_author': question.author.name,
                   'question_detail': question.detail, 'question_pubDate': timestamp_to_datetime(question.updated_time),
                   'answer_id': get_answer_num(url), 'answer_author': answer.author.name,
                   'answer_pubDate': timestamp_to_datetime(answer.updated_time), 'answer_content': str(answer.content)}

        return content
    except Exception as e:
        raise e
