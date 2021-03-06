# Generated by Django 2.2 on 2019-04-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workhour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DateField()),
                ('hours', models.IntegerField()),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credited_salary', models.IntegerField()),
                ('salary_date', models.DateField()),
                ('days', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.Workhour')),
            ],
        ),
    ]
