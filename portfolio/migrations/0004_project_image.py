from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_image",
            field=models.FileField(blank=True, upload_to="projects/"),
        ),
    ]
