# python v3.6.4

*   selenium **v3.10.0** _引用模块用于操作浏览器_

    > IEDriverServer.exe **v3.10.0**(这个地方版本与 selenium 一样) _IE 浏览器_

    > chromedriver.exe **v2.36**(根据谷歌浏览器版本安装) _谷歌浏览器_

*   xlrd **1.1.0** _读取 excel_

*   pywin32 _操作系统_

*   pynput  Python控制、监听键盘鼠标

-   打包命令，要在项目目录那里，根据 **sys.path** 看所有目录，一个一个加进去

```
pyinstaller.exe -F src/watch.py -p f:\\Work\\domeSelenium1 -p f:\\Work\\domeSelenium1\\src -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\DLLs -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\lib -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36 -p C:\\Users\\Dev\\AppData\\Roaming\\Python\\Python36\\site-packages -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\win32 -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\win32\\lib -p C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages\\Pythonwin
```
