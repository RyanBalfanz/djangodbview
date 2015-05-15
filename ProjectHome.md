Django dbview allows developers to see models, database structure and data in the admin panel.

Sometimes during development you need to see data, structure or model that is not included (and you do not plan to include it) to the admin panel. This application needs for such cases. It gives you full information about your models.

## Note: ##
Django dbview uses proxy model, so dbview only works with django 1.1 or higher.
dbview shows all of the models (and their data) of your application, and there is no way to exclude some of them.

## Installation: ##
You need the django admin panel installed and configured.
Add django dbview to your installed applications in the settings.py

```
INSTALLED_APPS = (
    ...,
    ...,
    ...,
    'dbview',)
```
After that find Dbview link in the admin panel.

## Removing: ##
Removing is very simple too. Just remove 'dbview' from INSTALLED\_APPS, and remove its directory from project.

## Screenshot ##
dbview shows permissions model.
![http://savepic.ru/1209315.png](http://savepic.ru/1209315.png)
