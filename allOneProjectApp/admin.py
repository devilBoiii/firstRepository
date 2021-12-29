from django.contrib import admin
from allOneProjectApp.models import onePiece
# Register your models here.

class onePieceAdmin(admin.ModelAdmin):

	list_display=('Char_id','Name','Age','Roles','Power')

admin.site.register(onePiece,onePieceAdmin)