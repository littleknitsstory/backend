from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    title = models.CharField(_("Title"), max_length=63, null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")


class CourseContent(models.Model):
    model_id = models.IntegerField(_("Model ID"))
    model_type = models.CharField(_("Model type"), max_length=63)


class Step(models.Model):
    title = models.CharField(_("Title"), max_length=63, null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    course = models.ForeignKey(
        Course,
        related_name="step_course",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Course")
    )
    content = models.ManyToManyField(
        CourseContent, related_name="step_contents", blank=True, verbose_name=_("Contents")
    )

