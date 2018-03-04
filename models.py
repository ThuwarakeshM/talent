from django.db import models
from django.contrib.auth.models import User

industries = (
    ('IT', 'Information Technology'),
    ('FN', 'Finance'),
    ('MC', 'Management Consultants'),
    ('CN', 'Constructions'),
)

districts = (
    ('AM', 'Ampara'),
    ('AN', 'Anuradhapura'),
    ('BD', 'Badulla'),
    ('BT', 'Batticaloa'),
    ('CO', 'Colombo'),
    ('GL', 'Galle'),
    ('GP', 'Gampaha'),
    ('HT', 'Hambantota'),
    ('JF', 'Jaffna'),
    ('KT', 'Kalutara'),
    ('KY', 'Kandy'),
    ('KG', 'Kegalle'),
    ('KL', 'Kilinochchi'),
    ('KR', 'Kurunegala'),
    ('MN', 'Mannar'),
    ('ME', 'Matale'),
    ('MT', 'Matara'),
    ('MO', 'Monaragala'),
    ('ML', 'Mullaitivu'),
    ('NE', 'Nuwara Eliya'),
    ('PN', 'Polonnaruwa'),
    ('PT', 'Puttalam'),
    ('RT', 'Ratnapura'),
    ('TR', 'Trincomalee'),
    ('VW', 'Vavuniya'),
)


# Create your models here.
class Publisher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    business_name = models.CharField(max_length=100, blank=False)
    industry = models.CharField(max_length=25, choices=industries)
    street_address = models.TextField(max_length=500, blank=False)
    district = models.CharField(max_length=20, choices=districts)

    def __str__(self):
        return self.business_name


class Telephone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=12, blank=False)


class Web(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    link = models.CharField(max_length=100, blank=False)


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)

    street_address = models.TextField(max_length=500, blank=False)
    district = models.CharField(max_length=50, choices=districts)
    town = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Advertisement(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    opening_date = models.DateField(auto_now=True)
    closing_date = models.DateField()

    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    contract_type = models.CharField(max_length=10, choices=(
        ('PT', 'Part-Time'),
        ('FT', 'Full-Time'),
        ('CN', 'Contract'),
    ))
    salary = models.FloatField()

    def __str__(self):
        return self.title + '@' + self.publisher.business_name


class Application(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    cv = models.FileField()

    def __str__(self):
        return self.applicant.first_name \
               + ' for ' \
               + self.advertisement.title \
               + ' @' \
               + self.advertisement.publisher.business_name


class Following(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.applicant.first_name \
               + ' following ' \
               + self.publisher.business_name


class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    datetime = models.DateTimeField(blank=False)
    venue = models.TextField(blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.application.advertisement.title \
               + '@' \
               + self.application.advertisement.publisher \
               + ' for ' \
               + self.application.applicant.first_name
