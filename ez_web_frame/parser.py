
import re

class ClientRequestParser:
        def __init__(self, data, db):
                """
                The `data` is string from client side!
                """
                try:
                        pattern = re.compile(r'(?P<method>.*)/(?P<command>.*)/(?P<status>.*)')
                        m = pattern.match(data)
                        self.request_data=m.groupdict()
                        self.request_method = self.request_data.get('method','No Key Found')
                        self.db=db
                except :
                        print('输入的命令有误')
                        self.request_method = 'no method'


        def get(self, db, task_id):
                response = db.get(task_id,'未找到Key')
                return response

        def post(self,db, command):
                pattern = re.compile(r'(?P<key>.*)=(?P<value>.*)')
                m = pattern.match(command)
                post_data = m.groupdict()
                key=post_data.get('key','未找到Key')
                value=post_data.get('value','未找到Key')
                db[key]=value
                response='请求成功'
                return response


        def response(self):
                response=''
                if self.request_method  == 'GET':
                        print('Get method')
                        task_id=self.request_data.get('command','未找到Key')
                        response=self.get(self.db, task_id)
                elif self.request_method == 'POST':
                        command=self.request_data.get('command','未找到Key')
                        response=self.post(self.db, command)
                else:
                        response = '错误的请求方式'

                response=response+'\r\n'
                # return response
                return self.make_response(response)

        def make_response(self, response):
                """
                给服务器给浏览器发送一个响应添加内容
                绝对路径自己改下-.-
                :param response:
                :return:
                """
                with open('/Users/a00301955/Documents/fun_test/little-case-of-python/ez_web_frame/response.txt') as p:
                        response = p.read()
                return response

