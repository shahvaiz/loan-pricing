# -*- coding: utf-8 -*-
# from south.utils import datetime_utils as datetime
# from south.db import db
# from south.v2 import SchemaMigration
from django.db import models


from django.db import migrations, models
class Migration(migrations.Migration):

    def forwards(self, orm):
        # Adding field 'Application.program'
        db.add_column(u'myapp_application', 'program',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.down_payment'
        db.add_column(u'myapp_application', 'down_payment',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.cash_out'
        db.add_column(u'myapp_application', 'cash_out',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.county'
        db.add_column(u'myapp_application', 'county',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.rate'
        db.add_column(u'myapp_application', 'rate',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Application.ysp'
        db.add_column(u'myapp_application', 'ysp',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Application.apr'
        db.add_column(u'myapp_application', 'apr',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Application.payment'
        db.add_column(u'myapp_application', 'payment',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.title_costs_total'
        db.add_column(u'myapp_application', 'title_costs_total',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.points'
        db.add_column(u'myapp_application', 'points',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'Application.closing_costs'
        db.add_column(u'myapp_application', 'closing_costs',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Application.investor'
        db.add_column(u'myapp_application', 'investor',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Application.zip_code'
        db.alter_column(u'myapp_application', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True))

    def backwards(self, orm):
        # Deleting field 'Application.program'
        db.delete_column(u'myapp_application', 'program')

        # Deleting field 'Application.down_payment'
        db.delete_column(u'myapp_application', 'down_payment')

        # Deleting field 'Application.cash_out'
        db.delete_column(u'myapp_application', 'cash_out')

        # Deleting field 'Application.county'
        db.delete_column(u'myapp_application', 'county')

        # Deleting field 'Application.rate'
        db.delete_column(u'myapp_application', 'rate')

        # Deleting field 'Application.ysp'
        db.delete_column(u'myapp_application', 'ysp')

        # Deleting field 'Application.apr'
        db.delete_column(u'myapp_application', 'apr')

        # Deleting field 'Application.payment'
        db.delete_column(u'myapp_application', 'payment')

        # Deleting field 'Application.title_costs_total'
        db.delete_column(u'myapp_application', 'title_costs_total')

        # Deleting field 'Application.points'
        db.delete_column(u'myapp_application', 'points')

        # Deleting field 'Application.closing_costs'
        db.delete_column(u'myapp_application', 'closing_costs')

        # Deleting field 'Application.investor'
        db.delete_column(u'myapp_application', 'investor')


        # Changing field 'Application.zip_code'
        db.alter_column(u'myapp_application', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    models = {
        u'myapp.application': {
            'Meta': {'object_name': 'Application'},
            'apr': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'cash_out': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'closing_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
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
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'phone_work': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'property_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
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
