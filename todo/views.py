from django.views.generic import TemplateView, ListView, UpdateView

# from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
 
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TodoItem
from .forms import InputForm


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
def edit(request, todo_id):
        if request.method == 'POST':
                item = TodoItem.objects.get(pk=todo_id)
                form = InputForm(request.POST or None, instance=item)

                if form.is_valid():
                        form.save()
                        #       output message
                        return redirect('/todo')
        else:
                item = TodoItem.objects.get(pk=todo_id)
                return render(request, 'edit.html', {'item': item}) 


def detailView(request, todo_id):
        item = TodoItem.objects.get(pk=todo_id)
        return render(request, 'detail.html', {'item': item})


class UpdateView(UpdateView):
        model = TodoItem
        template_name = "update.html"
        def getobj(self, id, queryset=None):
                id = self.kwargs['id']
                return self.model.objects.get(id=id)
        def formValid(self, form):
                form.save()
                return HttpResponseRedirect(reverse('todo'))



