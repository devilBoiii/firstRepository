from django.db import models

# Create your models here.
class onePiece(models.Model):
	Char_id=models.AutoField(primary_key=True)
	Name=models.CharField(max_length=50)
	Age=models.PositiveIntegerField()
	Roles=models.CharField(max_length=40)
	Power=models.CharField(max_length=50)

	class Meta:
		verbose_name='OnePiece'
		verbose_name_plural='OnePieces'

	def __str__(self):
		return self.Name+' With '+ str(self.Char_id)

