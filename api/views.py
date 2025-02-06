from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.utils import is_prime, is_perfect, is_armstrong, digit_sum, get_fun_fact


class ClassifyNum(APIView):
    def get(self, request):
        num = request.GET.get('number')

        if not num or not num.isdigit():
             return Response ({
                  "number": "alphabet",
                  "error": True
                }, status=400)
        
        num = int(num)
        properties = []

        if is_armstrong(num):
                properties.append("armstrong")

        properties.append( "odd" if num % 2 == 1 else "even")
    

        return Response({
                "number": num,
                "is_prime": is_prime(num),
                "is_perfect": is_perfect(num),
                "properties": properties,
                "digit_sum": digit_sum(num),
                "fun_fact": get_fun_fact(num)
        })