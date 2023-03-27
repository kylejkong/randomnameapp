from .models import Text
from django.shortcuts import render
import rstr

from django.http import JsonResponse
from django.views.generic import View



class AjaxHandlerView(View):
    def get(self, request):
        
        name1 = "([b-df-hj-np-tv-z]{1}[aeiou]){1,3}(?![\s\S]*\b\1\b)"
        name2 = "(([b-df-hj-np-tv-z]{1})[aeiou]){1,2}(?![\s\S]*\b\1\b)"
        text = request.GET.get('btn1') 
        text2 = request.GET.get('btn2') 
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if request.GET.get('btn1'):

                
                name1_male= "(yev|mov|nov|rov|sov|kov|vic|nic|kic|gic|bic|zic|ski|sky|nik|vak)"
                
                name1result = rstr.xeger(name1 + name1_male)

                
                return JsonResponse({'left':name1result}, status=200)
            elif request.GET.get('btn2'):
                
                name2_female = "(yeva|mova|nova|rova|sova|kova|vic|nic|kic|gic|bic|zic|ska|nik|vak)"
    
                name2result = rstr.xeger(name1 + name2_female)
            
                return JsonResponse({'right':name2result}, status=200)
            

            elif request.GET.get('btn3'):
                
                name2_male="(ro|o|to|ichi|ra|ga|wa|kio|ta)"
                name2_m = rstr.xeger(name2 + name2_male)
                return JsonResponse({'third':name2_m}, status=200)
            
            elif request.GET.get('btn4'):
                
                name2_female="(ko|mi|ka|na)"
                name2_f = rstr.xeger(name2 + name2_female)
                return JsonResponse({'fourth':name2_f}, status=200)


        return render(request, 'randomname/index.html')
