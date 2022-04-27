from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'