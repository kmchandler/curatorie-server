# Generated by Django 4.1.5 on 2023-02-22 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShareRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='SharedBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('priority', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='ListCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_item', models.TextField(max_length=1000)),
                ('priority', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='InspoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('priority', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('occasion', models.CharField(max_length=50)),
                ('gift_for', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('priority', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='BoardType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.board')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curatorieapi.user'),
        ),
    ]
