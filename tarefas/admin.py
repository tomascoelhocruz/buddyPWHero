from django.contrib import admin

# Register your models here.
from .models import Contact, Comment, Networking, Quizz, QuizzAval, Comentarios, CommonUser, Like, Post

admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Networking)
admin.site.register(Quizz)
admin.site.register(QuizzAval)
admin.site.register(Comentarios)
admin.site.register(CommonUser)
admin.site.register(Like)
admin.site.register(Post)
