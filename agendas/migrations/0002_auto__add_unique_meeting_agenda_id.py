# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Meeting', fields ['agenda_id']
        db.create_unique(u'agendas_meeting', ['agenda_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Meeting', fields ['agenda_id']
        db.delete_unique(u'agendas_meeting', ['agenda_id'])


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
            'agenda_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['agendas']