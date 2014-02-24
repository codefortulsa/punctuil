# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Alert.phone'
        db.alter_column(u'agendas_alert', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))

    def backwards(self, orm):

        # Changing field 'Alert.phone'
        db.alter_column(u'agendas_alert', 'phone', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'agendas.agendaitem': {
            'Meta': {'object_name': 'AgendaItem'},
            'backup': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['agendas.Meeting']"}),
            'minutes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'agendas.alert': {
            'Meta': {'object_name': 'Alert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alerts'", 'to': u"orm['agendas.AgendaItem']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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