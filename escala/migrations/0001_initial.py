# Generated by Django 3.1.7 on 2021-04-06 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ministerio', '0002_auto_20210405_2301'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('ultima_alteração', models.DateTimeField(auto_now_add=True)),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ministerio.funcao')),
            ],
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, max_length=1000, null=True)),
                ('evento', models.ManyToManyField(to='escala.Evento', verbose_name='Escala')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Responsavel')),
            ],
        ),
    ]
