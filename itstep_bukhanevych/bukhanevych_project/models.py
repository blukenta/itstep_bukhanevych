from django.db import models
from django_extensions.db.fields import ShortUUIDField

class TodoItem(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

def update_todo_item(id, state):
    todoitem = TodoItem.objects.get(id=id)
    if todoitem != None:
        todoitem.completed = bool(state)
        todoitem.save()