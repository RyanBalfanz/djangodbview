from django.db import models
from django.contrib.contenttypes.models import ContentType

class ContentTypeProxy(ContentType):
    class Meta:
        verbose_name = "Models"
        verbose_name_plural = "Models"
        proxy = True
    
    def table_name(self):
        """ returns database table name """
        return self.model_class()._meta.db_table
        
    def object_name(self):
        """ returns model name """
        return self.model_class()._meta.object_name

    def admin_link(self):
        """ returns link where object live in the admin panel"""
        # in case the object has not included to the admin panel, points nowhere
        return "<a href='/admin/%s/%s/'>%s</a>" % (self.app_label, self.model, self.model_class()._meta.object_name)
                
    admin_link.allow_tags = True
        
