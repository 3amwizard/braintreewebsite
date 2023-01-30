from django.db import models
from django.utils import timezone

# Create your models here.
MODULE_CHOICES = (('Verde People', 'Verde People'), ('Verde Fleet', 'Verde Fleet'), ('Verde Leave', 'Verde Leave'),
    ('Verde Gift Reg', 'Verde Gift Reg'), ('Verde Claims', 'Verde Claims'), ('Verde ELC', 'Verde ELC'), ('Verde Policy', 'Verde Policy'))
SIZE_CHOICES = (('1-10', '1-10'), ('11-50', '11-50'), ('51-100', '51-100'), ('101-500', '101-500'), ('501 -1000', '501-1000'),
    ('Over 1001', 'Over 1001'))

class Business(models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=36)
	email = models.EmailField()
	company = models.CharField(max_length=72)
	service = models.CharField(max_length=72, choices=MODULE_CHOICES)
	size = models.CharField(max_length=72, choices=SIZE_CHOICES)
	message = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

#options
ENTITY_CHOICES = (('Pty (Ltd)', 'Pty (Ltd)'), ('CC', 'CC'), ('Public Company', 'Public Company'))
NATURE_CHOICES = (('Importer', 'Importer'), ('Exporter', 'Exporter'), ('Both', 'Both'))
TURNOVER_CHOICES = (('Less than 1 million USD annually', 'Less than 1 million USD annually'), 
	('1-10 million annually', '1-10 million annually'), 
	('10 million or more annually', '10 million or more annually'))
CURRENT_USE_CHOICES = (('Your bank', 'Your bank'), ('Another intermediary', 'Another intermediary'))

def user_directory_path(instance, filename):
	return 'uploads/user_{0}/{1}'.format(instance.name, filename)

#Callback Modal
class Callback(models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=36)
	email = models.EmailField()
	phone = models.CharField(max_length=36)

	def __str__(self):
		return self.name

#individualform

class Individual(models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=36)
	email = models.EmailField()
	phone = models.CharField(max_length=36)
	occupation = models.CharField(max_length=72)
	tax_number = models.CharField(max_length=72)
	id_copy = models.FileField(upload_to=user_directory_path)
	selfie = models.FileField(upload_to=user_directory_path)
	por = models.FileField(upload_to=user_directory_path)

	def __str__(self):
		return self.name

#businessform
class Business(models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=36)
	email = models.EmailField()
	phone = models.CharField(max_length=36)
	company = models.CharField(max_length=72)
	entity_type = models.CharField(max_length=72, choices=ENTITY_CHOICES)
	nature = models.CharField(max_length=72, choices=NATURE_CHOICES)
	turnover = models.CharField(max_length=512, choices=TURNOVER_CHOICES)
	current_use = models.CharField(max_length=72, choices=CURRENT_USE_CHOICES)

	def __str__(self):
		return self.name