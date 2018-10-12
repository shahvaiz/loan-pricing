# -*- coding: utf-8 -*-
# from south.utils import datetime_utils as datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models


from django.db import migrations, models
class Migration(migrations.Migration):

    def forwards(self, orm):
        # Deleting model 'Application'
        db.delete_table(u'myapp_application')

        # Adding model 'Application2'
        db.create_table(u'myapp_application2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('phone_work', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('loan_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('loan_balance', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('loan_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('property_value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'myapp', ['Application2'])


    def backwards(self, orm):
        # Adding model 'Application'
        db.create_table(u'myapp_application', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('loan_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_work', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('property_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('loan_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('phone_home', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('phone_mobile', self.gf('django.db.models.fields.CharField')(max_length=13, null=True, blank=True)),
            ('loan_balance', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'myapp', ['Application'])

        # Deleting model 'Application2'
        db.delete_table(u'myapp_application2')


    models = {
        u'myapp.application2': {
            'Meta': {'object_name': 'Application2'},
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'loan_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'loan_balance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'loan_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'property_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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
