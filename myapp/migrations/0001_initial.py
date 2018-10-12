# -*- coding: utf-8 -*-
#from south.utils import datetime_utils as datetime
#from south.db import db
#from south.v2 import SchemaMigration
from django.db import models

from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):
        # Adding model 'RegionInfo'
        db.create_table(u'myapp_regioninfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_abbreviatison', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'myapp', ['RegionInfo'])

        # Adding model 'CountyFees'
        db.create_table(u'myapp_countyfees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('recording', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('taxes', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'myapp', ['CountyFees'])


    def backwards(self, orm):
        # Deleting model 'RegionInfo'
        db.delete_table(u'myapp_regioninfo')

        # Deleting model 'CountyFees'
        db.delete_table(u'myapp_countyfees')


    models = {
        u'myapp.countyfees': {
            'Meta': {'object_name': 'CountyFees'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recording': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'taxes': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'myapp.regioninfo': {
            'Meta': {'object_name': 'RegionInfo'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['myapp']
