from django.http import JsonResponse
from django.shortcuts import render
from chatbot.bot import get_basic_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ask_bot(request):
    if request.method == "POST":
        question = request.POST.get('question', 'Tell me a short Joke.')
        response = get_basic_response(question)
        return JsonResponse({'question': question, 'answer': response})

    return JsonResponse({'error': 'Please use POST method'})
