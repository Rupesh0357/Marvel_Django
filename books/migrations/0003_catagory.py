# Generated by Django 3.2.3 on 2021-06-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('discription', models.CharField(default='', max_length=400)),
                ('image', models.ImageField(upload_to='uploads/products')),
            ],
        ),
    ]
