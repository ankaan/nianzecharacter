# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Specialization'
        db.delete_table('charsheet_specialization')

        # Adding model 'MysticalSpecialization'
        db.create_table('charsheet_mysticalspecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['MysticalSpecialization'])

        # Adding unique constraint on 'MysticalSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_mysticalspecialization', ['char_id', 'name'])

        # Adding model 'AthleticsSpecialization'
        db.create_table('charsheet_athleticsspecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['AthleticsSpecialization'])

        # Adding unique constraint on 'AthleticsSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_athleticsspecialization', ['char_id', 'name'])

        # Adding model 'CustomKnowledgeSpecialization'
        db.create_table('charsheet_customknowledgespecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['CustomKnowledgeSpecialization'])

        # Adding unique constraint on 'CustomKnowledgeSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_customknowledgespecialization', ['char_id', 'name'])

        # Adding model 'SocialSpecialization'
        db.create_table('charsheet_socialspecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['SocialSpecialization'])

        # Adding unique constraint on 'SocialSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_socialspecialization', ['char_id', 'name'])

        # Adding model 'BattleSpecialization'
        db.create_table('charsheet_battlespecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['BattleSpecialization'])

        # Adding unique constraint on 'BattleSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_battlespecialization', ['char_id', 'name'])

        # Adding model 'CommonSpecialization'
        db.create_table('charsheet_commonspecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['CommonSpecialization'])

        # Adding unique constraint on 'CommonSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_commonspecialization', ['char_id', 'name'])

        # Adding model 'KnowledgeSpecialization'
        db.create_table('charsheet_knowledgespecialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['KnowledgeSpecialization'])

        # Adding unique constraint on 'KnowledgeSpecialization', fields ['char', 'name']
        db.create_unique('charsheet_knowledgespecialization', ['char_id', 'name'])

        # Removing M2M table for field spec on 'Character'
        db.delete_table('charsheet_character_spec')

        # Adding M2M table for field expertise on 'Character'
        db.create_table('charsheet_character_expertise', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['charsheet.character'], null=False)),
            ('expertise', models.ForeignKey(orm['charsheet.expertise'], null=False))
        ))
        db.create_unique('charsheet_character_expertise', ['character_id', 'expertise_id'])

        # Deleting field 'Expertise.character'
        db.delete_column('charsheet_expertise', 'character_id')


    def backwards(self, orm):
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

        # Adding model 'Specialization'
        db.create_table('charsheet_specialization', (
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('charsheet', ['Specialization'])

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

        # Adding M2M table for field spec on 'Character'
        db.create_table('charsheet_character_spec', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['charsheet.character'], null=False)),
            ('specialization', models.ForeignKey(orm['charsheet.specialization'], null=False))
        ))
        db.create_unique('charsheet_character_spec', ['character_id', 'specialization_id'])

        # Removing M2M table for field expertise on 'Character'
        db.delete_table('charsheet_character_expertise')


        # User chose to not deal with backwards NULL issues for 'Expertise.character'
        raise RuntimeError("Cannot reverse this migration. 'Expertise.character' and its values cannot be restored.")

    models = {
        'charsheet.armour': {
            'Meta': {'object_name': 'Armour'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.athleticsspecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'AthleticsSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'charsheet.battlespecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'BattleSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'gender': ('django.db.models.fields.CharField', [], {'default': "'Undefined'", 'max_length': '6'}),
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
        'charsheet.commonspecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'CommonSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'charsheet.customknowledgespecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'CustomKnowledgeSpecialization'},
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
        'charsheet.knowledgespecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'KnowledgeSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'charsheet.mysticalspecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'MysticalSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'charsheet.socialspecialization': {
            'Meta': {'unique_together': "(('char', 'name'),)", 'object_name': 'SocialSpecialization'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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