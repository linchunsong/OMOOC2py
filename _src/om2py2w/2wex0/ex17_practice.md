# 拼写错误的解决办法
## 问题
```
➜  Practice  cat test.txt
liukai
hen
zhuai
➜  Practice  pyhton ex17.py test.txt mew-file.txt
zsh: command not found: pyhton
➜  Practice  python ex17.py test.txt mew-file.txt
Copying from test.txt to mew-file.txt
The input file si 17 bytes long
Does the output file exists? True
Ready, hit RETURE to continue, CTRl-C to abort.

Traceback (most recent call last):
  File "ex17.py", line 19, in <module>
    out_file.write(indata)
NameError: name 'indata' is not defined  
````
根本就不清楚defined是啥意思，好吗？啥叫没有定义呢？		
## 尝试
然后在网上看了下原版的ex17.py发现可以运行。

```
➜  Practice  python ex1701.py test.txt mew-file.txt
Copying from test.txt to mew-file.txt
The input file is 17 bytes long
Does the output file exist? True
Ready, hit RETURN to continue, CTRL-C to abort.

Alright, all done.
➜  Practice  cat mew-file.txt
liukai
hen
zhuai
```
自己的再试试

```
➜  Practice  python ex17.py test.txt mew-file.txt
Copying from test.txt to mew-file.txt
The input file si 17 bytes long
Traceback (most recent call last):
  File "ex17.py", line 14, in <module>
    print "Does the output file exist? %r" % exist(to_file)
NameError: name 'exist' is not defined
➜  Practice  python ex17.py test.txt mew-file.txt
Copying from test.txt to mew-file.txt
Traceback (most recent call last):
  File "ex17.py", line 12, in <module>
    print "The input file si %d bytes long" % len(indata)
NameError: name 'indata' is not defined

```
一行一行对照着看代码有没拼写错误，发现14行引号里的exisits多了一个s，
Ctrl+F，所有exisits都改掉，又出别的问题了。然后启发了我，是不是indata也错了，Ctrl+F搜索，发现的确有个写错了。

```
➜  Practice  python ex17.py test.txt mew-file.txt
Copying from test.txt to mew-file.txt
The input file si 17 bytes long
Does the output file exist? True
Ready, hit RETURE to continue, CTRl-C to abort.

Alright, all done.
```
## 小结：
遇到拼写错误后，Ctrl+F，所有的都检查一遍。