from django.contrib import admin
from django.utils.html import format_html
from Home.models import Contact,Service,Rating,Properties,Agents,About,Team,Image

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

class ServiceAdmin(admin.ModelAdmin):
    list_display=('Service_icon','Service_title','short_description')
    search_fields = ('Service_title',)

    def short_description(self,obj):
        return obj.Service_decs[:50] + ('...' if len(obj.Service_decs) > 50 else '')
    
    short_description.short_description  = 'Service_decs'

class RatingAdmin(admin.ModelAdmin):
    list_display=('Rating_title','short_description','get_rating_image','Rating_about')
    
    def get_rating_image(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Rating_image.url)
    
    def short_description(self, obj):
        return obj.Rating_decs[:40] + ('...'if len(obj.Rating_decs) > 40 else '')

    short_description.short_description = 'Description'
    get_rating_image.short_description = 'Rating Image'
class PropertiesAdmin(admin.ModelAdmin):
    list_display = (
        'Properties_name',
        'Properties_address',
        'get_properties_image',
        'Properties_price',
        'agent',
        'short_description',  # Use the truncated description here
        'get_properties_image1',
        'get_properties_image2',
        'get_properties_image3'  
    )
    search_fields = ('Properties_name', 'agent__Agents_name')  # Ensure fields match model definitions

    def short_description(self, obj):
        # Truncate the description to the first 100 characters
        return obj.Properties_desc[:60] + ('...' if len(obj.Properties_desc) > 60 else '')
    
    def get_properties_image(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Properties_image.url)
    
    def get_properties_image1(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Properties_image1.url)
    
    def get_properties_image2(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Properties_image2.url)
    
    def get_properties_image3(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Properties_image3.url)
    
    short_description.short_description = 'Description' 
    get_properties_image.short_description = 'Properties Image'
    get_properties_image1.short_description = 'Properties Image1'
    get_properties_image2.short_description = 'Properties Image2'
    get_properties_image3.short_description = 'Properties Image3'

class AgentsAdmin(admin.ModelAdmin):
    list_display=('Agents_name','Agents_desc1','get_agents_image','Agents_phone')

    def get_agents_image(self,obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.Agents_image.url)

class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'About_icone',
        'About_name',
        'short_about_desc1',
        'get_about_image',  # Use the custom method to display the image
        'short_about_us1',
        'short_about_us2'
    )

    def short_about_desc1(self, obj):
        # Truncate About_desc1 to the first 40 words
        return ' '.join(obj.About_desc1.split()[:50]) + ('...' if len(obj.About_desc1.split()) > 50 else '')
    
    def short_about_us1(self, obj):
        # Truncate About_Us1 to the first 40 words
        return ' '.join(obj.About_Us1.split()[:20]) + ('...' if len(obj.About_Us1.split()) > 20 else '')

    def short_about_us2(self, obj):
        # Truncate About_Us2 to the first 40 words
        return ' '.join(obj.About_Us2.split()[:20]) + ('...' if len(obj.About_Us2.split()) > 20 else '')

    def get_about_image(self, obj):
        # Render the image as a thumbnail (passport size)
        return format_html('<img src="{}" width="100" height="100" />', obj.About_image.url)

    short_about_desc1.short_description = 'About Desc1'
    short_about_us1.short_description = 'About Us1'
    short_about_us2.short_description = 'About Us2'
    get_about_image.short_description = 'About Image' 

class TeamAdmin(admin.ModelAdmin):
    list_display=('Team_name','short_team_decs','Team_rank','get_team_image','Team_phone')

    def short_team_decs(self,obj):
        return obj.Team_desc[:80] + ('...' if len(obj.Team_desc) > 80 else '')
    
    def get_team_image(self,obj):

        return format_html('<img src="{}" width="100" height="100" />', obj.Team_image.url)
    
    short_team_decs.short_description = 'Team desc'
class ImageAdmin(admin.ModelAdmin):
    list_display=('Image_name','Images')



# Register your models here.
admin.site.register(Contact,ContactAdmin )
admin.site.register(Service,ServiceAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Properties,PropertiesAdmin)
admin.site.register(Agents,AgentsAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Image,ImageAdmin)