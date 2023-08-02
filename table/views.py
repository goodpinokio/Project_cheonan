from django.shortcuts import render
  # Replace with your actual model

def table_view(request):
    return render(
        request,
        'table/table.html',
    )