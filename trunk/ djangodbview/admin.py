from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.views.main import ChangeList
from dbview.models import ContentTypeProxy
from django.contrib.admin.sites import AdminSite

class ContentTypeProxyAdmin(admin.ModelAdmin):
    list_display = ["object_name", "app_label", "name", "admin_link", "table_name"]
    def change_view(self, request, object_id, extra_context=None):
        content_obj = self.model.objects.get(id=object_id)
        objects = content_obj.model_class().objects.all()
        cl = objects
        list_display = ('__str__',)
        list_display = [x.name for x in content_obj.model_class()._meta.fields]
        list_display_links = ()
        list_filter = ()
        list_select_related = False
        list_per_page = 40
        list_editable = ()
        search_fields = ()
        date_hierarchy = None
        save_as = False
        save_on_top = False
        ordering = None
        inlines = [] 
        
        # create model admin for such class
        current_model_admin = admin.ModelAdmin(content_obj.model_class(), AdminSite())
        
        # create Change list object.
        cl = ChangeList(request, content_obj.model_class(), list_display, list_display_links, list_filter,
                date_hierarchy, search_fields, list_select_related, list_per_page, list_editable, current_model_admin)
        
        cl.formset = None
        
        # what information about object to show in the admin panel 
        # all of them are attributes of model instance
        model_attrs = ["object_name", "db_table", "verbose_name", "proxy", "app_label",
                        "module_name"]

        model_info = []
        
        for attr in model_attrs:
            model_info.append({"name": attr, "value": cl.model._meta.__getattribute__(attr)})
        
        # what information about fields to show in the admin
        model_fields = {}
        model_fields["header"] = ["name", "internal_type", "max_length", "verbose_name",  
                                "unique", "rel", "null", "primary_key", "blank", "column", 
                                "db_column", "db_type", "db_index"]

        model_fields["fields"] = []
        for field in cl.model._meta.fields:
            field_list = []
            for attr in model_fields["header"]:
                # internal type is callable attribute
                if attr == "internal_type":
                    field_list.append(field.get_internal_type())
                    continue
                if attr == "db_type":
                    field_list.append(field.db_type())
                    continue
                attrib = field.__getattribute__(attr)
                if attr == "rel" and attrib:
                    field_list.append(attrib.to)
                    continue
                field_list.append(attrib)
                
            model_fields["fields"].append(field_list)

        return super(ContentTypeProxyAdmin, self).change_view(request, object_id, extra_context={"cl": cl,
                                                                                                 "model_info": model_info,
                                                                                                 "model_fields": model_fields})
        
admin.site.register(ContentTypeProxy, ContentTypeProxyAdmin)
