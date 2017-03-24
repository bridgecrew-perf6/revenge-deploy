# coding=utf-8

from celery import shared_task
from celery import task
from pypinyin import slug, NORMAL
from tool.email.send_email import KQEmail
from tool.general.generate_name import family_name, given_name
from tool.general.token import Token
from django.utils import timezone


@task()
def send_email_util(passport, subject, template_name, attributes):
    sec = KQEmail(subject=subject, receiver=passport)
    sec.send_email(template_name=template_name, attributes=attributes)


@shared_task
def bombTaskTime():
    fn = slug(family_name(), style=NORMAL, separator='')
    gn = slug(given_name(), style=NORMAL, separator='')
    email_suffix = ""
    passport = '.'.join([gn, fn]) + email_suffix
    print("发送给:",passport)
    token = Token().generate_md5_token_from_string(passport)
    bind_timestamp = timezone.now()
    send_email_util.delay(passport=passport,
                          subject="",
                          template_name="mail/anthrax.html",
                          attributes={'token': token,
                                      'operate_timestamp': bind_timestamp})

