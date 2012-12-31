from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def genProperty(pname):
  pro_vl = models.IntegerField( default=2,
                                verbose_name="%s VL"%(pname,),
                                validators=[
                                  MinValueValidator(2),
                                  MaxValueValidator(20)] )
  pro_pm = models.IntegerField( default=0,
                                verbose_name="%s PM"%(pname,),
                                validators=[
                                  MinValueValidator(-10),
                                  MaxValueValidator(10)] )
  pro_tm = models.IntegerField( default=0,
                                verbose_name="%s TM"%(pname,),
                                validators=[
                                  MinValueValidator(-10),
                                  MaxValueValidator(10)] )
  pro_ap = models.IntegerField( default=0,
                                verbose_name="%s AP"%(pname,))
  pro_max = models.IntegerField(default=2,
                                verbose_name="%s Max"%(pname,),
                                validators=[
                                  MinValueValidator(2),
                                  MaxValueValidator(20)] )
  return pro_vl, pro_pm, pro_tm, pro_ap, pro_max

def sanity():
  return models.IntegerField( default=0,
                              validators=[
                                MinValueValidator(-5),
                                MaxValueValidator(5)] )

PRO_MENTAL = ["APT","CHA","MAR","SPI","WIL","WIT"]
PRO_PHYSICAL = ["AGI","COG","FOR","PHY","PCN","REF"]
PRO_ALL = PRO_PHYSICAL+PRO_MENTAL
PRO_CHOICES = zip(PRO_ALL,PRO_ALL)
#PRO_CHOICES_OPT = [("","")]+PRO_CHOICES

GENDERS=(
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
    )

class Character(models.Model):

  # Basic stuff
  name = models.CharField(max_length=50)
  gender = models.CharField(max_length=1,choices=GENDERS)
  age = models.PositiveIntegerField()
  max_points = models.PositiveIntegerField(default=0)

  #nationality = models.ForeignKey(Nationality)
  #speciality = models.ForeignKey(Speciality)
  #race = models.ForeignKey(Race)
  #socialclass = models.ForeignKey(SocialClass)
  #striker = models.ForeignKey(Striker)

  bep = models.IntegerField(default=1)
  stg = models.IntegerField(default=0)

  # Properties
  agi_vl, agi_pm, agi_tm, agi_ap, agi_max = genProperty("AGI")
  cog_vl, cog_pm, cog_tm, cog_ap, cog_max = genProperty("COG")
  for_vl, for_pm, for_tm, for_ap, for_max = genProperty("FOR")
  phy_vl, phy_pm, phy_tm, phy_ap, phy_max = genProperty("PHY")
  pcn_vl, pcn_pm, pcn_tm, pcn_ap, pcn_max = genProperty("PCN")
  ref_vl, ref_pm, ref_tm, ref_ap, ref_max = genProperty("REF")

  apt_vl, apt_pm, apt_tm, apt_ap, apt_max = genProperty("APT")
  cha_vl, cha_pm, cha_tm, cha_ap, cha_max = genProperty("CHA")
  mar_vl, mar_pm, mar_tm, mar_ap, mar_max = genProperty("MAR")
  spi_vl, spi_pm, spi_tm, spi_ap, spi_max = genProperty("SPI")
  wil_vl, wil_pm, wil_tm, wil_ap, wil_max = genProperty("WIL")
  wit_vl, wit_pm, wit_tm, wit_ap, wit_max = genProperty("WIT")

  # Stat modifiers
  balance     = sanity()
  violence    = sanity()
  horror      = sanity()
  paranormal  = sanity()

  cc_mod = models.IntegerField(default=0,verbose_name='CC+')
  sc_mod = models.IntegerField(default=0,verbose_name='SC+')
  ac_mod = models.IntegerField(default=0,verbose_name='AC+')
  mc_mod = models.IntegerField(default=0,verbose_name='MC+')

  cc_rec_mod = models.IntegerField(default=0,verbose_name='CC Rec+')
  sc_rec_mod = models.IntegerField(default=0,verbose_name='SC Rec+')
  ac_rec_mod = models.IntegerField(default=0,verbose_name='AC Rec+')
  mc_rec_mod = models.IntegerField(default=0,verbose_name='MC Rec+')

  actions_mod         = models.IntegerField(default=0)
  chain_active_mod    = models.IntegerField(default=0)
  chain_inactive_mod  = models.IntegerField(default=0)
  initiative_mod      = models.IntegerField(default=0)

  cogdb_mod   = models.IntegerField(default=0,verbose_name='COG DB+')
  fordb_mod   = models.IntegerField(default=0,verbose_name='FOR DB+')
  pcndb_mod   = models.IntegerField(default=0,verbose_name='PCN DB+')
  melee_mod   = models.IntegerField(default=0,verbose_name='Melee+')
  basedmg_mod = models.IntegerField(default=0,verbose_name='Base DMG+')

  large_phs_mod = models.IntegerField(default=0,verbose_name='Large PHS+')
  large_mar_mod = models.IntegerField(default=0,verbose_name='Large MAR+')
  large_mer_mod = models.IntegerField(default=0,verbose_name='Large MER+')

  # Resistances
  phs_bc = models.IntegerField(default=10,verbose_name='PHS BC')
  mar_bc = models.IntegerField(default=10,verbose_name='MAR BC')
  mer_bc = models.IntegerField(default=10,verbose_name='MER BC')

  def __unicode__(self):
    return self.name

