ChemistryLIMS(V1.0) 是一款基于B/S架构，采用当今流行的编程语言python编写，web开发框架采用非常成熟的开源代码的Django，
Django功能强大，开发便捷，很多知名网站都是采用Django开发的。ChemistryLIMS设计模式遵循MTV， 即模型Model，
模板Template和视图View，软件强调代码复用，注重组件的重用性和“可插拔性“，注重敏捷开发和DRY（Don’t Repeat Yourself）法则。
由于Django有许多功能强大的第三方插件，从而使ChemistryLIMS具有很强的可扩展性。ChemistryLIMS能够和多种数据库连接，
这能够使有着复杂的数据处理需要的实验室信息管理系统变得简单而兼容性极强。

软件依赖环境：
需要安装python 3.0以上的版本
有关python的安装过程可自行检查python官方文档：
https://docs.python.org/3/




数据库要求：
软件自带数据库，也可使用开源数据库Mysql或其他商业数据库例如Oracle，SQL Server等。

软件的安装：
下载软件安装到电脑，解压，以windows操作系统为例，打开windows命令终端，cd到项目主目录下：
例如本机的解压安装路径为：C:\Users\86139\Llims\ChemistryLIMS

为现有项目生成依赖环境：
python -m pip install -r requirements.txt

在该目录下打开命令行终端输入：python manage.py migrate
进行数据库迁移

输入：python manage createsuperuser
按照提示输入用户名密码和邮箱创建超级管理员后继续以下步骤：
输入：python manage.py runserver 8000
打开浏览器，输入以下网址，输入刚才创建的超级用户名和密码：
http://127.0.0.1:8000/admin/

