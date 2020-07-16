# Generated by Django 3.0.8 on 2020-07-16 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200716_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название тега')),
            ],
        ),
        migrations.AlterField(
            model_name='ad',
            name='img_src',
            field=models.FileField(null=True, upload_to='items'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='tag',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='goods.Tags'),
        ),
    ]
