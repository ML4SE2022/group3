from django.db.models import Q

Book.objects.filter(Q(authors__name='Author1') & Q(authors__name='Author2'))