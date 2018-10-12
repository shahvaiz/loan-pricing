# -*- coding: utf-8 -*-
# from south.utils import datetime_utils as datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models

from django.db import migrations, models

class Migration(migrations.Migration):

    def forwards(self, orm):
        # Deleting field 'Inquiry.name'
        db.delete_column(u'myapp_inquiry', 'name')

        # Adding field 'Inquiry.first_name'
        db.add_column(u'myapp_inquiry', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Inquiry.name'
        db.add_column(u'myapp_inquiry', 'name',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2015, 5, 12, 0, 0), max_length=40),
                      keep_default=False)

        # Deleting field 'Inquiry.first_name'
        db.delete_column(u'myapp_inquiry', 'first_name')


    models = {
        u'myapp.application': {
            'Meta': {'object_name': 'Application'},
            'apr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'cash_out': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'closing_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'down_payment': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investor': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'loan_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'loan_balance': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'loan_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'payment': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'property_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_costs_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'ysp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'myapp.countyfees': {
            'Meta': {'object_name': 'CountyFees'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recording': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'taxes': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'myapp.inquiry': {
            'Meta': {'object_name': 'Inquiry'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
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
