# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meeting'
        db.create_table(u'agendas_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('agenda_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'agendas', ['Meeting'])

        # Adding model 'AgendaItem'
        db.create_table(u'agendas_agendaitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agendas.Meeting'])),
            ('section', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('minutes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('backup', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'agendas', ['AgendaItem'])


    def backwards(self, orm):
        # Deleting model 'Meeting'
        db.delete_table(u'agendas_meeting')

        # Deleting model 'AgendaItem'
        db.delete_table(u'agendas_agendaitem')


    models = {
        u'agendas.agendaitem': {
            'Meta': {'object_name': 'AgendaItem'},
            'backup': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agendas.Meeting']"}),
            'minutes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'agendas.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'agenda_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['agendas']