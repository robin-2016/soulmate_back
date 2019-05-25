#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Robin

from flask import Flask,request
import json
from model import db,User,Dati

app= Flask(__name__)
@app.route("/")
def index():
    return "Hello world!!!"

@app.route("/dati/road")
def road():
    timu1={'title':'1.你有时间可以放松下自己，优先选择哪一项?','option':[{'value':'A','name':'听音乐','checked':False},
                                                      {'value':'B','name':'看电影','checked':False},
                                                     {'value':'C','name':'出去旅行','checked':False},{'value':'D','name':'蹦极','checked':False}]}
    timu2={'title':'2.选择我的兴趣标签:','option':[{'value':'A','name':'音乐','checked':False},{'value':'B','name':'电影','checked':False},
                                          {'value':'C','name':'宅','checked':False},{'value':'D','name':'终身学习','checked':False}]}
    timu3={'title':'3.从下面选择最想去旅游地:','option':[{'value':'A','name':'云南','checked':False},{'value':'B','name':'海南','checked':False},
                                          {'value':'C','name':'哈尔滨','checked':False},{'value':'D','name':'成都','checked':False}]}
    timu4={'title':'4.当要我到一个新的地方去时，我喜欢:','option':[{'value':'A','name':'要一幅地图','checked':False},
                                                   {'value':'B','name':'要书面指南','checked':False}]}
    timu5={'title':'5.我比较偏爱的获取新信息的媒体是:','option':[{'value':'A','name':'图画、图解、图形及图象','checked':False},
                                                  {'value':'B','name':'书面指导和言语信息','checked':False}]}
    data={'data':[timu1,timu2,timu3,timu4,timu5]}
    jsondata=json.dumps(data)
    # if request.method=='POST':
    #     # print(type(request.values['result']))
    #     fromdata=request.values
    #     dati= db.query(Dati).filter_by(openid=fromdata['openId']).first()
    #     # dati = Dati.query.filter_by(openid=fromdata['openId']).firs()
    #     print(dati)
    #     if dati != None:
    #         dati.result1=fromdata['result']
    #     else:
    #         dati=Dati(openid=fromdata['openid'],result1=fromdata['result'])
    #     print(dati)
    #     db.add(dati)
    #     db.commit()
    #     db.close()
    return jsondata

@app.route("/dati/people")
def people():
    timu1 = {'title': '1.对你爱过的人最想说的一句话?',
                'option': [{'value': 'A', 'name': '下回，好好爱她/他，别再让人家伤心了','checked':False},
                           {'value': 'B', 'name': '感谢你照耀了我的人生，让我也有了能够温暖别人的力量','checked':False}]}
    timu2 = {'title': '2. 下面哪句台词，你和前任都喜欢:', 'option': [{'value': 'A', 'name': '女人你已经成功引起了我的兴趣','checked':False},
                                                       {'value': 'B', 'name': '你好，好久不见','checked':False}]}
    timu3 = {'title': '3.认识你的人倾向形容你为:', 'option': [{'value': 'A', 'name': '热情和敏感','checked':False},
                                                   {'value': 'B', 'name': '逻辑和明确','checked':False}]}
    timu4 = {'title': '4.你倾向拥有:', 'option': [{'value': 'A', 'name': '很多认识的人和很亲密的朋友','checked':False},
                                                            {'value': 'B', 'name': '一些很亲密的朋友和一些认识的人','checked':False}]}
    timu5 = {'title': '5.在第一次约会中:', 'option': [{'value': 'A', 'name': '若你所约的人来迟了，你会很不高兴','checked':False},
                                                           {'value': 'B', 'name': '一点儿都不在乎，因为你自己常常迟到','checked':False}]}
    data = {'data': [timu1, timu2, timu3, timu4, timu5]}
    jsondata = json.dumps(data)
    return jsondata

@app.route("/dati/book")
def book():
    timu1 = {'title': '1.你平时更常看哪类书籍',
                'option': [{'value': 'A', 'name': '阅读罗曼蒂克一类的小说','checked':False},{'value': 'B', 'name': '看传记体裁的书籍','checked':False},
                           {'value': 'C', 'name': '流行的时尚杂志格外青睐','checked':False},{'value': 'D', 'name': '阅读财政经济一类的书报杂志', 'checked': False}]}
    timu2 = {'title': '2. 哪位历史人物你最有好感:', 'option': [{'value': 'A', 'name': '包青天','checked':False},
                                                    {'value': 'B', 'name': '诸葛亮','checked':False},
                                                    {'value': 'C', 'name': '唐伯虎', 'checked': False},
                                                    {'value': 'D', 'name': '雷锋', 'checked': False}]}
    timu3 = {'title': '3.在工作上，我表现出更多的是:', 'option': [{'value': 'A', 'name': '热忱，有很多想法且很有灵性','checked':False},
                                                   {'value': 'B', 'name': '完美精确且为人可靠','checked':False},
                                                   {'value': 'C', 'name': '坚强而有推动力', 'checked': False},
                                                   {'value': 'D', 'name': '有耐心且适应性强', 'checked': False}]}
    timu4 = {'title': '4.我在以下哪个群体中较感满足？', 'option': [{'value': 'A', 'name': '能心平气和大家达成一致的','checked':False},
                                                            {'value': 'B', 'name': '能彼此展开充分激烈的辩论','checked':False},
                                             {'value': 'C', 'name': '能详细讨论事情', 'checked': False},
                                             {'value': 'D', 'name': '能随意无拘束地开心地自由谈话', 'checked': False}]}
    timu5 = {'title': '5. 面对他人对自己的赞美，我的本能反应是：', 'option': [{'value': 'A', 'name': '没有也无所谓，欣喜也不至于','checked':False},
                                                           {'value': 'B', 'name': '我不需那些赞美，宁可他们欣赏我的能力','checked':False},
                                               {'value': 'C', 'name': '有点怀疑对方是否认真或立即回避众人的关注', 'checked': False},
                                                {'value': 'D', 'name': '赞美是一件多么令人愉悦的事', 'checked': False}]}
    data = {'data': [timu1, timu2, timu3, timu4, timu5]}
    jsondata = json.dumps(data)
    return jsondata

@app.route('/result',methods=['GET','POST'])
def result():
    fromdata = request.values
    if request.method=='GET':
        # print(fromdata)
        dati_result=db.query(Dati).filter_by(openid=fromdata['openId']).first()
        if fromdata['id'] == '1':
            dresult=dati_result.result1
            if dresult[0]=='A':
                bname='音乐家'
            elif dresult[0]=='B':
                bname='艺术家'
            elif dresult[0]=='C':
                bname='旅行家'
            else:
                bname='冒险家'
            if dresult['2']=='C'

        elif fromdata['id'] == '2':
            dresult = dati_result.result2
        else:
            dresult = dati_result.result3
        print(dresult)
        print(type(dresult))
    if request.method=='POST':
        data = db.query(Dati).filter_by(openid=fromdata['openId']).first()
        if data == None:
            dati1=Dati(openid=fromdata['openId'])
            if fromdata['id'] == '1':
                dati1.result1=fromdata['result']
            elif fromdata['id'] == '2':
                dati1.result2 = fromdata['result']
            else:
                dati1.result3 = fromdata['result']
            db.add(dati1)
        else:
            if fromdata['id'] == '1':
                data.result1=fromdata['result']
            elif fromdata['id'] == '2':
                data.result2 = fromdata['result']
            else:
                data.result3 = fromdata['result']
            db.add(data)
        db.commit()
        return 'OK'
    return 'OK'

if __name__=="__main__":
    app.run(host='192.168.10.104')