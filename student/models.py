from django.db import models

# Create your models here.


class AdminData(models.Model):
    username = models.TextField(max_length=100, unique=True, blank=False)
    password = models.TextField(max_length=100, blank=False)
    dept_id = models.TextField(max_length=50, blank=False)
    enroll_no = models.TextField(max_length=50, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class StudentData(models.Model):
    enroll_no = models.TextField(max_length=50, unique=True, blank=False)
    username = models.TextField(max_length=100, unique=False, blank=False)
    password = models.TextField(max_length=100, blank=False)
    dept_id = models.TextField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tuition = models.IntegerField(default=0)  # cents


class Resources(models.Model):
    title = models.TextField(max_length=100, blank=False)
    details = models.TextField(max_length=1000, blank=False)
    type = models.TextField(max_length=50, blank=False)
    file_name = models.TextField(max_length=50, blank=False)
    file_link = models.TextField(max_length=100, blank=False)
    dept_id = models.TextField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Clubs(models.Model):
    title = models.TextField(max_length=100, blank=False)
    details = models.TextField(max_length=1000, blank=False)
    file_name = models.TextField(max_length=50, blank=False)
    file_link = models.TextField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.TextField(max_length=100, blank=False)
    details = models.TextField(max_length=1000, blank=False)
    file_name = models.TextField(max_length=50, blank=False)
    file_link = models.TextField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Placements(models.Model):
    company = models.TextField(max_length=100, blank=False)
    details = models.TextField(max_length=1000, blank=False)
    document = models.TextField(max_length=50, blank=False, null=True)
    documentUrl = models.TextField(max_length=100, blank=False, null=True)
    form_link = models.TextField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
