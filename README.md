<img src="./logo.png" style="width:200px">

                    // Sugar //

            A minimal web framework by Python.

        Sugar tastes sweet.You feel bored when you repeat
        the CGI script and write the database code repeatedly.
        No one wants to focus on how to output Content-Type
        and to shut down the database after all operations
        have been done.So, you need a spoon of sugar liberated
        from the saccharification, repeated work.



### 框架可以运行啦!!!

下载本项目后,在Pycharm中打开.

运行manage.py 文件.

![](https://ip.freep.cn/592196/Screenshot%20from%202017-10-12%2010-46-16.png)
![](https://ip.freep.cn/592196/Screenshot%20from%202017-10-12%2010-45-48.png)
![](https://ip.freep.cn/592196/Screenshot%20from%202017-10-12%2010-46-00.png)


### 就目前来说,还是有不少问题的,比如templates和static文件夹的位置.

在sugar/__sugar__.py文件中有如下:


```
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, 'templates')
static_path = os.path.join(base_dir, 'static')
```

base_dir变量获取的是 path/sugar/ 目录,那么之后的两个变量路径是:

>  template_path -> path/sugar/templates

>  static_path   -> path/sugar/static

那么我们的templates和static这两个文件夹就必须放在path/sugar/中.
这样极大的限制了我们,如果把这个框架放进: path/python/dist-packages/ 中做库的话.
那么我们肯定是希望templates和static文件夹,放在我们的项目中而不是框架的目录中.

这是我要首先解决的一个问题.
