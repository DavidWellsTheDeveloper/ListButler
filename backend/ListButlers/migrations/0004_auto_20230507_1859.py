# Generated by Django 2.2.12 on 2023-05-07 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ListButlers', '0003_listitem_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='owner',
        ),
        migrations.AlterField(
            model_name='listitem',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='ListButlers.List'),
        ),
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.BooleanField(default=False)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_users', to='ListButlers.List')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]