from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import render
from .models import EntryForm

admin.site.register(EntryForm)
