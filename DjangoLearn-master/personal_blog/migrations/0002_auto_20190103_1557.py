# Generated by Django 2.1.4 on 2019-01-03 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_time'], 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
    ]
