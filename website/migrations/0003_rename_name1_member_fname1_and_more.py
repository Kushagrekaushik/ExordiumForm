# Generated by Django 4.2.6 on 2023-10-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_member_tname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name1',
            new_name='Fname1',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name2',
            new_name='Fname2',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name3',
            new_name='Lname1',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name4',
            new_name='Lname2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email3',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email4',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone3',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone4',
        ),
        migrations.RemoveField(
            model_name='member',
            name='roll1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='roll2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='roll3',
        ),
        migrations.RemoveField(
            model_name='member',
            name='roll4',
        ),
        migrations.RemoveField(
            model_name='member',
            name='tname',
        ),
        migrations.AddField(
            model_name='member',
            name='Q1',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Q2',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Email1',
            field=models.EmailField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Email2',
            field=models.EmailField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Phone1',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Phone2',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Roll1',
            field=models.IntegerField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='Roll2',
            field=models.IntegerField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
