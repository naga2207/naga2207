# Generated by Django 4.2.4 on 2023-08-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0006_user_registration_alter_task_manage_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('si_num', models.PositiveIntegerField(auto_created=True, unique=True)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='task_manage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager_app.registration'),
        ),
        migrations.DeleteModel(
            name='User_Registration',
        ),
    ]