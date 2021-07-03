# Generated by Django 3.2.5 on 2021-07-03 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clareza', models.IntegerField(default='12')),
                ('rigor', models.IntegerField(default='12')),
                ('precisao', models.IntegerField(default='12')),
                ('profundidade', models.IntegerField(default='12')),
                ('amplitude', models.IntegerField(default='12')),
                ('logica', models.IntegerField(default='12')),
                ('significancia', models.IntegerField(default='12')),
                ('originalidade', models.IntegerField(default='12')),
                ('sugestao', models.TextField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default='5')),
                ('comment', models.TextField(default='', max_length=400)),
                ('postedTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommonUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('accessToken', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('subject', models.CharField(default='', max_length=200)),
                ('message', models.TextField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefas.commonuser')),
            ],
        ),
        migrations.CreateModel(
            name='Networking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('surname', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('typeOfUser', models.BooleanField(choices=[(True, 'Guide'), (False, 'Tourist')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('satisfaction', models.IntegerField(default='5')),
                ('destination', models.CharField(max_length=200)),
                ('visitDate', models.DateField(blank=True, null=True)),
                ('groupSize', models.IntegerField(blank=True, null=True)),
                ('useAgain', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='QuizzAval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout', models.CharField(max_length=200)),
                ('beAguide', models.BooleanField(choices=[(True, 'Sim!'), (False, 'Siiiim!')])),
                ('numberOfApps', models.IntegerField()),
                ('percentageOfPay', models.IntegerField()),
                ('availablePlataforms', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('howManyDevs', models.IntegerField()),
                ('animations', models.IntegerField()),
                ('audioQuestion', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])),
                ('disciplina', models.CharField(max_length=200)),
                ('diff', models.IntegerField(default='12')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfLikes', models.ManyToManyField(blank=True, to='tarefas.Like')),
            ],
        ),
    ]
