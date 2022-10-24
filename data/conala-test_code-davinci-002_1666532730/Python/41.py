from django.db.models import Max

max_value = Model.objects.all().aggregate(Max('field_name'))