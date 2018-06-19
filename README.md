Flasky
==========
This repository contains the source code learning from Flask Web Development.

##第一部分  Flask简介

###第一章：安装
###第二章：程序的基本结构
###第三章：模板
###第四章：Web表单
###第五章：数据库
###第六章：电子邮件
###第七章：大型程序的结构


##第二部分  实例：社交博客程序

###第八章：用户认证
###第九章：用户角色
###第十章：用户资料
###第十一章：博客文章
###第十二章：关注者
###第十三章：用户评论
###第十四章：应用编程接口


##第三部分  成功在望

###第十五章：测试
###第十六章：性能
###第十七章：部署
###第十八章：简介

##写在前面：
###6.16
	按照作者的代码 已成功部署到Heroku服务器上，可直接访问 
	Website: https://flask-web-01.herokuapp.com/  
		//欢迎访问此网站，注册用户需验证邮箱，如果嫌麻烦，可以使用账户 276434920@qq.com 密码 123 登陆体验
	Github:  https://git.heroku.com/flask-web-01.git
	算是了解了一下利用Flask开发web application的流程 

###6.19
	前两天端午，自己也偷偷休息了下，没做什么有效的工作
	今天将笔记整理了下，上传到GitHub，网站肯定需要润色，但接下来准备找工作，所以可能需要对之前所学的知识点做个总结，再刷一些面试题，之后等工作落定后再修改网站，添加一些新的功能

###单词缩写
	Pro：Problem
	Ans：Answer
	Sum：Summary
	Ps：Postscript
	Rs：Reference source

##每日记录：

#6.7
(venv) Mac:Flask_Web Heaven$ export FLASKY_ADMIN = <304090717@qq.com>
报错：-bash: syntax error near unexpected token 'newline' 脚本中有特殊字符？去掉<>
https://stackoverflow.com/questions/5134399/bash-syntax-error-near-unexpected-token-newline/
https://blog.csdn.net/langjijianghu_123/article/details/78974466
Mac 系统，如果只在终端使用 export 这个命令写入环境变量，它配置的只是临时变量，不能长期保存，电脑开关机后或重新打开终端或另开一个窗口，仍然会回到没有配置环境变量的状态。

Mac中的环境变量 https://blog.csdn.net/waneto2008/article/details/52486433
	etc/profile 系统级别的环境变量
	~/.bash_profile 用户级别的环境变量 

	导入变量：export MAIL_USERNAME=30490717@qq.com 
	查看变量：echo $MAIL_USERNAME 

flask-mail的邮箱配置问题 https://blog.csdn.net/lagelangzhi/article/details/51717433
配置邮箱发送邮件需要去设置里开启邮箱的SMTP服务，并通过短信获取服务提供商的发送的密码，此处使用了QQ邮箱
新密码：ahvtapoodpuscafb （不再是QQ原始密码）（Ps：此密码已修改，最新密码保存在本地主机中）

linux 怎么将一个文件夹移入另一个文件夹 
	mv old_directory/ new_directory/ 没有指定具体值则将此文件夹一起移走

@property装饰器把方法变成属性便于调用

6.8

python manage.py runserver --> ValueError: urls must start with a leading slash
解决：路由注册时忘记加上'/‘ url_prefix='/auth'而不是'auth'

---email = db.column(db.String(64), unique=True, index=True)
	TypeError: column() got an unexpected keyword argument 'unique'
暂时先去掉了unique 和 index 两项
之后在 Python shell 中新建用户
	email='heaven@gmail.com',username='Heaven',password='123')
	email='zero@123.com',username='zero',password='123'
提示 AttributeError: 'String' object has no attribute 'lower'
回到代码中查看，发现 email = db.column(db.String(64)，unique=True, index=True)
一个小小的错误 可能就是几个小时的时间 仔细看看 column-->Column 还有这个逗号，也错了


SQLAlchemy sqlite

在Python shell中新建用户提示没有这张表

