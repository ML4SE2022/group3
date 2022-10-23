from django.db.models import F

qs = Model.objects.all().values_list('field', flat=True)
qs = Model.objects.all().values_list('field', flat=True).distinct()
qs = Model.objects.all().values_list('field', flat=True).order_by('field')
qs = Model.objects.all().values_list('field', flat=True).order_by('-field')
qs = Model.objects.all().values_list('field', flat=True).order_by(F('field').desc())
qs = Model.objects.all().values_list('field', flat=True).order_by(F('field').asc())
qs = Model.objects.all().values_list('field', flat=True).order_by('field').distinct()
qs = Model.objects.all().values_list('field', flat=True).order_by('-field').distinct()
qs = Model.objects.all().values_list('field', flat=True).order_by(F('field').desc()).distinct()
qs = Model.objects.all().values_list('field', flat=True).order_by(F('field').asc()).distinct()