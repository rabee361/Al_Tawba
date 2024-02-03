from django.db import models

class Fatwa(models.Model):
    question = models.CharField(max_length=200 , verbose_name='السؤال')
    answer = models.CharField(max_length=200 , verbose_name='الفتوى')
    date = models.DateField(auto_now_add=True)


class HajInfo(models.Model):
    pass


class Campaign(models.Model):
    about = models.TextField()

    def __str__(self):
        return 'معلومات عن الحملة'
    

class PrayType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pray(models.Model):
    pray_type = models.ForeignKey(PrayType , on_delete=models.CASCADE)
    text = models.CharField(max_length=600)

    def __str__(self):
        return self.text[:50]
    


class Nosk(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=500)



class AdviceType(models.Model):
    name = models.CharField(max_length=20)


class Advices(models.Model):
    advice_type = models.ForeignKey()
    text = models.CharField(max_length=200)
