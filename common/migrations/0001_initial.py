# Generated by Django 3.0.4 on 2020-03-23 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_author', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('question_detail', models.TextField()),
                ('question_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer_author', models.CharField(max_length=30)),
                ('Answer_text', models.TextField()),
                ('Answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Question')),
            ],
        ),
    ]
