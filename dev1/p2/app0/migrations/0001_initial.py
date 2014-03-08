# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'app0_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app0', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'app0_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proposition', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app0.Poll'])),
        ))
        db.send_create_signal(u'app0', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'app0_poll')

        # Deleting model 'Choice'
        db.delete_table(u'app0_choice')


    models = {
        u'app0.choice': {
            'Meta': {'object_name': 'Choice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app0.Poll']"}),
            'proposition': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'app0.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app0']