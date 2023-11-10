# Casbin
### [0x01 前言](https://github.com/charonlight/xxl-jobExploitGUI#0x01-前言)

工具实现了Casbin账号密码泄露漏洞的单个URL检测、批量URL检测

###0x02 工具使用说明

**单个检测**

```
python3 Casbin_get_users.py -u http://127.0.0.1
```

![image-20231110093654911](C:\Users\hxma2\AppData\Roaming\Typora\typora-user-images\image-20231110093654911.png)

**批量检测**

```
python3 Casbin_get_users.py -f url.txt
```

![image-20231110093848701](C:\Users\hxma2\AppData\Roaming\Typora\typora-user-images\image-20231110093848701.png)

脚本检查结束会在脚本文件夹下会自动生成result.txt文件，文件内容为存在漏洞的URL

![image-20231110094126703](C:\Users\hxma2\AppData\Roaming\Typora\typora-user-images\image-20231110094126703.png)

### [0x03 免责声明](https://github.com/charonlight/xxl-jobExploitGUI#0x03-免责声明)

该开源工具是由作者按照开源许可证发布的，仅供个人学习和研究使用。作者不对您使用该工具所产生的任何后果负任何法律责任。

![image-20231110094300346](C:\Users\hxma2\AppData\Roaming\Typora\typora-user-images\image-20231110094300346.png)



