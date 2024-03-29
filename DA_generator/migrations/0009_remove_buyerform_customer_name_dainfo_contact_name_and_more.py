# Generated by Django 4.2.6 on 2023-10-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DA_generator', '0008_auto_20231009_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyerform',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='dainfo',
            name='contact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dainfo',
            name='customer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyerdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='buyerform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dainfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='srinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
