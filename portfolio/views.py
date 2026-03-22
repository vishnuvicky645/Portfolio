from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.conf import settings

from .forms import ContactMessageForm
from .models import (
	Achievement,
	Certificate,
	Education,
	Experience,
	OpenSourceContribution,
	Profile,
	Project,
	Skill,
)


def home(request):
	if request.method == "POST":
		form = ContactMessageForm(request.POST)
		if form.is_valid():
			contact_message = form.save()

			receiver_email = settings.CONTACT_RECEIVER_EMAIL
			if receiver_email:
				email_subject = f"Portfolio Contact: {contact_message.subject}"
				email_body = (
					f"You received a new contact message from your portfolio form.\n\n"
					f"Name: {contact_message.full_name}\n"
					f"Email: {contact_message.email}\n"
					f"Subject: {contact_message.subject}\n\n"
					f"Message:\n{contact_message.message}"
				)
				try:
					sent_count = send_mail(
						subject=email_subject,
						message=email_body,
						from_email=settings.DEFAULT_FROM_EMAIL,
						recipient_list=[receiver_email],
						fail_silently=False,
					)
				except Exception:
					messages.warning(
						request,
						"Message saved, but email notification could not be sent. Check your email settings.",
					)
				else:
					if sent_count == 1:
						messages.success(request, "Your message was sent successfully.")
					else:
						messages.warning(
							request,
							"Message saved, but email notification was not delivered.",
						)
			else:
				messages.warning(
					request,
					"Message saved, but email receiving address is not configured.",
				)
			return redirect("portfolio:home")
	else:
		form = ContactMessageForm()

	profile = Profile.objects.first()
	programming_languages = Skill.objects.filter(category="programming_languages")
	frameworks_libraries = Skill.objects.filter(category="frameworks_libraries")
	tools = Skill.objects.filter(category="tools")
	databases = Skill.objects.filter(category="databases")
	soft_skills = Skill.objects.filter(category="soft")
	projects = Project.objects.all()
	certificates = Certificate.objects.all()
	experiences = Experience.objects.all()
	educations = Education.objects.all()
	achievements = Achievement.objects.all()
	open_source_contributions = OpenSourceContribution.objects.all()

	context = {
		"profile": profile,
		"programming_languages": programming_languages,
		"frameworks_libraries": frameworks_libraries,
		"tools": tools,
		"databases": databases,
		"soft_skills": soft_skills,
		"projects": projects,
		"certificates": certificates,
		"experiences": experiences,
		"educations": educations,
		"achievements": achievements,
		"open_source_contributions": open_source_contributions,
		"form": form,
	}
	return render(request, "portfolio/home.html", context)
