from django.db import models


class Profile(models.Model):
	full_name = models.CharField(max_length=120)
	headline = models.CharField(max_length=200)
	short_intro = models.TextField()
	about_me = models.TextField()
	college_name = models.CharField(max_length=180, blank=True)
	branch = models.CharField(max_length=120, blank=True)
	current_year = models.CharField(max_length=60, blank=True)
	career_goal = models.TextField(blank=True)
	hobbies = models.TextField(blank=True)
	profile_image = models.FileField(upload_to="profile/", blank=True)
	email = models.EmailField()
	phone = models.CharField(max_length=20, blank=True)
	location = models.CharField(max_length=120, blank=True)
	linkedin_url = models.URLField(blank=True)
	github_url = models.URLField(blank=True)
	resume_url = models.URLField(blank=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Profile"

	def __str__(self):
		return self.full_name


class Skill(models.Model):
	SKILL_CATEGORIES = (
		("programming_languages", "Programming Languages"),
		("frameworks_libraries", "Frameworks/Libraries"),
		("tools", "Tools"),
		("databases", "Databases"),
		("soft", "Soft Skills"),
	)

	SKILL_TYPES = (
		("technical", "Technical"),
		("soft", "Soft"),
	)

	name = models.CharField(max_length=80)
	category = models.CharField(max_length=40, choices=SKILL_CATEGORIES, default="programming_languages")
	skill_type = models.CharField(max_length=20, choices=SKILL_TYPES, default="technical")
	proficiency = models.PositiveSmallIntegerField(default=80)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "name"]

	def __str__(self):
		return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
	title = models.CharField(max_length=140)
	description = models.TextField()
	technologies = models.CharField(max_length=240)
	project_image = models.FileField(upload_to="projects/", blank=True)
	image_url = models.URLField(blank=True)
	github_url = models.URLField(blank=True)
	live_url = models.URLField(blank=True)
	is_featured = models.BooleanField(default=True)
	completed_on = models.DateField(blank=True, null=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "-completed_on", "title"]

	def __str__(self):
		return self.title


class Certificate(models.Model):
	title = models.CharField(max_length=160)
	issuer = models.CharField(max_length=120)
	issue_date = models.DateField(blank=True, null=True)
	credential_id = models.CharField(max_length=100, blank=True)
	credential_url = models.URLField(blank=True)
	certificate_file = models.FileField(upload_to="certificates/", blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "-issue_date", "title"]

	def __str__(self):
		return f"{self.title} - {self.issuer}"


class Experience(models.Model):
	role = models.CharField(max_length=160)
	organization = models.CharField(max_length=160, blank=True)
	duration = models.CharField(max_length=120)
	tech_used = models.CharField(max_length=240, blank=True)
	key_points = models.TextField(help_text="One point per line")
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "role"]

	def __str__(self):
		if self.organization:
			return f"{self.role} - {self.organization}"
		return self.role


class Education(models.Model):
	degree = models.CharField(max_length=180)
	institution = models.CharField(max_length=180)
	year_range = models.CharField(max_length=100, blank=True)
	cgpa = models.CharField(max_length=40, blank=True)
	description = models.TextField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "degree"]

	def __str__(self):
		return f"{self.degree} - {self.institution}"


class Achievement(models.Model):
	title = models.CharField(max_length=180)
	details = models.TextField(blank=True)
	year = models.CharField(max_length=20, blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "title"]

	def __str__(self):
		return self.title


class OpenSourceContribution(models.Model):
	title = models.CharField(max_length=180)
	repository = models.CharField(max_length=220, blank=True)
	description = models.TextField(blank=True)
	pr_link = models.URLField(blank=True)
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["display_order", "title"]

	def __str__(self):
		return self.title


class ContactMessage(models.Model):
	full_name = models.CharField(max_length=120)
	email = models.EmailField()
	subject = models.CharField(max_length=160)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.full_name} - {self.subject}"
