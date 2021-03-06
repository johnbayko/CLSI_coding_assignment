# Generated by Django 2.2.4 on 2019-08-20 01:43

from django.db import migrations, models
import django.db.models.deletion
from procurement.models import Representative


def move_representatives(apps, schema_editor):
    Supplier = apps.get_model('procurement', 'Supplier')
    for supplier in Supplier.objects.all():
        supplier.representatives.create(representative_name = supplier.representative_name, representative_email = supplier.representative_email)


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('representative_name', models.CharField(blank=True, max_length=255, null=True)),
                ('representative_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representatives', to='procurement.Supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(move_representatives),
        migrations.RemoveField(
            model_name='supplier',
            name='representative_email',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='representative_name',
        ),
    ]
