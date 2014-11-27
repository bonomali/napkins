# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'soda_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('img', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('links', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'soda', ['Company'])

        # Adding model 'User'
        db.create_table(u'soda_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('num_apps_left_today', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['soda.Profile'], null=True)),
        ))
        db.send_create_signal(u'soda', ['User'])

        # Adding model 'Profile'
        db.create_table(u'soda_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('github_url', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('linkedin_url', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('personal_site_url', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('college', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('gpa', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('address', self.gf('django.db.models.fields.CharField')(default='', max_length=230)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=130)),
            ('state', self.gf('django.db.models.fields.CharField')(default='', max_length=130)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(default='', max_length=130)),
            ('coverletter', self.gf('django.db.models.fields.CharField')(default='', max_length=15000)),
            ('resume', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, blank=True)),
        ))
        db.send_create_signal(u'soda', ['Profile'])

        # Adding model 'Application'
        db.create_table(u'soda_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['soda.User'], null=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['soda.Company'], null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=30)),
        ))
        db.send_create_signal(u'soda', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'soda_company')

        # Deleting model 'User'
        db.delete_table(u'soda_user')

        # Deleting model 'Profile'
        db.delete_table(u'soda_profile')

        # Deleting model 'Application'
        db.delete_table(u'soda_application')


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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'num_apps_left_today': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['soda.Profile']", 'null': 'True'})
        }
    }

    complete_apps = ['soda']