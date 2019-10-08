from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Student


# Create your views here.
def index(request):
    return render(request, 'classroom/index.html')


def lists(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'classroom/lists.html', context)


def new(request):
    return render(request, 'classroom/new.html')


@require_POST
def create(request):
    student = Student()
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect(f'/classroom/students/{student.id}/')


def detail(request, num):
    student = get_object_or_404(Student, id=num)
    context = {'student': student}
    return render(request, 'classroom/detail.html', context)


def edit(request, num):
    student = Student.objects.get(id=num)
    context = {'student': student}
    return render(request, 'classroom/edit.html', context)


@require_POST
def update(request, num):
    student = Student.objects.get(id=num)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.save()
    return redirect(f'/classroom/students/{student.id}/')


@require_POST
def delete(request, num):
    student = Student.objects.get(id=num)
    student.delete()
    return redirect('/classroom/students/')
