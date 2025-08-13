from django.contrib import admin
from defects.models import defectData, DeveloperData, TesterData, Defect_Screenshot

# Register your models here.
admin.site.register(defectData)
admin.site.register(DeveloperData)
admin.site.register(TesterData)
admin.site.register(Defect_Screenshot)

# SUPERUSER 
# python manage.py createsuperuser
# user : defectadmin
# email : defect@gmail.com
# password : qwert


# users data
# username : Android
# password : 123456

# username : Apple
# password : 67890

# username : Sachin
# password : yuiop

# username : John
# password : john12

# username : Priya
# password : priya34

# username : King
# password : king56