SKILL_ALL = ["Acrobatics","Thrust Weapons","Survival"]
SKILL_CHOICES = zip(SKILL_ALL,SKILL_ALL)

class Skill(models.Model):
  character = models.ForeignKey(Character)
  name = models.CharField(max_length=30,choices=SKILL_CHOICES)
  speciality = models.BooleanField()
  level = models.IntegerField(default=1,
                              validators=[
                                MinValueValidator(0),
                                MaxValueValidator(5)] )
  ap = models.IntegerField(verbose_name="AP",default=0)

class Weapon(models.Model):
  character = models.ForeignKey(Character)

  name    = models.CharField(max_length=50)
  dmg     = models.IntegerField(verbose_name='DMG')
  dub_abs = models.IntegerField(verbose_name='ABS')
  dub     = models.IntegerField(verbose_name='DUB')
  req     = models.IntegerField(verbose_name='REQ')
  rng     = models.IntegerField(verbose_name='RNG')
  act     = models.IntegerField(verbose_name='ACT')
  sr      = models.IntegerField(verbose_name='SR')

  def __unicode__(self):
    return self.name

class Armour(models.Model):
  character = models.ForeignKey(Character)

  name    = models.CharField(max_length=50)
  dub_abs = models.IntegerField(verbose_name='ABS')
  dub     = models.IntegerField(verbose_name='DUB')
  req     = models.IntegerField(verbose_name='REQ')
  agi     = models.IntegerField(verbose_name='AGI')
  mov     = models.IntegerField(verbose_name='MOV')
  act     = models.IntegerField(verbose_name='ACT')
  sc      = models.IntegerField(verbose_name='SC')

  def __unicode__(self):
    return self.name

class Affliction(models.Model):
  character = models.ForeignKey(Character)

  name  = models.CharField(max_length=50)
  note  = models.CharField(max_length=100)
  sg      = models.IntegerField(verbose_name='SG')

  def __unicode__(self):
    return self.name

class Modifier(models.Model):
  character = models.ForeignKey(Character)

  name = models.CharField(max_length=50)
  benefit = models.BooleanField()
  cost = models.IntegerField(default=0)

  def __unicode__(self):
    return self.name

class Misc(models.Model):
  character = models.ForeignKey(Character)

  name  = models.CharField(max_length=50)
  cost  = models.IntegerField()

  def __unicode__(self):
    return self.name

