from django.contrib import admin

# Register your models here.
from .models import Client,Todolist,Comment,MyModel,Expense

admin.site.register(Client)
admin.site.register(Todolist)
admin.site.register(Comment)
admin.site.register(MyModel)

admin.site.register(Expense)