from django.db import models

COUNTRY_CHOICES = (
    ('USA', 'United States'),
    ('UK', 'United Kingdom'),
    ('IND', 'India'),
    ('AUS', 'Australia'),
    ('CAN', 'Canada'),
    ('JPN', 'Japan'),
    ('FRA', 'France'),
    ('GER', 'Germany'),
    ('ITA', 'Italy'),
    ('RUS', 'Russia'),
    ('CHN', 'China'),
    ('BRA', 'Brazil'),
    ('MEX', 'Mexico'),
    ('ARG', 'Argentina'),
    ('ESP', 'Spain'),
    ('POR', 'Portugal'),
    ('SWE', 'Sweden'),
    ('NOR', 'Norway'),
    ('DEN', 'Denmark'),
    ('FIN', 'Finland'),
    ('NED', 'Netherlands'),
    ('BEL', 'Belgium'),
    ('LUX', 'Luxembourg'),
    ('IRL', 'Ireland'),
    ('SCO', 'Scotland'),
    ('WAL', 'Wales'),
    ('NZL', 'New Zealand'),
    ('RSA', 'South Africa'),
    ('KEN', 'Kenya'),
    ('NGA', 'Nigeria'),
    ('EGY', 'Egypt'),
    ('ISR',  'Israel'),
    ('JOR', 'Jordan'),
    ('KSA', 'Saudi Arabia'),
    ('UAE', 'United Arab Emirates'),
    ('QAT', 'Qatar'),
    ('OMA', 'Oman'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
