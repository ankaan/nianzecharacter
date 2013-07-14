# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'KnowledgeSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_knowledgespecialization', ['char_id', 'name'])

        # Removing unique constraint on 'CommonSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_commonspecialization', ['char_id', 'name'])

        # Removing unique constraint on 'BattleSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_battlespecialization', ['char_id', 'name'])

        # Removing unique constraint on 'SocialSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_socialspecialization', ['char_id', 'name'])

        # Removing unique constraint on 'CustomKnowledgeSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_customknowledgespecialization', ['char_id', 'name'])

        # Removing unique constraint on 'AthleticsSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_athleticsspecialization', ['char_id', 'name'])

        # Removing unique constraint on 'MysticalSpecialization', fields ['char', 'name']
        db.delete_unique('charsheet_mysticalspecialization', ['char_id', 'name'])

        # Deleting model 'MysticalSpecialization'
        db.delete_table('charsheet_mysticalspecialization')

        # Deleting model 'AthleticsSpecialization'
        db.delete_table('charsheet_athleticsspecialization')

        # Deleting model 'CustomKnowledgeSpecialization'
        db.delete_table('charsheet_customknowledgespecialization')

        # Deleting model 'SocialSpecialization'
        db.delete_table('charsheet_socialspecialization')

        # Deleting model 'BattleSpecialization'
        db.delete_table('charsheet_battlespecialization')

        # Deleting model 'CommonSpecialization'
        db.delete_table('charsheet_commonspecialization')

        # Deleting model 'KnowledgeSpecialization'
        db.delete_table('charsheet_knowledgespecialization')

        # Adding model 'CustomKnowledge'
        db.create_table('charsheet_customknowledge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
        ))
        db.send_create_signal('charsheet', ['CustomKnowledge'])

        # Adding unique constraint on 'CustomKnowledge', fields ['char', 'name']
        db.create_unique('charsheet_customknowledge', ['char_id', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'CustomKnowledge', fields ['char', 'name']
        db.delete_unique('charsheet_customknowledge', ['char_id', 'name'])

        # Adding model 'MysticalSpecialization'
        db.create_table('charsheet_mysticalspecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['MysticalSpecialization'])

        # Adding unique constraint on 'MysticalSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_mysticalspecialization', ['char_id', 'name'])

        # Adding model 'AthleticsSpecialization'
        db.create_table('charsheet_athleticsspecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['AthleticsSpecialization'])

        # Adding unique constraint on 'AthleticsSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_athleticsspecialization', ['char_id', 'name'])

        # Adding model 'CustomKnowledgeSpecialization'
        db.create_table('charsheet_customknowledgespecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['CustomKnowledgeSpecialization'])

        # Adding unique constraint on 'CustomKnowledgeSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_customknowledgespecialization', ['char_id', 'name'])

        # Adding model 'SocialSpecialization'
        db.create_table('charsheet_socialspecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['SocialSpecialization'])

        # Adding unique constraint on 'SocialSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_socialspecialization', ['char_id', 'name'])

        # Adding model 'BattleSpecialization'
        db.create_table('charsheet_battlespecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['BattleSpecialization'])

        # Adding unique constraint on 'BattleSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_battlespecialization', ['char_id', 'name'])

        # Adding model 'CommonSpecialization'
        db.create_table('charsheet_commonspecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['CommonSpecialization'])

        # Adding unique constraint on 'CommonSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_commonspecialization', ['char_id', 'name'])

        # Adding model 'KnowledgeSpecialization'
        db.create_table('charsheet_knowledgespecialization', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['KnowledgeSpecialization'])

        # Adding unique constraint on 'KnowledgeSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_knowledgespecialization', ['char_id', 'name'])

        # Deleting model 'CustomKnowledge'
        db.delete_table('charsheet_customknowledge')


    models = {
        'charsheet.armour': {
            'Meta': {'object_name': 'Armour'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.character': {
            'Meta': {'object_name': 'Character'},
            'acu_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'acu_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ath_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ath_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bat_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bat_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'bra_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bra_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'com_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'com_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'expertise': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['charsheet.Expertise']", 'null': 'True', 'blank': 'True'}),
            'foc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'foc_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kno_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kno_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_vl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mys_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mys_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'nationality_fancy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'race_fancy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'soc_lvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'soc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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