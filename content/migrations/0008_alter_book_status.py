# Generated by Django 4.2.5 on 2023-09-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sell', 'sell')], default='available', max_length=50, null=True),
        ),
    ]
