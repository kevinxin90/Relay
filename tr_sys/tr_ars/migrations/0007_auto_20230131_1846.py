# Generated by Django 3.2.4 on 2023-01-31 18:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tr_ars', '0006_message_result_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='result_stat',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('D', 'Done'), ('S', 'Stopped'), ('R', 'Running'), ('E', 'Error'), ('W', 'Waiting'), ('U', 'Unknown')], db_index=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]