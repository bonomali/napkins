# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.fb_id'
        db.add_column(u'soda_user', 'fb_id',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.fb_id'
        db.delete_column(u'soda_user', 'fb_id')


    models = {
        u'soda.application': {
            'Meta': {'object_name': 'Application'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['soda.Company']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['soda.User']", 'null': 'True'})
        },
        u'soda.company': {
            'Meta': {'object_name': 'Company'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'links': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'soda.profile': {
            'Meta': {'object_name': 'Profile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '230'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '130'}),
            'college': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'coverletter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15000'}),
            'github_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'gpa': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'personal_site_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'resume': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '130'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '130'})
        },
        u'soda.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'num_apps_left_today': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['soda.Profile']", 'null': 'True'})
        }
    }

    complete_apps = ['soda']