from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoItem


"""
------------------

Demonstrate simple CRUD Operations in django DB

------------------
"""
"Things to do"
# List Todo Items in DB
def All_Items (request):
        all_items = TodoItem.objects.all
        return render(request, 'todo.html', {'all_items': all_items})
# Add a Todo Item

# Delete a TodoItem
def deleteItem(request, todo_id):
        item_to_delete = TodoItem.objects.get(id=todo_id)
        item_to_delete.delete()
        return HttpResponseRedirect('/todo')

# Update a todo Item




