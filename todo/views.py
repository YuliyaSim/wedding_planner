from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Coordinator
from todo.forms import *

from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.urls import reverse_lazy
from funky_sheets.formsets import HotView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return render(request, 'todo/index.html', {'todos': todos, 'categories':categories})
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo

    return render(request, 'todo/index.html', {'todos': todos, 'categories':categories})

    # third if:
        # checkedlist = tuple(map(int, request.POST["checkedbox"])) #checked todos to be deleted
        # TodoList.objects.filter(pk__in=checkedlist).delete()


class CreateCoordinationView(HotView, LoginRequiredMixin):
    # Define model to be used by the view
    model = Coordinator
    # Define template
    template_name = 'todo/hot/coordinations.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes' # default: true
    checkbox_unchecked = 'no' # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('todo:update_coordination')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'id',
        'name',
        'role',
        'phone',
        'email',
        'website',
        'cost',
        'notes',
    )
    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        },
        # When value is list don't wrap it in quotes
        'dropdownMenu': [
            'remove_col',
            '---------',
            'make_read_only',
            '---------',
            'alignment'
        ]
    }


class UpdateCoordinationView(CreateCoordinationView, LoginRequiredMixin):
  template_name = 'todo/hot/update_coordination.html'
  # Define 'update' action
  action = 'update'
  # Define 'update' button
  button_text = 'Update'

  def get_queryset(self):
      return Coordinator.objects.all()



class CreateWeddingDayView(HotView, LoginRequiredMixin):
  # Define model to be used by the view
  model = WeddingDay
  # Define template
  template_name = 'todo/hot/create_wedding_day.html'
  # Define custom characters/strings for checked/unchecked checkboxes
  checkbox_checked = 'yes'  # default: true
  checkbox_unchecked = 'no'  # default: false
  # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
  prefix = 'table'
  # Define success URL
  success_url = reverse_lazy('todo:wedding_day')
  # Define fields to be included as columns into the Handsontable spreadsheet
  fields = (
      'id',
      'time',
      'item',
      'notes',
  )
  # Define extra formset factory kwargs
  factory_kwargs = {
      'widgets': {
          'release_date': DateInput(attrs={'type': 'date'}),
          'genre': CheckboxSelectMultiple(),
          'parents_guide': CheckboxInput(),
      }
  }
  # Define Handsontable settings as defined in Handsontable docs
  hot_settings = {
      'contextMenu': 'true',
      'autoWrapRow': 'true',
      'rowHeaders': 'true',
      'contextMenu': 'true',
      'search': 'true',
      'licenseKey': 'non-commercial-and-evaluation',
      # When value is dictionary don't wrap it in quotes
      'headerTooltips': {
          'rows': 'false',
          'columns': 'true'
      },
      # When value is list don't wrap it in quotes
      'dropdownMenu': [
          'remove_col',
          '---------',
          'make_read_only',
          '---------',
          'alignment'
      ]
  }


class WeddingDayView(CreateWeddingDayView, LoginRequiredMixin):
  template_name = 'todo/hot/wedding_day.html'
  action = 'update'
  button_text = 'Update'

  def get_queryset(self):
      return WeddingDay.objects.all()





