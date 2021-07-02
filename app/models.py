from django.db import models


class T_Users(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Куратор'
        # default='Не назначено'
    )

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'

    def __str__(self):
        return self.name

    @property
    def get_procedures_by_curator(self):
        result = ''
        for procedure in T_Procedures.objects.filter(curator__name__contains=self.name):
            result = result + ' %s, \n' % procedure.xml_type
        return result

    get_procedures_by_curator.fget.short_description = 'Отслеживаемые процедуры'


class T_Procedures(models.Model):
    curator = models.ForeignKey(
        T_Users,
        on_delete=models.SET_NULL,
        null=True
    )
    xml_type = models.CharField(
        max_length=100,
    )
    purchaseNumber = models.IntegerField()
    docPublishDate = models.DateTimeField()
    purchaseObjectInfo = models.TextField(max_length=5000)
    regNum = models.IntegerField()
    maxPrice = models.IntegerField()

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'
        ordering = ('id',)

    def __str__(self):
        return str(self.purchaseNumber)