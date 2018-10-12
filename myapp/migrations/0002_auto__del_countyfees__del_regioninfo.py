# -*- coding: utf-8 -*-
#from south.utils import datetime_utils as datetime
#from south.db import db
#from south.v2 import SchemaMigration
from django.db import models
from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):
        # Deleting model 'CountyFees'
        db.delete_table(u'myapp_countyfees')

        # Deleting model 'RegionInfo'
        db.delete_table(u'myapp_regioninfo')


    def backwards(self, orm):
        # Adding model 'CountyFees'
        db.create_table(u'myapp_countyfees', (
            ('county', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('recording', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taxes', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'myapp', ['CountyFees'])

        # Adding model 'RegionInfo'
        db.create_table(u'myapp_regioninfo', (
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('state_abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'myapp', ['RegionInfo'])


    models = {

    }

    complete_apps = ['myapp']
