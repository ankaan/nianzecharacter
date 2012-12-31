from charsheet.models import Character,Skill,SkillChoice,PRO_ALL
from charsheet.models import WeaponTemplate,ArmourTemplate
from charsheet.models import Weapon,Armour,Affliction,Misc
from charsheet.models import Nationality,Speciality,Race
from charsheet.models import SocialClass,Striker
from charsheet.models import GeneralBenefit,Trait,Lineage
from charsheet.models import GeneralDeficiency,Quirk
from django.contrib import admin

class WeaponInline(admin.TabularInline):
  model = Weapon
  extra = 0

class ArmourInline(admin.TabularInline):
  model = Armour
  extra = 0

class AfflictionInline(admin.TabularInline):
  model = Affliction
  extra = 0

class MiscInline(admin.TabularInline):
  model = Misc
  extra = 0

class SkillChoiceInline(admin.TabularInline):
  model = SkillChoice
  extra = 0

class GeneralBenefitInline(admin.TabularInline):
  model = GeneralBenefit
  extra = 0

class GeneralDeficiencyInline(admin.TabularInline):
  model = GeneralDeficiency
  extra = 0

class CharacterAdmin(admin.ModelAdmin):

  pro = [x.lower() for x in PRO_ALL]
  pro_fields = [ (x+'_vl',x+'_pm',x+'_tm',x+'_ap',x+'_max') for x in pro ]

  list_display = ('name',)

  fieldsets = (
      (None, {
        'fields': (
          ('name','age','gender','race'),
          ('nationality','socialclass','speciality','striker'),
          'max_points',
          'general_benefits',
          'general_deficiencies',
        ),
      }),
      ('Properties', {
        'fields': pro_fields,
      }),
      ('Sanity', {
        'fields': (('balance','violence','horror','paranormal'),),
      }),
      ('Modifiers', {
        'fields': (
          ('cc_mod','sc_mod','ac_mod','mc_mod'),
          ('cc_rec_mod','sc_rec_mod','ac_rec_mod','mc_rec_mod'),
          ('actions_mod','chain_active_mod','chain_inactive_mod','initiative_mod'),
          ('cogdb_mod','fordb_mod','pcndb_mod','melee_mod','basedmg_mod'),
          ('large_phs_mod','large_mar_mod','large_mer_mod'),
        ),
      }),
      ('Resistances', {
        'fields': (('phs_bc','mar_bc','mer_bc'),),
      }),
  )
  inlines = [ SkillChoiceInline,
              #GeneralBenefitInline,
              #GeneralDeficiencyInline,
              WeaponInline,
              ArmourInline,
              AfflictionInline,
              MiscInline]
admin.site.register(Character,CharacterAdmin)

class SkillAdmin(admin.ModelAdmin):
  list_display = ('name','primary_pro','secondary_pro','wit_rec','cost','action')
admin.site.register(Skill,SkillAdmin)

class WeaponTemplateAdmin(admin.ModelAdmin):
  list_display = ('name','dmg','dub_abs','dub','req','rng','act','sr')
admin.site.register(WeaponTemplate,WeaponTemplateAdmin)

class ArmourTemplateAdmin(admin.ModelAdmin):
  list_display = ('name','dub_abs','dub','req','agi','mov','act','sc')
admin.site.register(ArmourTemplate,ArmourTemplateAdmin)

class NationalityAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(Nationality,NationalityAdmin)

class SpecialityAdmin(admin.ModelAdmin):
  list_display = ('name','cost','socialclass')
admin.site.register(Speciality,SpecialityAdmin)

class RaceAdmin(admin.ModelAdmin):
  list_display = ('name','cost','youth','adult','old','death')
admin.site.register(Race,RaceAdmin)

class SocialClassAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(SocialClass,SocialClassAdmin)

class StrikerAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(Striker,StrikerAdmin)

class GeneralBenefitAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(GeneralBenefit,GeneralBenefitAdmin)

class TraitAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(Trait,TraitAdmin)

class LineageAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(Lineage,LineageAdmin)

class GeneralDeficiencyAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(GeneralDeficiency,GeneralDeficiencyAdmin)

class QuirkAdmin(admin.ModelAdmin):
  list_display = ('name','cost')
admin.site.register(Quirk,QuirkAdmin)
