from django.db import models
from django.core.validators import RegexValidator
from django.db import models

from django.utils.translation import gettext_lazy as _
from datetime import datetime as date



# Create your models here.

class Feedback(models.Model):
    feedbackName=models.CharField(max_length=32)
    feedbackEmail=models.EmailField()
    feedbackSubject=models.TextField()
    def __str__(self):
        return self.feedbackName

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32)
    apelido = models.CharField(max_length=32)
    email = models.EmailField()
    telemovel = models.CharField(max_length=13, default='xd')
    dataNascimento = models.DateField()
    criado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.id}: {self.nome} {self.apelido}"

class raiddifficulty(models.Model):
    dificuldade = models.CharField(max_length=6)
    codigo = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.dificuldade}({self.codigo})"

class Raid(models.Model):

    class raidlevels(models.IntegerChoices):
        vanilla = 60, 'Vanilla'
        burningCrusade = 70, 'Burning Crusade'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32)
    level = models.IntegerField(default=raidlevels.vanilla, choices=raidlevels.choices)
    difficulty = models.ForeignKey(raiddifficulty,
                                   on_delete=models.CASCADE,
                                   related_name="diff")


    def __str__(self):
        return f"{self.nome}({self.difficulty.codigo}) [level {self.level} : {self.difficulty.dificuldade} dificulty]"






class Raider(models.Model):

    class raiderrole(models.TextChoices):
        DamageDealer = 'Damage Dealer', 'dps'
        Healer = 'Healer', 'healer'
        Tank = 'Tank', 'tank'

    class raiderclass(models.TextChoices):
        Hunter = 'Hunter', 'hunter'
        Shamman = 'Shamman', 'shamman'
        Rogue = 'Rogue', 'rogue'
        Druid = 'Druid', 'druid'
        Warrior = 'Warrior', 'warrior'
        Paladin = 'Paladin', 'paladin'
        Warlock = 'Warlock', 'warlock'
        Priest = 'Priest', 'priest'
        Mage = 'Mage', 'mage'

    player_name = models.CharField(max_length=24)
    role = models.CharField(max_length=13,default=raiderrole.DamageDealer, choices=raiderrole.choices)
    charclass = models.CharField(max_length=7,default=raiderclass.Hunter, choices=raiderclass.choices)
    raids = models.ManyToManyField(Raid,
                                   blank=True,
                                   related_name="Raiders")

    def __str__(self):
        return f"{self.player_name} [{self.charclass}:{self.role}]"


