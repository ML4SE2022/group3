def get_list(request):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'list.html', {'list': list})