# Generated by Django 4.2.6 on 2023-10-09 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_level', models.CharField(choices=[('med', 'medical'), ('hos', 'hospital'), ('den', 'dental'), ('lab', 'laboratory')], default='med', max_length=3)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'first level category',
                'verbose_name_plural': 'first level categories',
                'ordering': ('first_level',),
            },
        ),
        migrations.CreateModel(
            name='SecondLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_level_name', models.CharField(blank=True, max_length=300)),
                ('second_sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sscategory', to='home.firstlevelcategory')),
            ],
            options={
                'verbose_name': 'second level category',
                'verbose_name_plural': 'second level categories',
                'ordering': ('second_level_name', 'second_sub_category'),
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_status', models.CharField(choices=[('p', 'published'), ('d', 'draft'), ('w', 'Withdrawn')], default='d', max_length=1)),
                ('UMDNS', models.PositiveIntegerField(blank=True, null=True)),
                ('risk_class', models.CharField(blank=True, max_length=10)),
                ('modality', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=15, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DUser', to='accounts.user')),
                ('first_level_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dfcategory', to='home.firstlevelcategory')),
                ('second_level_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dscategory', to='home.secondlevelcategory')),
            ],
            options={
                'ordering': ('first_level_category', 'second_level_category', 'name'),
                'get_latest_by': 'created',
            },
        ),
    ]
