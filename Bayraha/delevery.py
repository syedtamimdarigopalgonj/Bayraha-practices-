from django.shortcuts import render

def delivery_view(request):
    result = None
    if request.method == 'POST':
        user_input = request.POST.get('input_name')
        result = f"Received: {user_input}"
    return render(request, 'delivery.html', {'result': result})