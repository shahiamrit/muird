from django.contrib import admin
from . models import Slider, Iru, Vmgo, About, Gallary
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# admin.site.register(Slider)
# admin.site.register(Iru)

class SliderAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

class IruAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

class VMgoAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(About, AboutAdmin)



admin.site.register(Slider, SliderAdmin)
admin.site.register(Iru, IruAdmin)
admin.site.register(Vmgo, VMgoAdmin)
admin.site.register(Gallary)
