from django.db import models


class Event(models.Model):

    class Meta:
        verbose_name = 'праздник'
        verbose_name_plural = 'праздники'

    name = models.CharField(
        max_length=256,
        verbose_name='название праздника'
    )
    date_start = models.DateTimeField(
        verbose_name='дата начала события',
        null=True
    )
    date_end = models.DateTimeField(
        verbose_name='дата окончания события',
        null=True
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='описание',
        null=True
    )
    address = models.CharField(
        max_length=360,
        verbose_name='адрес',
        null=True
    )
    background = models.ImageField(
        upload_to='events/'
    )
    dresscode = models.CharField(
        max_length=256,
        verbose_name='дресс код',
        blank=True,
        default='Отсутствует'
    )

    def __str__(self):
        return self.name


class Gift(models.Model):

    class Meta:
        verbose_name = 'подарок'
        verbose_name_plural = 'подарки'

    name = models.CharField(
        max_length=256,
        verbose_name='название подарка'
    )
    price = models.PositiveIntegerField(
            verbose_name='цена подарка',
        )
    photo = models.ImageField(
        upload_to='gifts/'
    )
    link = models.URLField(
        verbose_name='ссылка на подарок',
        blank=True,
        null=True
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE,
        related_name='gifts',
        verbose_name='праздник'
    )

    def __str__(self):
        return self.name


class WebConfig(models.Model):

    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'настройки'

    logo = models.ImageField(
        upload_to='config/',
        verbose_name='логотип'
    )
    site_name = models.CharField(
        max_length=256,
        verbose_name='название сайта'
    )
    pic_buy = models.ImageField(
        upload_to='config/',
        verbose_name='картинка для "я куплю"'
    )
    pic_bought = models.ImageField(
        upload_to='config/',
        verbose_name='картинка для "я купил"'
    )
    pic_arrow = models.ImageField(
        upload_to='config/',
        verbose_name='стрелка'
    )
    pic_new_gift = models.ImageField(
        upload_to='config/',
        verbose_name='картинка для "новый подарок"'
    )
