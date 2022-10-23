import random

def get_random_item(model):
    count = model.objects.count()
    random_index = random.randint(0, count - 1)
    return model.objects.all()[random_index]