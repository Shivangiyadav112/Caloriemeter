from django.shortcuts import render
import json
import requests

# LPshNMe3p5WejHMPvqM39Q==j6ks0vfLZVjT32ld
# Create your views here.
def home(request):
    
    if request.method =='POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get (api_url + query, headers={'X-Api-Key': 'LPshNMe3p5WejHMPvqM39Q==j6ks0vfLZVjT32ld'})
        try:
            api =json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "Oops! There was an error "
            print(e)
        return render(request,'webpages/home.html',{'api':api,'query':query})
    else:
        return render(request,'webpages/home.html',{'query':'Enter a valid query'})


    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'LPshNMe3p5WejHMPvqM39Q==j6ks0vfLZVjT32ld'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
 
def exercise(request):
    
    if request.method =='POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api = requests.get (api_url + query , headers={'X-Api-Key': 'LPshNMe3p5WejHMPvqM39Q==j6ks0vfLZVjT32ld'}).json()
        return render(request,'webpages/exercise.html',{'api':api})
    else:
        return render(request,'webpages/exercise.html')
    
   
  
