# Generated by Django 3.0.8 on 2020-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('tm1', models.CharField(blank=True, max_length=100, null=True)),
                ('tm2', models.CharField(blank=True, max_length=100, null=True)),
                ('tm3', models.CharField(blank=True, max_length=100, null=True)),
                ('tm4', models.CharField(blank=True, max_length=100, null=True)),
                ('tm5', models.CharField(blank=True, max_length=100, null=True)),
                ('tm6', models.CharField(blank=True, max_length=100, null=True)),
                ('tm7', models.CharField(blank=True, max_length=100, null=True)),
                ('tm8', models.CharField(blank=True, max_length=100, null=True)),
                ('m1', models.CharField(blank=True, max_length=100, null=True)),
                ('m2', models.CharField(blank=True, max_length=100, null=True)),
                ('m3', models.CharField(blank=True, max_length=100, null=True)),
                ('m4', models.CharField(blank=True, max_length=100, null=True)),
                ('m5', models.CharField(blank=True, max_length=100, null=True)),
                ('m6', models.CharField(blank=True, max_length=100, null=True)),
                ('m7', models.CharField(blank=True, max_length=100, null=True)),
                ('m8', models.CharField(blank=True, max_length=100, null=True)),
                ('tu1', models.CharField(blank=True, max_length=100, null=True)),
                ('tu2', models.CharField(blank=True, max_length=100, null=True)),
                ('tu3', models.CharField(blank=True, max_length=100, null=True)),
                ('tu4', models.CharField(blank=True, max_length=100, null=True)),
                ('tu5', models.CharField(blank=True, max_length=100, null=True)),
                ('tu6', models.CharField(blank=True, max_length=100, null=True)),
                ('tu7', models.CharField(blank=True, max_length=100, null=True)),
                ('w1', models.CharField(blank=True, max_length=100, null=True)),
                ('w2', models.CharField(blank=True, max_length=100, null=True)),
                ('w3', models.CharField(blank=True, max_length=100, null=True)),
                ('w4', models.CharField(blank=True, max_length=100, null=True)),
                ('w5', models.CharField(blank=True, max_length=100, null=True)),
                ('th1', models.CharField(blank=True, max_length=100, null=True)),
                ('th2', models.CharField(blank=True, max_length=100, null=True)),
                ('th3', models.CharField(blank=True, max_length=100, null=True)),
                ('th4', models.CharField(blank=True, max_length=100, null=True)),
                ('th5', models.CharField(blank=True, max_length=100, null=True)),
                ('th6', models.CharField(blank=True, max_length=100, null=True)),
                ('th7', models.CharField(blank=True, max_length=100, null=True)),
                ('f1', models.CharField(blank=True, max_length=100, null=True)),
                ('f2', models.CharField(blank=True, max_length=100, null=True)),
                ('f3', models.CharField(blank=True, max_length=100, null=True)),
                ('f4', models.CharField(blank=True, max_length=100, null=True)),
                ('f5', models.CharField(blank=True, max_length=100, null=True)),
                ('f6', models.CharField(blank=True, max_length=100, null=True)),
                ('f7', models.CharField(blank=True, max_length=100, null=True)),
                ('s1', models.CharField(blank=True, max_length=100, null=True)),
                ('s2', models.CharField(blank=True, max_length=100, null=True)),
                ('s3', models.CharField(blank=True, max_length=100, null=True)),
                ('s4', models.CharField(blank=True, max_length=100, null=True)),
                ('s5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
