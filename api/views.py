from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.utils import is_prime, is_perfect, is_armstrong, digit_sum, get_fun_fact


class ClassifyNum(APIView):
    def POST(self, request):
        num = request.GET.get('number')

        if not num or num.isdigit():
             return Response ({
                  "number": "alphabet",
                  "error": True
                }, status=status.HTTP_400_Bad_REQUEST)
        
        num = int(num)
        properties = []

        if is_armstrong(num):
                properties.append("armstrong")

        properties.append( "odd" if num % 2 == 1 else "even")
    

        return Response({
                "number": num,
                "is_prime": is_prime,
                "is_perfect": is_perfect,
                "properties": is_armstrong,
                "digit_sum": digit_sum,
                "fun_fact": get_fun_fact
        })