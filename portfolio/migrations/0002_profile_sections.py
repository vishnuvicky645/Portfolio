from django.db import migrations, models


def seed_new_sections(apps, schema_editor):
    Profile = apps.get_model("portfolio", "Profile")
    Education = apps.get_model("portfolio", "Education")
    Experience = apps.get_model("portfolio", "Experience")
    Achievement = apps.get_model("portfolio", "Achievement")
    OpenSourceContribution = apps.get_model("portfolio", "OpenSourceContribution")

    profile = Profile.objects.order_by("id").first()
    if profile:
        if not profile.college_name:
            profile.college_name = "Your College Name"
        if not profile.branch:
            profile.branch = "Computer Science and Engineering (CSE)"
        if not profile.current_year:
            profile.current_year = "3rd Year"
        if not profile.career_goal:
            profile.career_goal = (
                "To become a software engineer focused on scalable web products, "
                "clean architecture, and meaningful user experiences."
            )
        if not profile.hobbies:
            profile.hobbies = "Coding challenges, tech blogging, cricket, and exploring Linux tooling."
        profile.save()

    if not Education.objects.exists():
        Education.objects.create(
            degree="BTech in Computer Science and Engineering",
            institution="Your College Name",
            year_range="2023 - 2027",
            cgpa="8.5 / 10",
            description="Current undergraduate degree with focus on software development and core CS subjects.",
            display_order=1,
        )

    if not Experience.objects.exists():
        Experience.objects.create(
            role="Web Development Intern",
            organization="Example Company",
            duration="May 2025 - July 2025",
            tech_used="HTML, CSS, JavaScript, Django",
            key_points=(
                "Built responsive frontend components.\n"
                "Collaborated on backend APIs and bug fixes.\n"
                "Improved page load performance and UI consistency."
            ),
            display_order=1,
        )

    if not Achievement.objects.exists():
        Achievement.objects.bulk_create(
            [
                Achievement(
                    title="Top 10 finalist in college hackathon",
                    year="2025",
                    details="Built and presented a full-stack problem-solving project.",
                    display_order=1,
                ),
                Achievement(
                    title="Solved 300+ coding problems",
                    year="",
                    details="Practiced DSA and problem-solving across coding platforms.",
                    display_order=2,
                ),
            ]
        )

    if not OpenSourceContribution.objects.exists():
        OpenSourceContribution.objects.create(
            title="Documentation and bug-fix contributions",
            repository="github.com/yourusername/your-repo",
            description="Submitted pull requests for fixes and docs improvements.",
            pr_link="",
            display_order=1,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="branch",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="profile",
            name="career_goal",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="college_name",
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name="profile",
            name="current_year",
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name="profile",
            name="hobbies",
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name="Achievement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=180)),
                ("details", models.TextField(blank=True)),
                ("year", models.CharField(blank=True, max_length=20)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "title"]},
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("degree", models.CharField(max_length=180)),
                ("institution", models.CharField(max_length=180)),
                ("year_range", models.CharField(blank=True, max_length=100)),
                ("cgpa", models.CharField(blank=True, max_length=40)),
                ("description", models.TextField(blank=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "degree"]},
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=160)),
                ("organization", models.CharField(blank=True, max_length=160)),
                ("duration", models.CharField(max_length=120)),
                ("tech_used", models.CharField(blank=True, max_length=240)),
                (
                    "key_points",
                    models.TextField(help_text="One point per line"),
                ),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "role"]},
        ),
        migrations.CreateModel(
            name="OpenSourceContribution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=180)),
                ("repository", models.CharField(blank=True, max_length=220)),
                ("description", models.TextField(blank=True)),
                ("pr_link", models.URLField(blank=True)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["display_order", "title"]},
        ),
        migrations.RunPython(seed_new_sections, migrations.RunPython.noop),
    ]
