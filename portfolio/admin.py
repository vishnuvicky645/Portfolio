from django.contrib import admin

from .models import (
	Achievement,
	Certificate,
	ContactMessage,
	Education,
	Experience,
	OpenSourceContribution,
	Profile,
	Project,
	Skill,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("full_name", "college_name", "current_year", "email", "location", "updated_at")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ("name", "category", "skill_type", "display_order")
	list_filter = ("category", "skill_type")
	search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "is_featured", "completed_on", "display_order")
	list_filter = ("is_featured",)
	search_fields = ("title", "technologies")
	exclude = ("project_image", "image_url", "live_url")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ("title", "issuer", "issue_date", "certificate_file", "display_order")
	search_fields = ("title", "issuer")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
	list_display = ("role", "organization", "duration", "display_order")
	search_fields = ("role", "organization", "tech_used")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	list_display = ("degree", "institution", "year_range", "cgpa", "display_order")
	search_fields = ("degree", "institution")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
	list_display = ("title", "year", "display_order")
	search_fields = ("title", "details")


@admin.register(OpenSourceContribution)
class OpenSourceContributionAdmin(admin.ModelAdmin):
	list_display = ("title", "repository", "display_order")
	search_fields = ("title", "repository", "description")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ("full_name", "email", "subject", "created_at", "is_read")
	list_filter = ("is_read", "created_at")
	search_fields = ("full_name", "email", "subject")
