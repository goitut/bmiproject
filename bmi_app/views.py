from django.shortcuts import render
from urllib3 import request

# Create your views here.
def calculate_bmi(request): 
    context = {}
    # Check if the user has clicked the submit button
    if request.method == 'POST':
        # Get data from the HTML form
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))

        # Your original formula 
        bmi = weight / (height ** 2)


        # Your orginal classificaltion logic 
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            category = 'Normal weight'
        elif 25 <= bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obesity'

        # Send data back to the webpage context, rounded to 2 decimal places


        context = {
            'bmi' : round(bmi, 2),
            'category' : category,
            'weight' : weight,
            'height' : height
        }

    return render(request, 'bmi_app/index.html', context)