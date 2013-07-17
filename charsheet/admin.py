from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple, ModelForm

from charsheet.models import *

class CustomKnowledgeInline(admin.TabularInline):
  model = CustomKnowledge
  extra = 0

class WeaponInline(admin.TabularInline):
  model = Weapon
  extra = 0

class ArmourInline(admin.TabularInline):
  model = Armour
  extra = 0

class WoundInline(admin.TabularInline):
  model = Wound
  extra = 0

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    widgets = {
        'expertise': CheckboxSelectMultiple(),
    }

  def attr(self):
    for k, v in sorted(Character.ATTR.items()):
      yield v, self[k+'_vl'], self[k+'_mod']

  def skill(self):
    for k, v in sorted(Character.SKILL.items()):
      yield v, self[k+'_lvl'], self[k+'_mod']

  def spec(self):
    for skill, specnames in sorted(Character.SPEC.items()):
      yield Character.SKILL[skill], (self[n] for n in sorted(specnames))

class CharacterAdmin(admin.ModelAdmin):
  form = CharacterForm

  save_on_top = True
  list_display = ('name',)

#  fieldsets = (
#      (None, {
#        'fields': (
#          ('name',),
#          ('age','gender'),
#          ('race','race_fancy'),
#          ('nationality','nationality_fancy'),
#          ('striker'),
#        ),
#      }),
#      ('Misc', {
#        'fields': (
#          ('bep','stp'),
#        ),
#      }),
#      ('Attributes', {
#        'fields': [(x+'_vl',x+'_mod') for x in sorted(Character.ATTR.keys())],
#      }),
#      ('Skills', {
#        'fields': [(x+'_lvl',x+'_mod') for x in sorted(Character.SKILL.keys())],
#      }),
#      ('Specializations', {
#        'fields': (
#          ('acrobatics','climb','dodge'),
#          ('axe','bow','chain_weapon'),
#          ('steal',),
#          ('alchemy','civics','history'),
#          ('channel','multitrance','sorcery'),
#          ('act','deceive','rhetoric'),
#        ),
#      }),
#      ('Expertises', {
#        'fields': (
#          ('expertise'),
#        ),
#      }),
#  )

  #filter_horizontal = ('expertise',)

  inlines = [ CustomKnowledgeInline,
              WeaponInline,
              ArmourInline,
              WoundInline]

admin.site.register(Character,CharacterAdmin)

class ExpertiseAdmin(admin.ModelAdmin):
  list_display = ('name','ip','cs')
  list_editable = ('ip','cs')
  list_display_links = ('name',)

  fieldsets = (
      (None, {
        'fields': (
          ('name','ip','cs','affinity'),
        ),
      }),
  )

admin.site.register(Expertise,ExpertiseAdmin)
