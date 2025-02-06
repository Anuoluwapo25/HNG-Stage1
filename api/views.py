from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .utils import is_prime, is_perfect, digit_sum, fun_fact, is_armstrong

class ClassifyNum(APIView):
    def get(self, request):
        num = request.GET.get("number")  

        if num is None or num.strip() == "":
            return Response({"number": num, "error": True}, status=400)

        try:
            num = int(num)
        except ValueError:
            return Response({"number": num, "error": True}, status=400)

        properties = []

        if is_armstrong(num):
                properties.append("armstrong")

        properties.append( "odd" if num % 2 == 1 else "even")

        
        is_prime_result = is_prime(num)
        is_perfect_result = is_perfect(num)
        digit_sum_result = digit_sum(num)
        get_fun_fact_result = fun_fact(num)


        return Response({
            "number": num,
            "is_prime": is_prime_result,
            "is_perfect": is_perfect_result,
            "properties": properties, 
            "digit_sum": digit_sum_result,
            "fun_fact": get_fun_fact_result,
        })