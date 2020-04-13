from django.contrib.auth.models import User


def run():
    with open('sendgrid_export.csv', 'w') as csv:
        cabecalho = 'username,first_name,last_name,email\n'
        csv.write(cabecalho)
        for user in User.objects.all():
            d = f'{user.username},{user.first_name},{user.last_name},{user.email}\n'
            csv.write(d)
