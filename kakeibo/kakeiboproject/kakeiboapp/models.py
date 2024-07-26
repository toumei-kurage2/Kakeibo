from django.db import models
class Koumoku(models.Model):
    Koumoku_name=models.CharField(max_length=30,unique=True)
    yosan = models.IntegerField()
    class Meta:
        db_table="koumoku"
    def __str__(self):
        return self.Koumoku_name


class Rireki(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    date=models.DateField()
    fee=models.IntegerField()
    koumoku=models.ForeignKey(Koumoku,on_delete=models.CASCADE)
    class Meta:
        db_table="Rireki"
