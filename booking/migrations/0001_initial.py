# Generated by Django 4.2.4 on 2023-12-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('transmition', models.CharField(choices=[('Mannual', 'Mannual'), ('Automatic', 'Automatic')], max_length=10)),
                ('engine', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Ev', 'Ev')], max_length=10)),
                ('rent', models.IntegerField()),
                ('location', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Idukki', 'Idukki'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'), ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Thrissur', 'Thrissur'), ('Wayanad', 'Wayanad')], max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/images')),
                ('discription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Maketrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Idukki', 'Idukki'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'), ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Thrissur', 'Thrissur'), ('Wayanad', 'Wayanad')], max_length=50)),
                ('dropoff', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Ernakulam', 'Ernakulam'), ('Idukki', 'Idukki'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'), ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Thrissur', 'Thrissur'), ('Wayanad', 'Wayanad')], max_length=50)),
                ('pick_date', models.DateField()),
                ('drop_date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
