from django.db import models


class Operations(models.Model):
    id = models.ForeignKey('Users', models.DO_NOTHING, db_column='id')
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_of_operation = models.CharField(max_length=10)
    op_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'тип: {self.type}, размер: {self.amount}, дата: {self.date_of_operation}'

    class Meta:
        managed = False
        db_table = 'operations'
        verbose_name_plural = 'Operations'
        verbose_name = 'Operation'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'
