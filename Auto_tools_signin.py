import requests
import json
import datetime
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; E6883 Build/32.4.A.1.54; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36',
   # 'Cookie':'smile=6D1; UTH_cookietime=2592000; UTH_auth=9469AOkbnGuWXJae9tax1xhro0Lpk5OoL%2FteXrsEoGe1uUrHJnCddFwZnPrW2wJ4rxUUSuNHcM9e%2F6QHd7QTeHyHGXxN54PwZ82Ftw; UTH_visitedfid=48D40; UTH_sid=7FzULH'
    'Referer':'https://www.t00ls.net/members-profile-12894.html'
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
    loginurl="https://www.t00ls.net/login.json"
    logindata={
    "action" :"login",
    "username":"yourname",  #填你的用户名，不要填ID
    "password":"yourMD5",   #你密码的MD5值
    "questionid":1, #问题编号，对照上面注释填写，若没有设置提问则此处随便填写
    "answer":""  #输入回答，若没有设置提问则此处随便填写
    }
    response=session.post(url=loginurl,data=logindata,headers=headers)
    responsejson=json.loads(response.text)
    try:
        return responsejson["status"]
    except:
        return "login_error"

def signin(session):
    singurl="https://www.t00ls.net/ajax-sign.json"
    signdata={
    "formhash":"",
    "signsubmit":"true"
    }
    formhashpage=session.post(url=singurl,data=signdata,headers=headers).text
    mark=formhashpage.find("formhash=")
    formhash=formhashpage[mark+9:mark+9+8]
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
result=login(session)
if result=="success":
    result=signin(session)
else:
    print("login_error")
    result="login_error"
logwrite(result)
webhook(result)
