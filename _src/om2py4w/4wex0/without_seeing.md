# IPython之视而不见的后果
9:26 下午 十一月 9, 2015

## 起源
看大妈上课时用ipython非常酷，每次在终端输入```ipython```,底下便跳出in，out等酷酷的字符。

## 尝试
于是自己也想装个，便用 ```pip install ipython```安装，安装完结果运行不了。

```
➜  ~  ipython
zsh: command not found: ipython
```
开始怀疑自己，怀疑人生！难道我没安装好？

```
➜  ~  pip install ipython
Requirement already satisfied (use --upgrade to upgrade): ipython in /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
Cleaning up...
➜  ~
```
重新安装，却提示已经安装好。于是转去安装目录：

```
➜  ~  /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
➜  site-packages  ipython
➜  ipython
```
还是不行......
google,stackoverflow各种搜索，还是不行。
咨询朋友，咨询教练，把他们折腾到半夜，还是没搞定。

## 转机
今天吃完饭，便想重新折腾ipython，各种安装办法都试过了，于是便到githup/ipython看看，结果看到这段：

> Instant running
>
> You can run IPython from this directory without even installing it system-wide by typing at the terminal:
>
> ```$ python -m IPython```

运行：

```python
➜  ipython  python -m IPython
Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46)
Type "copyright", "credits" or "license" for more information.

IPython 4.1.0-dev -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print "hello"
hello

In [2]:
```
添加 alias ipython="python -m IPython"  到 ~/.zshrc ,运行：

```
➜  ~  ipython
Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46)
Type "copyright", "credits" or "license" for more information.

IPython 4.1.0-dev -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```
搞定！

## 小结
千万别视而不见！



