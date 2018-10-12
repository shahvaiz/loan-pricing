# -*- coding: utf-8 -*-
# from south.utils import datetime_utils as datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models

from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):
        # Deleting model 'Customers'
        db.delete_table(u'myapp_customers')

        # Adding model 'Application'
        db.create_table(u'myapp_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone_work', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('loan_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('loan_balance', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('loan_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('property_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('property_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'myapp', ['Application'])


    def backwards(self, orm):
        # Adding model 'Customers'
        db.create_table(u'myapp_customers', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone_work', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'myapp', ['Customers'])

        # Deleting model 'Application'
        db.delete_table(u'myapp_application')


    models = {
        u'myapp.application': {
            'Meta': {'object_name': 'Application'},
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'loan_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'loan_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'loan_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'property_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
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
