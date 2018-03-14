# python v3.6.4

*   selenium **v3.10.0** _引用模块用于操作浏览器_

    > IEDriverServer.exe **v3.10.0**(这个地方版本与 selenium 一样) _IE 浏览器_

    > chromedriver.exe **v2.36**(根据谷歌浏览器版本安装) _谷歌浏览器_

*   xlrd **1.1.0** _读取 excel_

-   config.py 模块的代码

```
import os

class Config:
    username = ''  # 用户名
    password = ''  # 密码
    userurl = ''  # 要打开的url
    assestpath = os.path.abspath('')
    pass
```
