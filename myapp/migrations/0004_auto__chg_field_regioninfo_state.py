# -*- coding: utf-8 -*-
#from south.utils import datetime_utils as datetime
#from south.db import db
#from south.v2 import SchemaMigration
from django.db import models

from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):

        # Changing field 'RegionInfo.state'
        db.alter_column(u'myapp_regioninfo', 'state', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'RegionInfo.state'
        db.alter_column(u'myapp_regioninfo', 'state', self.gf('django.db.models.fields.CharField')(max_length=15))

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
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['myapp']
