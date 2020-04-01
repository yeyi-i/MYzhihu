#!/usr/bin/python3

from __future__ import unicode_literals, print_function

import os
from zhihu_oauth import ZhihuClient


def get_question(url):
    url_question = ""

    for i in url.replace("https://www.zhihu.com/question/", ''):
        if i == "/":
            break
        url_question += i

    return int(url_question)


def listener(c_socket, addr):
    print("连接地址：%s" % str(addr))
    msgr = c_socket.recv(1024).decode('utf-8')
    print(msgr)
    msg = "server accepted msg: " + msgr + " from server respond.\r\n"
    c_socket.send(msg.encode('utf-8'))
    question = client.question(get_question('https://www.zhihu.com/question/382545061/answer/1105370864'))
    # print(question.title)
    # print(question.updated_time)
    # print(question.detail)

    # print(question.author.name) # 没有这个author类
    print(question.title)
    print(question.detail)
    print(question.updated_time)
    #
    # answer = client.from_url(msgr)
    # print(answer.author.name)
    # print(answer.content)
    c_socket.close()


def logger(text):
    log = open("./program.log", "a")
    log.writelines(text + "\n")
    log.close()


author_name = []
data = []

def converstaion(replies_object):
    global author_name
    global data
    if replies_object is not None:
        num = 0
        for r in replies_object:
            if num == 3:
                break
            if num > 0:
                author_name.append(r.author.name)
                converstaion(r.replies)
                print("  " + r.author.name + " replied "
                      + author_name[len(author_name) - 2]
                      + ": " + r.content + "\n")
                data.append({"name": author_name[len(author_name) - 2],
                             "replied by": r.author.name,
                             "content": r.content})
                author_name.pop(len(author_name) - 1)
            num += 1
        return data


if __name__ == '__main__':
    client = ZhihuClient()
    TOKEN_FILE = './static/token.pkl'
    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        client.login_in_terminal()
        client.save_token(TOKEN_FILE)

    # question = client.question(get_question('https://www.zhihu.com/question/382545061/answer/1105370864'))
    # # print(question.author.name) # 没有这个author类
    # print(question.title)
    # print(question.detail)
    # print(question.updated_time)

    answer = client.from_url('https://www.zhihu.com/question/382545061/answer/1105370864')
    # print(answer.author.name)
    # print(answer.content)
    # print(answer.updated_time)

    num = 0
    for i in answer.comments:
        if num == 3:
            print(author_name)
            num = 0
            break
        print(i.author.name + ": " + i.content + "\n")
        author_name.append(i.author.name)
        # for n in i.replies:
        #     if num == 5:
        #         num = 0
        #         break
        #     if num > 1:
        #         print("  " + n.author.name + " replied " + i.author.name + ': ' + n.content + "\n")
        #     for u in n.replies:
        #         if num == 3:
        #             num = 0
        #             break
        #         if num > 1:
        #             print("     " + u.author.name + " replied " + n.author.name + ': ' + u.content + "\n")
        #         num += 1
        #     num += 1
        print(converstaion(i.replies))
        print(len(data))
        data = []
        num += 1

    # print(answer.comment)

    # # me = client.me()
    # logger("socket listener started")
    #
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind((socket.gethostname(), 8888))
    # s.listen(3)
    #
    # while True:
    #     c, address = s.accept()
    #     _thread.start_new_thread(listener, (c, address))

    # 爬取答案：
    # answer = client.answer(1071790931)
    # print(answer.content)
    # print(answer.can_comment)
    # for i in answer.comments:
    #     print("作者： " + str(i.author.name))
    #     print("内容： " + i.content)

# Debug
# print('name', me.name)
# print('headline', me.headline)
# print('description', me.description)
#
# print('following topic count', me.following_topic_count)
# print('following people count', me.following_topic_count)
# print('followers count', me.follower_count)
#
# print('voteup count', me.voteup_count)
# print('get thanks count', me.thanked_count)
#
# print('answered question', me.answer_count)
# print('question asked', me.question_count)
# print('collection count', me.collection_count)
# print('article count', me.articles_count)
# print('following column count', me.following_column_count)
