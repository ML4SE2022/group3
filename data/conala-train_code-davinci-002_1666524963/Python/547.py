from django.db.models import F

# Get all models ordered by the name of its OneToOne model
Model.objects.order_by(F('one_to_one_model__name'))