from django.db import models


class Motor(models.Model):
    modeles = models.CharField(max_length=125, verbose_name='Modèles', unique=True, null=True)
    photo = models.ImageField(null=True)
    puissance_cv = models.CharField(max_length=125, verbose_name='Puissance cv', null=True)
    volume_balaye = models.CharField(max_length=125, verbose_name='Volume Balayé m3/h')
    application = models.CharField(max_length=125, verbose_name='Application')
    voltage = models.CharField(max_length=125, verbose_name='Voltage v')
    intensite_max_1PH_50 = models.CharField(max_length=125, verbose_name='50 HZ Intensité max pour 1PH', null=True, blank=True)
    intensite_max_3PH_50 = models.CharField(max_length=125, verbose_name='50 HZ Intensité max pour 3PH', null=True, blank=True)
    puissance_frigorifique_75 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour 7.5°', null=True, blank=True)
    puissance_frigorifique_5 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour 5°', null=True, blank=True)
    puissance_frigorifique_0 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour 0°', null=True, blank=True)
    puissance_frigorifique_m5 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -5°', null=True, blank=True)
    puissance_frigorifique_m10 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -10°', null=True, blank=True)
    puissance_frigorifique_m15 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -15°', null=True, blank=True)
    puissance_frigorifique_m20 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -20°', null=True, blank=True)
    puissance_frigorifique_m25 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -25°', null=True, blank=True)
    puissance_frigorifique_m30 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -30°', null=True, blank=True)
    puissance_frigorifique_m35 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -35°', null=True, blank=True)
    puissance_frigorifique_m40 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -40°', null=True, blank=True)
    puissance_frigorifique_m45 = models.CharField(max_length=125, verbose_name='Puissance Frigorifique pour -45°', null=True, blank=True)
