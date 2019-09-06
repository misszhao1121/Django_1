from django.core.mail import send_mail
import  time

class sendmail():
    def __init__(self,receive_addr,sub_info,content_info):
        sub_date = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())  #定义时间
        self.receive_addr = receive_addr
        self.sub_info = sub_info + sub_date
        self.content_info = content_info
# 发送邮件方法
    def send(self):
        try:
            send_mail(
                subject=self.sub_info,
                message=self.content_info,
                from_email='542275297@qq.com',
                recipient_list=self.receive_addr,
                fail_silently=False,
            )
            return True
        except Exception as  e:
            print(e)
            return  False
