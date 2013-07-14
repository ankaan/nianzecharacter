from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def choices(options):
  if type(options) is list:
    return zip(options,options)
  elif type(options) is dict:
    return sorted(options.items())
  else:
    raise TypeError('Options must be a list or a dict.')

def gen_attr(name):
  stat_vl = models.IntegerField(default=0,
                                verbose_name='%s VL'%(name),
                                validators=[
                                  MinValueValidator(0),
                                  MaxValueValidator(30)] )
  stat_mod = models.IntegerField( default=0,
                                  verbose_name='%s MOD'%name,
                                  validators=[
                                    MinValueValidator(-10),
                                    MaxValueValidator(10)] )
  return stat_vl, stat_mod

def gen_skill(name):
  stat_lvl = models.IntegerField( default=0,
                                  verbose_name='%s LvL'%(name),
                                  validators=[
                                    MinValueValidator(0),
                                    MaxValueValidator(6)] )
  stat_mod = models.IntegerField( default=0,
                                  verbose_name='%s MOD'%name,
                                  validators=[
                                    MinValueValidator(-10),
                                    MaxValueValidator(10)] )
  return stat_lvl, stat_mod

class Expertise(models.Model):
  ENERGY_AFFINITY={ 'a': 'Aruhun',
                    'g': 'Gaia',
                    'm': 'Marchon'}

  name = models.CharField(max_length=50)
  ip = models.IntegerField( verbose_name='IP',
                            default=0)
  cs = models.IntegerField( verbose_name='CS',
                            default=0)
  affinity = models.CharField(max_length=1,
                              choices=choices(ENERGY_AFFINITY),
                              default='g')

  def __unicode__(self):
    return self.name

class Character(models.Model):
  ATTR = {'acu': 'Accuracy',
          'bra': 'Brawn',
          'cor': 'Coordination',
          'foc': 'Focus',
          'men': 'Mentality',
          'vit': 'Vitality'}
  
  SKILL = { 'ath': 'Athletics',
            'bat': 'Battle',
            'com': 'Common',
            'kno': 'Knowledge',
            'mys': 'Mystical',
            'soc': 'Social'}

  GENDERS=['Male','Female','Other']
  RACES = ['Human','Elf','Dwarf','Half Elf','Panling','Xin\'Ar','Xin\'Er']
  NATIONALITIES = ['Meno','Katia','Aguin','Deben']
  STRIKERS = ['Marchon Striker','Aruhun Striker','Gaia Striker']

  # Basic stuff
  name = models.CharField(max_length=50)
  age = models.PositiveIntegerField(default=0)
  gender = models.CharField(max_length=6,
                            choices=choices(GENDERS),
                            blank=True,
                            default='')

  race = models.CharField(max_length=20,
                          choices=choices(RACES),
                          blank=True,
                          default='')
  race_fancy = models.CharField(verbose_name='Fancy Race',
                                max_length=20,
                                blank=True,
                                default='')

  nationality = models.CharField( max_length=20,
                                  choices=choices(NATIONALITIES),
                                  blank=True,
                                  default='')
  nationality_fancy = models.CharField( verbose_name='Fancy Nationality',
                                        max_length=20,
                                        blank=True,
                                        default='')

  striker = models.CharField( max_length=20,
                              choices=choices(STRIKERS),
                              blank=True,
                              default='')

  bep = models.PositiveIntegerField(verbose_name='BEP',
                                    default=1)
  stp = models.PositiveIntegerField(verbose_name='STP',
                                    default=0)

  # Attributes
  acu_vl, acu_mod = gen_attr('Accuracy')
  bra_vl, bra_mod = gen_attr('Brawn')
  cor_vl, cor_mod = gen_attr('Coordination')
  foc_vl, foc_mod = gen_attr('Focus')
  men_vl, men_mod = gen_attr('Mentality')
  vit_vl, vit_mod = gen_attr('Vitality')

  # Skills
  ath_lvl, ath_mod = gen_skill('Athletics')
  bat_lvl, bat_mod = gen_skill('Battle')
  com_lvl, com_mod = gen_skill('Common')
  kno_lvl, kno_mod = gen_skill('Knowledge')
  mys_lvl, mys_mod = gen_skill('Mystical')
  soc_lvl, soc_mod = gen_skill('Social')

  # Specializations
  acrobatics = models.BooleanField(default=False)
  climb = models.BooleanField(default=False)
  dodge = models.BooleanField(default=False)
  
  axe = models.BooleanField(default=False)
  bow = models.BooleanField(default=False)
  chain_weapon = models.BooleanField(default=False)

  steal = models.BooleanField(default=False)

  alchemy = models.BooleanField(default=False)
  civics = models.BooleanField(default=False)
  history = models.BooleanField(default=False)

  channel = models.BooleanField(default=False)
  multitrance = models.BooleanField(default=False)
  sorcery = models.BooleanField(default=False)

  act = models.BooleanField(default=False)
  deceive = models.BooleanField(default=False)
  rhetoric = models.BooleanField(default=False)

  # Expertises
  expertise = models.ManyToManyField( Expertise,
                                      verbose_name="Expertises",
                                        null=True,
                                        blank=True)

  def __unicode__(self):
    return self.name

class CustomKnowledge(models.Model):
  name = models.CharField(max_length=20)
  char = models.ForeignKey( Character,
                            verbose_name='Character')

  class Meta:
    unique_together = (('char','name'),)

  def __unicode__(self):
    return self.name

class Weapon(models.Model):
  character = models.ForeignKey(Character)
  info = models.CharField(max_length=50)

  def __unicode__(self):
    return self.info

class Armour(models.Model):
  character = models.ForeignKey(Character)
  info = models.CharField(max_length=50)

  def __unicode__(self):
    return self.info

class Wound(models.Model):
  SEVERITIES = ['Minor','Major','Abiding']

  character = models.ForeignKey(Character)
  info = models.CharField(max_length=50)
  severity = models.CharField(max_length=50,
                              choices=choices(SEVERITIES))

  def __unicode__(self):
    return self.info
