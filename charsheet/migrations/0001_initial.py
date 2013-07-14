# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialization'
        db.create_table('charsheet_specialization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('charsheet', ['Specialization'])

        # Adding model 'Character'
        db.create_table('charsheet_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('striker', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bep', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('stp', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('acu_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('acu_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bra_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('bra_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cor_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('cor_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('foc_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('foc_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('men_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('men_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('vit_vl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('vit_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ath_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('ath_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bat_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('bat_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('com_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('com_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kno_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('kno_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mys_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('mys_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('soc_lvl', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('soc_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('charsheet', ['Character'])

        # Adding M2M table for field spec on 'Character'
        db.create_table('charsheet_character_spec', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['charsheet.character'], null=False)),
            ('specialization', models.ForeignKey(orm['charsheet.specialization'], null=False))
        ))
        db.create_unique('charsheet_character_spec', ['character_id', 'specialization_id'])

        # Adding model 'Expertise'
        db.create_table('charsheet_expertise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ip', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cs', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('charsheet', ['Expertise'])

        # Adding model 'Weapon'
        db.create_table('charsheet_weapon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('charsheet', ['Weapon'])

        # Adding model 'Armour'
        db.create_table('charsheet_armour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('charsheet', ['Armour'])

        # Adding model 'Wound'
        db.create_table('charsheet_wound', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charsheet.Character'])),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('charsheet', ['Wound'])


    def backwards(self, orm):
        # Deleting model 'Specialization'
        db.delete_table('charsheet_specialization')

        # Deleting model 'Character'
        db.delete_table('charsheet_character')

        # Removing M2M table for field spec on 'Character'
        db.delete_table('charsheet_character_spec')

        # Deleting model 'Expertise'
        db.delete_table('charsheet_expertise')

        # Deleting model 'Weapon'
        db.delete_table('charsheet_weapon')

        # Deleting model 'Armour'
        db.delete_table('charsheet_armour')

        # Deleting model 'Wound'
        db.delete_table('charsheet_wound')


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
            'acu_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ath_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ath_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bat_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'bat_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bep': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'bra_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bra_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'com_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'com_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cor_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'foc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'foc_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kno_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'kno_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'men_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'mys_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'mys_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'soc_lvl': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'soc_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spec': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['charsheet.Specialization']", 'symmetrical': 'False'}),
            'stp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'striker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vit_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vit_vl': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'charsheet.expertise': {
            'Meta': {'object_name': 'Expertise'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['charsheet.Character']"}),
            'cs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'charsheet.specialization': {
            'Meta': {'object_name': 'Specialization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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