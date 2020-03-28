# Auto-sign-in-T00ls.net
基于土司官方api的自动签到脚本

官方文档有一些错误（至2020.3.28）：
  1.  username正确应该填用户名，文档中错误的写为UID
  2.  登录接口返回的formhash是错误的，与签到页面的不符。
此脚本对上述问题做了修正，可正常使用。

准备环境：

python3、可写的目录权限（用于生成日志）

用法：

<details>
  <summary>1.windows下设置自动签到：</summary>
  1. 打开cmd，输入：
  
  schtasks /create /sc daily /tn "t00ls_sign" /tr "python tools_sign.py"
  
  2.在cmd输入compmgmt.msc，打开计算机管理，在左侧选择系统工具->任务计划程序->活动任务->找到t00ls_sign双击->属性->操作->编辑， 在“起始于里”写入你存放脚本的文件夹路径。
  3.每天会自动签到，可以在log.txt查看签到日志.
  
</details>

2.linux下设置自动签到：
    （待补充）
    
3.手动签到一次：

  python3 Auto_tools_signin.py
