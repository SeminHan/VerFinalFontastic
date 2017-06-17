from django.contrib import admin
from .models import Post,Question,Call,Upload,Search,Font,call_Comment , question_Comment,Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display =['id','title','created_at']
	list_display_links = ['title']

@admin.register(Question)
class question_board_Admin(admin.ModelAdmin):
	list_display=['id','title','created_at']
	list_display_links = ['title']

@admin.register(Call)
class call_board_Admin(admin.ModelAdmin):
	list_display=['id','title','created_at']
	list_display_links = ['title']

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
	list_display = ['id','photo']
	list_display_links = ['id']

@admin.register(Search)
class FontAdmin(admin.ModelAdmin):
	list_display=['id', 'title']
	list_display_links = ['title']

@admin.register(Font)
class FontAdmin_data(admin.ModelAdmin):
	list_display = ['id','title']
	list_display_links = ['title']

@admin.register(call_Comment)
class call_comment_Admin(admin.ModelAdmin):
	list_display=['id','message']
	list_display_links=['message']

@admin.register(question_Comment)
class question_comment_Admin(admin.ModelAdmin):
	list_display=['id','message']
	list_display_links=['message']

@admin.register(Comment)
class post_comment_admin(admin.ModelAdmin):
	list_display=['id','message']
	list_display_links=['message']


# Register your models here.
