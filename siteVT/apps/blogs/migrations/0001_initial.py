# Generated by Django 3.0.4 on 2020-03-20 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_full_name', models.CharField(max_length=50, verbose_name='full_name')),
                ('p_information', models.TextField(verbose_name='Information')),
                ('p_date_birth', models.DateTimeField(verbose_name='published')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=15, verbose_name='from')),
                ('s_percent', models.DecimalField(decimal_places=2, max_digits=3)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ed_start', models.CharField(max_length=4, verbose_name='from')),
                ('ed_end', models.CharField(max_length=7, verbose_name='to')),
                ('ed_place', models.CharField(max_length=200, verbose_name='Place')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_start', models.CharField(max_length=4, verbose_name='from')),
                ('e_end', models.CharField(max_length=7, verbose_name='to')),
                ('e_place', models.CharField(max_length=200, verbose_name='Place')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Person')),
            ],
        ),
    ]
