# Auto-sign-in-T00ls.net V1.3
基于土司官方api的自动签到脚本

<details>
<summary>更新说明：</summary>
2020.7.7：账号密码登录后自动保存cookie，在失效前免登录，失效后再用密码登录</br>
2020.4.9：@we1x4n 添加了webhook以使用微信查看签到结果</br>
2020.3.28：修正api导致的错误</br>
</details>

*****************
准备环境：

python3、可写的目录权限（用于生成日志）

用法：

<details>
  <summary>1. Windows下设置自动签到：</summary>
  
    1) . 打开cmd，输入： 
     schtasks /create /sc daily /tn "t00ls_sign" /tr "python Auto_tools_signin.py"
  
    2) .在cmd输入compmgmt.msc，打开计算机管理，在左侧选择系统工具->任务计划程序->活动任务->找到t00ls_sign双击->属性->操作->编辑，
      在“起始于”里写入你存放脚本的文件夹路径。
 ![image](https://github.com/raddyfiy/cod/blob/master/2020-03-28_153315.png)
    
    3) .每天会自动签到，可以在log.txt查看签到日志.
</details>


<details>
  <summary>2. Linux下设置自动签到：</summary>
  
    1) 
      crontab -e
  
    2) 写以下指令，每天5.00am自动执行。
      0 5 * * * python /path/Auto_tools_signin.py
</details>
    

<details>
  <summary>3. 手动签到一次：</summary>
    
    python3 Auto_tools_signin.py
</details>


  
