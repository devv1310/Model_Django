from django.db import models

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_contact=models.IntegerField()
    stu_email=models.EmailField()
    stu_city=models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name+' '+self.stu_email

    class Meta:
        db_table='Student'
        verbose_name_plural='Student'
        # verbose_name='Student'
        ordering=['stu_name']