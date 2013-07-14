# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Expertise.affinity'
        db.add_column('charsheet_expertise', 'affinity',
                      self.gf('django.db.models.fields.CharField')(default='G', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Expertise.affinity'
        db.delete_column('charsheet_expertise', 'affinity')


    models = {
        'charsheet.armour': {
            'Meta': {'object_name': 'Armour'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.character': {
            'Meta': {'object_name': 'Character'},
            'acrobatics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'act': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'acu_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'acu_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'alchemy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ath_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ath_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'axe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bat_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bat_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'bow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bra_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bra_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'chain_weapon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'channel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'civics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'climb': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'com_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'com_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'deceive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dodge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expertise': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['charsheet.Expertise']", 'null': 'True', 'blank': 'True'}),
            'foc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'foc_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'history': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kno_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kno_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'multitrance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mys_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mys_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'nationality_fancy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'race_fancy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'rhetoric': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'soc_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'soc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sorcery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'steal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'striker': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'vit_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vit_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'charsheet.customknowledge': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'CustomKnowledge'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'charsheet.expertise': {
            'Meta': {'object_name': 'Expertise'},
            'affinity': ('django.db.models.fields.CharField', [], {'default': "'G'", 'max_length': '1'}),
            'cs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.wound': {
            'Meta': {'object_name': 'Wound'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['charsheet']