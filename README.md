
                    // Sugar //

            A minimal web framework by Python.

        Sugar tastes sweet.You feel bored when you repeat
        the CGI script and write the database code repeatedly.
        No one wants to focus on how to output Content-Type
        and to shut down the database after all operations
        have been done.So, you need a spoon of sugar liberated
        from the saccharification, repeated work.

- #### Python version

> Python3

- #### Use pip to install dependency Libraries

```
pip install Jinja2
```

## feature
- extensible
- URL mapping
- error handling (404,500)
- template rendering
- HttpReqeust, HttpResponse
- context
- cache

### 框架可以运行啦!!!

下载本项目后,在Pycharm中打开.

运行manage.py 文件.

![](http://img.vim-cn.com/5d/9c51a291020fe9851e794ba9a67eeef2d15e7d.png)
![](https://ip.freep.cn/592196/Screenshot%20from%202017-10-12%2010-45-48.png)
![](https://ip.freep.cn/592196/Screenshot%20from%202017-10-12%2010-46-00.png)


### 就目前来说,还是有不少问题的,比如templates和static文件夹的位置.

在sugar/\_\_sugar\_\_.py文件中有如下:

```
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, 'templates')
static_path = os.path.join(base_dir, 'static')
```

<del>base_dir变量获取的是 path/sugar/ 目录,那么之后的两个变量路径是:</del>

<del> > template_path -> path/sugar/templates</del>

<del> > static_path   -> path/sugar/static</del>

<del>那么我们的templates和static这两个文件夹就必须放在path/sugar/中.</del>
<del>这样极大的限制了我们,如果把这个框架放进: path/python/dist-packages/ 中做库的话.</del>
<del>那么我们肯定是希望templates和static文件夹,放在我们的项目中而不是框架的目录中.</del>

<del> 这是我要首先解决的一个问题. </del>

<hr>  

<del>就上面这个问题,已经有了暂时的解决方法,更改了 </del>

<del>sugar/\_\_init\_\_.py 中 base_dir 变量,使其值为上层文件夹路径.</del>
<del>所以我们的templates和static文件夹可以拿到了外面.</del>

<del>但是还是缺陷. </del>

<del>缺陷就是如果要使用这个框架就必须把这个框架放在项目中,因为很多环境的配置与那个变量base_dir有关. 所以下一步工作就是当框架文件放在任何地方的时候,项目都可以如期运行.</del>

#### 灵活性的问题解决了.