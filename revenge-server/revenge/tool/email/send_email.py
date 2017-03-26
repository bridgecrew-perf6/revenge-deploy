#coding:utf-8

from django.template import loader
from django.core.mail import EmailMultiAlternatives

class KQEmail:
    def __init__(self, subject, receiver):
        self.__subject = subject
        self.__receiver = receiver
        self.__fail_silently = False

    def send_email(self, template_name, attributes):
        body = loader.render_to_string(template_name, attributes)
        kq_email = EmailMultiAlternatives(subject=self.__subject,
                                          body=body,
                                          from_email=None,
                                          to=self.__receiver)
        kq_email.content_subtype = "html"
        kq_email.send(self.__fail_silently)





