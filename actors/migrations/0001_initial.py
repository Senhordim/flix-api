# Generated by Django 5.1 on 2024-08-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('USA', 'United States'), ('UK', 'United Kingdom'), ('IND', 'India'), ('AUS', 'Australia'), ('CAN', 'Canada'), ('JPN', 'Japan'), ('FRA', 'France'), ('GER', 'Germany'), ('ITA', 'Italy'), ('RUS', 'Russia'), ('CHN', 'China'), ('BRA', 'Brazil'), ('MEX', 'Mexico'), ('ARG', 'Argentina'), ('ESP', 'Spain'), ('POR', 'Portugal'), ('SWE', 'Sweden'), ('NOR', 'Norway'), ('DEN', 'Denmark'), ('FIN', 'Finland'), ('NED', 'Netherlands'), ('BEL', 'Belgium'), ('LUX', 'Luxembourg'), ('IRL', 'Ireland'), ('SCO', 'Scotland'), ('WAL', 'Wales'), ('NZL', 'New Zealand'), ('RSA', 'South Africa'), ('KEN', 'Kenya'), ('NGA', 'Nigeria'), ('EGY', 'Egypt'), ('ISR', 'Israel'), ('JOR', 'Jordan'), ('KSA', 'Saudi Arabia'), ('UAE', 'United Arab Emirates'), ('QAT', 'Qatar'), ('OMA', 'Oman')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
