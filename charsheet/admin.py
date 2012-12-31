from charsheet.models import Character,Skill,PROS
from charsheet.models import Weapon,Armour,Affliction,Misc
from charsheet.models import Modifier
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

class ModifierInline(admin.TabularInline):
  model = Modifier
  extra = 0

class SkillInline(admin.TabularInline):
  model = Skill
  extra = 0

class CharacterAdmin(admin.ModelAdmin):

  pro = [x.lower() for x in PROS]
  pro_fields = [ (x+'_vl',x+'_pm',x+'_tm',x+'_ap',x+'_max') for x in pro ]

  list_display = ('name',)

  fieldsets = (
      (None, {
        'fields': (
          ('name','age','gender','race'),
          ('nationality','socialclass','speciality','striker'),
          'max_points',
        ),
      }),
      ('Properties', {
        'fields': pro_fields,
      }),
      ('Sanity', {
        'fields': (('balance','violence','horror','paranormal'),),
      }),
      ('Stat Modifiers', {
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

  inlines = [ SkillInline,
              WeaponInline,
              ArmourInline,
              AfflictionInline,
              MiscInline,
              ModifierInline]
admin.site.register(Character,CharacterAdmin)
