from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myschool_app.models import Teste

# 50% funcional: prevenção de utilizadores duplicados
# e envio para a caixa de spam


def run():
    for teste in Teste.objects.filter(data=date.today() + relativedelta(days=4)):
        email_html = render_to_string('myschool_app/app/emails/lembrete_testes.html', {
                                      'utilizador': teste.utilizador, 'teste': teste})
        email_simples = strip_tags(email_html)
        remetente = 'mySchool <info@myschool-app.tk'

        send_mail('Notificação de testes pendentes', email_simples, remetente, [
                  teste.utilizador.email], html_message=email_html)
