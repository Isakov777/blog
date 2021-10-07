# Generated by Django 3.2.7 on 2021-10-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(to='posts.Post', verbose_name='tags')),
            ],
        ),
    ]
