# Generated by Django 2.1.15 on 2020-07-22 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_utc_to_tli_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(help_text='Add a heading for this note')),
                ('content', models.TextField(blank=True, help_text='Add the content of this note')),
            ],
        ),
        migrations.AlterField(
            model_name='savedreport',
            name='report_type',
            field=models.CharField(max_length=128),
        ),
        migrations.AddField(
            model_name='reportnote',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.SavedReport'),
        ),
    ]
