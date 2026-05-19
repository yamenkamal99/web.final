from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm
from datetime import date


def home(request):
    subjects = Subject.objects.all().order_by('exam_date')

    today = date.today()

    return render(request, 'planner/home.html', {
        'subjects': subjects,
        'today': today,
    })


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()

    return render(request, 'planner/add_subject.html', {
        'form': form
    })


def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm(instance=subject)

    return render(request, 'planner/edit_subject.html', {
        'form': form
    })


def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('home')

    return render(request, 'planner/delete_subject.html', {
        'subject': subject
    })