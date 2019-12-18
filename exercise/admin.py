from django.contrib import admin
from .models import Tree
from .models import Ground
from .models import Root
from .models import Trunk
from .models import Leaf
from .models import Branch
# Register your models here.

admin.site.register(Tree)
admin.site.register(Ground)
admin.site.register(Root)
admin.site.register(Trunk)
admin.site.register(Leaf)
