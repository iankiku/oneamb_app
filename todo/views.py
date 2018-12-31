from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoItem
from .forms import updateForm


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
def addTodo(request):
        new_item = TodoItem(content = request.POST['content'])
        new_item.save()
        return HttpResponseRedirect('/todo/')


# Delete a TodoItem
def deleteItem(request, todo_id):
        item_to_delete = TodoItem.objects.get(id=todo_id)
        item_to_delete.delete()
        return HttpResponseRedirect('/todo')


# Update a todo Item
def updateItem(request, todo_id):
        if request.method == 'POST':
                formVal = updateForm(request.POST)
                

                if formVal.is_valid():
                        pass    # validate form
                        # save form data
                        
                        return HttpResponseRedirect('/todo') #redirect todo list
                else:
                        pass #show errors if failed
                        #return


        # after updating item return to home
        return HttpResponseRedirect('/todo')







def detailView(request, todo_id):
        item = TodoItem.objects.get(pk=todo_id)
        return render(request, 'detail.html', {'item': item})