---InvalidRequestError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (sqlite3.OperationalError) no such table: users [SQL: u'INSERT INTO users (username, role_id, password_hash) VALUES (?, ?, ?)'] [parameters: ('Heaven', None, 'pbkdf2:sha256:50000$1lXaaAUe$26d3996391b079f20df978dd6b944516df194115760d939ef2e55e1ea2f29977')] (Background on this error at: http://sqlalche.me/e/e3q8)
解决办法：python manage.py db upgrade 
有时直接使用无效 还需要创建迁移脚本 python manage.py db migrate -m"initila migration"

---小结：每次对数据库模型做了修改（models.py），需要创建迁移脚本，然后将数据库更新到最新版本


从昨晚到现在 花了五六个小时 主要解决了两个错误 一是拼写 二是没有创建数据库迁移脚本

Pro：使用 git status 时出现 Untracked files 和 Modified，这两种状态有什么区别
Ans：
Untracked files 有可能是新增的文件 之前没有记录 所以是未跟踪
Modified 则是之前有记录的文件，做了修改

6.9

Tip：单元测试 python manage.py test 可以发现程序中的一些错误

Pro：创建迁移脚本时提示 
	py:69: UserWarning: Skipping unsupported ALTER for creation of implicit constraint warnings.warn(msg)
Ans：中间不小心误删了一个迁移数据库（导致后面部署到服务器时还出现了问题）

Pro：运行程序 python manage.py runserver,提示
---raise SMTPAuthenticationError(code, resp)
---SMTPAuthenticationError: (535, 'Error:\xc7\xeb\xca\xb9\xd3\xc3\xca\xda\xc8\xa8\xc2\xeb\xb5\xc7\xc2\xbc\xa1\xa3\xcf\xea\xc7\xe9\xc7\xeb\xbf\xb4: http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256')

Ans：
一直没有成功发送邮件 想了半天 环境变量也没问题 多次设置了 也去shell里尝试发送邮件 还是不行 猜测有两种原因 一是在手机上点了什么服务器之类的 使授权码失效 二是配置环境变量的时候没加'' 直接输入的字符串 猜测是第二种原因，重新设置环境变量，问题解决  

Sum：出现问题要学会分析  一是看shell报什么错 从前往后看 最后一句都给了一个网站 登陆这个网站看看什么原因 就知道是授权码的问题 二是熟悉了python manage.py shell的使用 对这个shell的作用有了一定的了解  比如输入os.environ.get('MAIL_PASSWORD') 可以得到一个值 

6.10

Pro：发现作者在 修改密码 这一步没有验证新密码是否和原密码相同这个问题 自己加上了这部分代码 

Pro：为什么有两个resetpassword表单

Pro：单元测试 python manage.py test 报错
----BuildError: Could not build url for endpoint 'auth.password_reset, token=token, _external=True'. Did you mean 'auth.password_reset_request' instead?

Ans：找到源代码
if not current_user.is_anonymous:
		return redirect(url_for('main.index'))
没发现错误，继续查找
<p>To reset your password <a href="{{ url_for('auth.password_reset', token=token, _external=True) }}">click here</a></p>  
发现问题 </a>.</p> 这中间有个点没加上 一直找不到正确的链接 -Ps:这个点的作用还没查到？

6.11

last_seen 上次登录时间 这个功能是怎么实现的tou

Pro：运行程序报错
	AttributeError: 'SQLAlchemy' object has no attribute 'Datetime' 
Ans：Datetime --> DateTime

Pro:添加了头像，但一直报错
	NameError: global name 'dafault' is not defined 可能是拼错了？
	python manage.py test 也报错  
Ans：将identicon 改成 retro 测试没问题了
再改回来 几个头像都能正常显示 除了blank
虽然默认值一样 但不同邮箱的头像是不一样的


Pro：<div class="post-thumbnail">
			<a href="{{ url_for('.user', username=post.author.username) }}"></a>
		</div>
定义这个块有什么作用啊

Pro：AttributeError: 'AnonymousUserMixin' object has no attribute 'can'
Ans：login_manager.anonymous_user = AnonymousUser 这句话漏掉了，新登录用户默认为匿名用户


Pro：头像跟数据一直重叠在一起 无法正常显示 
Ans：换个浏览器就好了  一直在检查 花了一两个小时 还是没检查出原因 后来搜索别人做这一部分，也遇到了这样的问题，给出了方案
搜索词 min-height: 260px; 	margin-left: 280px 找到了别人跟着教程做的记录 最终发现了原因所在

6.12

Sum：
Profile pages 资料页
blog posts 博客文章

Pro：
	main/ auth/ 为什么需要两个文件夹
	独立模板 局部模板 _posts.html 

Pro：生成虚拟用户和文章
>>>User.generate_fake(100)
>>>Post.generate_fake(100)
第一句话没问题 运行post..报错
OperationalError: (sqlite3.OperationalError) database is locked [SQL: u'INSERT INTO posts (body, timestamp, author_id) VALUES (?, ?, ?)'] [parameters: (u'Sed sagittis.', '2018-06-10 00:00:00.000000', 66)] (Background on this error at: http://sqlalche.me/e/e3q8)

Ans:登陆提供的网站
u'Ut at dolor quis odio consequat varius.


    @staticmethod
    def generate_fake(count=10):
        from random import seed, randint
        import forgery_py
        from sqlalchemy.exc import IntegrityError

        seed()
        user_count = User.query.count()
        u = User.query.offset(5).first()
        p = Post(body=forgery_py.lorem_ipsum.sentence(),timestamp=forgery_py.date.date(True), author=u)
        db.session.add(p)
        db.session.commit()

搞了半天不清楚什么原因 然后运行 User.generate_fake(100)也报错 猜测是之前运行这个命令时 有某个进程在数据库没有正常关闭 重启命令行 再运行就OK了  我服  花我一个多小时

Pro:
<span class="label lable-primary">Edit</span>
<span class="label label-danger">Edit [Admin]</span>
<span class="label label-default">Permalink</span>

这几行代码间的 lable-primary label-danger label-default有什么区别

Ans：代表不同的标签 有一个一直没正确显示 原来是label拼成了lable c

6.13

Sum：为了实现数据库中多对多的关系，需要引入第三个表--关联表，通过SQLAlchemgy可以很快速的生成关联表，但是不能自定义添加额外的信息（如日期），所以必须提升关联表的地位，使其变成程序可以放访问的模型

Pro： 
FAIL: test_follows (test_user_model.UserModelTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/Heaven/Flask_Web/tests/test_user_model.py", line 156, in test_follows
    self.assertFalse(u1.is_following(u2))
AssertionError: True is not false

Ans：first()  把括号弄丢了


Sum：
@property装饰器 把一个方法变成属性 可以做一些限制 又方便调用 
@staticmethod python 内置函数 让类不用实例化就可以调用该方法
class a:
	@staticmethod
	def f():
		...
可以使用 a.f()来调用 也可 a().f() 

Pro：
db.event.listen(Comment.body, 'set', 'Comment.on_changed_body') 多了一个引号 四处寻找原因

Ans：比较了一边代码 没发现 重启termainal browser 没用 运行python manage.py shell 
from .models import Comment
m = Comment()
m.body = 'dd' TypeError: 'str' object is not callable
m.body_text = 'ff' 正常
去查看models 发现了问题

url_for 不是直接链接到 @main.route  而是链接到函数？>>>查阅后知，传入参数是函数名，生成的是函数对应的URL
Tip： url_for('.index',name=name,_external=True) 	传入视图函数名作为参数返回url,将动态部分作为关键字参数，第三个参数表示绝对地址

disabled的值表示能否正常显示评论内容 设为True后就不能显示评论内容了 moderator的作用就是禁止一些评论 而非修改评论 

Sum：
	json.dumps()将Python dict对象序列化为json对象 
	json.loads()将json对象序列化为dict 对象 
	如果是对文件进行操作 去掉s
	Serializer() 序列化
	jsonify() 使用了json.dumps()方法 返回的格式为 application/json
	json.dumps() 返回的content-type: text/html; 

colorama==0.2.7 这个包暂时不写


Pro：ImportError: No module named api_1_0 
Ans：试了 .api_1_0 api_1_0 app.api_1_0
	api_1_0 里的初始化文件写成了 __init.py 漏了斜杠


Pro: http --json --auth '304090717@qq.com':'123' GET http://127.0.0.1:5000/api/v1.0/posts
报错：
http: error: ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: /api/v1.0/posts (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x109364190>: Failed to establish a new connection: [Errno 61] Connection refused',)) while doing GET request to URL: http://127.0.0.1:5000/api/v1.0/posts

Ans: HTTPie测试web服务时，要先启动服务器，再执行执行测试代码。打开两个cmd界面就行了。


Sum: api_1_0 中没有views.py 是怎么处理路由的 不是根据文件夹 虽然把相同前缀的路由都放在同个文件夹中 但是出路路由还是根据 @api.route('../..') 这个路径来的 跟文件夹没关系(尝试把 posts/ 放在 users/ 文件夹中 还是能够正常处理) 所以处理路由是在文件夹中逐个寻找的 

Pro: 运行 http://localhost:5000/api/v1.0/posts/55  报错
	TypeError: <bound method Post.to_json of <Post 55>> is not JSON serializable
	报的不是 Not Found 这个错 说明此文章存在 是代码出错

Ans：return jsonify(post.to_json) 中json()括号掉了


Pro：试了下几个路由 都能走通 目前不太理解这个API是干嘛用的? 是不是比如main下的路由通过web browser浏览的路由 通过手机端或平板端浏览需要进行一些处理 这个API就是处理的那部分过程 比如客户端只接受JSON 不接受HTML作为响应 就把响应全部处理程JSON对象再返还给用户？

test_404 (test_api.APITestCase) ... ok
test_anonymous (test_api.APITestCase) ... ERROR
test_bad_auth (test_api.APITestCase) ... ok
test_comments (test_api.APITestCase) ... ERROR
test_no_auth (test_api.APITestCase) ... ERROR
test_posts (test_api.APITestCase) ... FAIL
test_token_auth (test_api.APITestCase) ... ERROR
test_unconfirmed_account (test_api.APITestCase) ... ok
test_users (test_api.APITestCase) ... ok


test_anonymous (test_api.APITestCase) ... ERROR
TypeError: The view function did not return a valid response. The function either returned None or ended without a return statement.


test_comments (test_api.APITestCase) ... ERROR
AttributeError: type object 'Comment' has no attribute 'from_json'
这个方法漏写了 补上 ok



test_no_auth (test_api.APITestCase) ... ERROR

test_posts (test_api.APITestCase) ... FAIL
Traceback (most recent call last):
  File "/Users/Heaven/Flask_Web/tests/test_api.py", line 125, in test_posts
    self.assertTrue(response.status_code == 400)
AssertionError: False is not true
换成401 403 404 都不行 加上一句 print response.status_code 结果为201 正确插入了 研究代码 发现
if body is None and body == '':
    raise ValidationError('post does not have a body')
此处应该是 or 而非 and 
  File "/Users/Heaven/Flask_Web/app/api_1_0/posts.py", line 49, in edit_post
    if f.current_user != post.author and not g.current_user.can(Permission.ADMINISTER):
NameError: global name 'f' is not defined
	if f.current_user != post.author and not g.current_user.can(Permission.ADMINISTER): 
将 f 改成 g   ok 


test_token_auth (test_api.APITestCase) ... ERROR
 File "/Users/Heaven/Flask_Web/app/api_1_0/authentication.py", line 15, in verify_password
    g.current_user = User.verify_password(email_or_token)
TypeError: unbound method verify_password() must be called with User instance as first argument (got str instance instead)
	g.current_user = User.verify_password(email_or_token) -->User.verify_auth_password(email_or_token)

    g.current_user = User.verify_auth_password(email_or_token)
AttributeError: type object 'User' has no attribute 'verify_auth_password'
--->verify_auth_token

这三个错误都变成 TypeError: The view function did not return a valid response. The function either returned None or ended without a return statement.

经分析 找到 def get_posts():
	if pagination.has_next:  next-->prev


将api/posts.py 文件直接复制过来 发现全部OK了 说明肯定哪里拼错了 
	return jsonify({
			'posts': [post.to_json() for post in posts],
			'prev': prev,
			'next': next,
			'count': pagination.total
			})
这个缩进有问题   放在 if pagination.has_next() 里去了 结果只有下页时才有返回值

Sum：这些错误都是拼写的错误 真的要注意 

Pro：
加入 selenium 后测试跳过了 test_admin_home_page (test_selenium.SeleniumTestCase) ... skipped 'Web browser not available'

Ans：
是因为默认的是firefox() 无法启动 直接将 webdriver.Firefox()-->webdriver.Chrome()/Safari() 是没有用的 因为火狐浏览器原生支持selenium  Chrome 和 Safari 需要下载插件和配置
去 http://npm.taobao.org/mirrors/chromedriver/ 下载最新版的chromedriver 解压后移入/usr/local/bin 不要写入/usr/bin(此操作也不允许 管理员权限都不行 也没必要)

Pro：Traceback (most recent call last):
  File "/Users/Heaven/Flask_Web/tests/test_selenium.py", line 78, in test_admin_home_page
    self.client.page_source))  Hello,\s+Stranger'
AssertionError: None is not true

Ans：没匹配上 所以返回None 去掉！即可 跟+没关系 

Sum：加上selenium 进行测试 服务器线程总是不能正常关闭 都是手动 kill 

Sum：性能
	缓慢数据库查询 部署在生产环境中 默认是在开发环境 需要修改 记录保存在日志中 需要配置日志记录器
	分析源码 由于会影响程序运行的时间 配置在开发阶段
	python manage.py profile 启动服务 并检测各部分程序运行时间

Tip：在 heroku.com 注册账号验证码一直不出来 需要翻墙 才能刷新验证码  邮箱最好用gmail
	Rs：https://blog.csdn.net/while10/article/details/79053563


6.15/6.16

Sum：购买了一些工具，成功注册Heroku账号，此处不提

Pro：将实例代码推送到heroku上时,提示
	remote: -----> Installing python-3.6.5
	remote: -----> Installing pip
自动下载了一些包 这个是怎么实现的

Ans：根据需求文件requirems来实现的，自动安装其中提到的包

Pro：运行 pipenv install 报错：
	raise ValueError('unknown locale: %s' % localename)
	ValueError: unknown locale: UTF-8

Ans：在~./bash_profile 加入
	export LC_ALL=en_US.UTF-8
	export LANG=en_US.UTF-8
然后重新打开要运行 pipenv install这个命令的窗口 运行即可

Tip：pipenv shell进入虚拟环境

Pro：先下载 Postgres 安装 然后在命令行输入
	sudo mkdir -p /etc/paths.d && echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp

Mac:python-getting-started Heaven$ psql -h localhost
psql: could not connect to server: Connection refused
	Is the server running on host "localhost" (127.0.0.1) and accepting
	TCP/IP connections on port 5432?
could not connect to server: Connection refused
	Is the server running on host "localhost" (::1) and accepting
	TCP/IP connections on port 5432?

Ans：PostgreSQL 服务未启动 进入 /Applications/Postgres.app/Contents/Versions/10/bin/psql 启动服务器

Tip：Procfile 规定用哪个命令启动程序
	Created postgresql-concentric-49098 as DATABASE_URL


Pro：git push heroku master 后创建的是python3.6 会有影响不 本地是2.7
Ans：有影响，后面会提到

Pro：运行  heroku run python manage.py deploy 报错：
	sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: users
[SQL: 'ALTER TABLE users ADD COLUMN email VARCHAR(64)'] (Background on this error at: http://sqlalche.me/e/e3q8)

Ans：修改
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')
---> 去掉TEST 把生产环境和测试环境的数据库设置成一样的了

Pro：修改后继续部署 报错：
	sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) relation "users" does not exist
[SQL: 'ALTER TABLE users ADD COLUMN email VARCHAR(64)'] (Background on this error at: http://sqlalche.me/e/f405)

Ans:
数据库迁移是一步步来的 最开始的时候 猜测是在最开始不懂迁移的时候把数据库迁移文件给误删了 现在我的第一个迁移文件不是创建users表 所以后面的迁移都无法进行 有两种解决方案
	1.全部删掉 重新在本地创建后上传 创建完整的模型
	2.补上删掉的users表 

先尝试第一种方案 将迁移记录全部删掉后 尝试重新生成新的文件 python manag.py db upgrade -m"the completed db" 
报错：alembic.util.exc.CommandError: Can't locate revision identified by '27474b5b9239'
	这个数字是最后一个迁移文件的编号 表名还是有记录存储在某个地方 所以猜测数据库迁移不是从前往后更新的 而是从后往前追溯定位的 最后一次的编号存储在了某个地方

现在尝试第二种方案 去作者的 github 上找到误删的那份记录 添加到本地 然后纠正一些编号 继续迁移更新
报错：alembic.util.exc.CommandError: Target database is not up to date.
把自己的原始 initial.py 这个文件删掉后一切正常  这个文件本来就是多余的 以为没什么影响就留着了 看来还是有影响



Pro：启动服务后 一切正常 连接该目标网址时显示界面错误 查看日志 heroku logs 显示

	__import__(module)
	2018-06-16T05:17:56.401164+00:00 app[web.1]: ModuleNotFoundError: No module named 'flasky'


Ans： from . import config ---> import config 修改后错误还在

File "/app/.heroku/python/lib/python3.6/site-packages/gunicorn/util.py", line 350, in import_app
 __import__(module)
 ModuleNotFoundError: No module named 'flasky'

猜测是不是受版本的影响，在Python3 中flasky跟Python2中不同 于是新增了一个 runtime.txt 文件夹 指定了创建的版本 
	Rs：https://blog.csdn.net/BenBoy007/article/details/79504494

这次显示创建的是Python2.7  但还是提示没有flasky 而且出现了另外一个问题
 	The latest version of Python 2 is python-2.7.15 (you are using python-2.7.10, which is unsupported).
	remote:  !     We recommend upgrading by specifying the latest version (python-2.7.15).
	remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes

UserWarning: The psycopg2 wheel package will be renamed from release 2.8;  Ps:改成2.8后还报错 没有这个版本 改回2.7.4 忽略此条语句

不停地修改 测试 查看日志 没解决问题 后换个关键词搜索 用 worker-failed-to-boot搜索 发现一篇文章
https://stackoverflow.com/questions/24488891/gunicorn-errors-haltserver-haltserver-worker-failed-to-boot-3-django
打开自己的Procfile 显示 web: gunicorn flasky:app  将flasky改成manage 问题解决

这两天工作
Procfile 修改了app
migrations 补上了前面误删的文件
runtime.txt 指定了服务器端python的代码
git push heroku master  每次都会重新下载安装 且名字要指定
config.py 修改了ProductionConfig里的DATABASE_URI
部署到服务器时python使用最新2.7.15 不需要使用本地的Python2.7.10
创建了新的文件夹 以及git仓库

一些参考网站

部署学习网站 
	https://devcenter.heroku.com/articles/getting-started-with-python#view-logs
	https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

pipenv 在本地模拟服务器端的app时才会用到 和 postgresql 一样
	https://www.jianshu.com/p/00af447f0005


