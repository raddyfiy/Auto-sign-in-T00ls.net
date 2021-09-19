import requests
import json
import pickle
import datetime
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; E6883 Build/32.4.A.1.54; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36',   
    'Referer':'https://www.t00ls.com/members-profile-12894.html'
}
logindata={
"action" :"login",
"username":"yourname",  #填你的用户名，不要填ID
"password":"yourMD5",   #密码的MD5值
"questionid":1, #问题编号，对照下面注释填写，若没有设置提问则此处随便填写
"answer":""  #输入回答，若没有设置提问则此处随便填写，或不填
}
# questionid
# 1 母亲的名字
# 2 爷爷的名字
# 3 父亲出生的城市
# 4 您其中一位老师的名字
# 5 您个人计算机的型号
# 6 您最喜欢的餐馆名称
# 7 驾驶执照的最后四位数字

def login(session):
    loginurl="https://www.t00ls.com/login.json"
    response=session.post(url=loginurl,data=logindata,headers=headers)
    responsejson=json.loads(response.text)
    with open("cookiefile","wb") as fn:
        pickle.dump(session.cookies,fn)
    try:
        return responsejson["status"],responsejson["formhash"]
    except:
        return "login_error"

def cookielogin(session):
    singurl="https://www.t00ls.com/ajax-sign.json"
    signdata={
    "signsubmit":"true"
    }
    with open('cookiefile', 'rb') as fn:
        session.cookies.update(pickle.load(fn))
    formhashpage=session.post(url=singurl,data=signdata,headers=headers).text
    if(formhashpage.find(logindata["username"])>0):
        result="success"
        mark=formhashpage.find("formhash=")
        formhash=formhashpage[mark+9:mark+9+8]
        return result,formhash
    else:
        return "fail"

def signin(session,formhash):
    singurl="https://www.t00ls.com/ajax-sign.json"
    signdata={
    "formhash":"",
    "signsubmit":"true"
    }

    print(formhash)
    signdata["formhash"]=formhash
    response=session.post(url=singurl,data=signdata,headers=headers)
    #print(response.text)
    try:
        result=json.loads(response.text)["message"]
        print(result)       #出现success为签到成功，alreadysign为已经签到过
        return result
    except:
        print("Error,please give me issue")
        return "Error,please give me issue"

def logwrite(result):
    fn=open("log.txt",'a')
    time=datetime.datetime.now()
    fn.write(str(time)+"    :   "+result+"\n")
    fn.close()

def webhook(result):
    webhookurl = "http://sc.ftqq.com/"
    sckey = ""#替换成自己的sckey
    requests.get(url=webhookurl + sckey + ".send?text=t00ls_signin_result&desp=" + result)


session=requests.session()
try:
    result,formhash=cookielogin(session)
except:
    result,formhash=login(session)
if result=="success":
    result=signin(session,formhash)
else:
    print("login_error")
    result="login_error"
logwrite(result)
webhook(result)
