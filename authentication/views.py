from django.shortcuts import render
from first_app.forms import AddPersonForm

import json
import requests

# Create your views here.

def third_party_post_api(request):
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        data = form.data
        url = 'http://127.0.0.1/api/add-person'
        api = requests.post(url=url,data=data)

        try:
            response = json.loads(api.text)
        except ConnectionError as e:
            response = None
    else:
        form = AddPersonForm()
    
    return render(request, 'add-person.html', {'form':form})
