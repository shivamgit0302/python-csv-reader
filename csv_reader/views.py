from django.shortcuts import render
import csv

# Create your views here.

def read_csv(request):
    headers = data = []
    try:
        with open('spacex_launch_data.csv', 'r' , encoding='UTF-8') as file:   # Opens file in read mode
            reader=csv.DictReader((file))
            headers = [col for col in reader.fieldnames]
            data = [row for row in reader] 
    except Exception as error:    #cathces exception ex. in this case FileNotFoundError 
        print(error)        
    
    return render(request, 'datatable.html', {
        'headers': headers,
        'data': data,
    }) 
