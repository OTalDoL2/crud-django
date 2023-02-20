from django.db import models

# Bastante semelhante ao model do springboot, porém mais curto...
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
