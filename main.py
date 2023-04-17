

# flask实例文件代码：
from flask import Flask
# 导入配置类
from settings import Defaultconfig
# 导入Baseconverter
from werkzeug.routing import BaseConverter
from flask import request
main = Flask(__name__)
# 从配置对象中加载配置
main.config.from_object(Defaultconfig)
@main.route('/')
def index():
    # get方式调用配置
    mysql_port = main.config.get('MYSQL_PORT')
    print(mysql_port)
    # 字典键值方式调用配置
    mysql_host = main.config['MYSQL_HOST']
    print(mysql_host)
    return 'load config from object'
#
# @main.route('/user/<user_id>')
# def get_id(user_id):
#     print(user_id)
#     print(type(user_id))
#     return '这是用户页面'


@main.route('/user/<int:user_id>')
def get_id(user_id):
    print(user_id)
    print(type(user_id))
    return '这是用户页面'


# 自定义converte类
class phoneconverter(BaseConverter):
    regex = r'1[3-9]/d{9}'  # 不可加^ 和 $
# 添加至converters容器
main.url_map.converters['phone'] = phoneconverter


@main.route('/user/phone/<phone:phone_num>')
def get_phone(phone_num):
    print(phone_num)
    print(type(phone_num))
    return '这是用户电话页面'




# 使用自定义转换器
@main.route('/user/<phone:user_id>')
def user_info(user_id):
    return user_id


@main.route('/h', methods=['post'])
def login():
    # 获取from表单中的用户名
    username = request.form.get('uname')
    # 获取form表单中的密码
    password = request.form.get('pwd')
    # 用户名与密码的判断
    if username == 'admin' and password == 'admin123':
        return '登录成功'
    else:
        return '登录失败'


# 创建Flask实例对象
# main = Flask(__name__)

@main.route('/up', methods=['POST'])
def upload_file():
    # 获取前端传递过来的文件对象
    img = request.files.get('pic')
    # 获取文件对象的文件名
    file_name = img.filename
    # 保存文件对象
    img.save(file_name)
    return '上传成功!'

if __name__ == '__main__':
    main.run()

