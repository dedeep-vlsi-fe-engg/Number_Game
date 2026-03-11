from django.shortcuts import render
import random

def play(request):
    # Start a new game
    if 'secret' not in request.session:
        request.session['secret'] = random.randint(1, 100)
        request.session['attempts'] = 0

    message = ""
    secret = request.session['secret']

    if request.method == 'POST':
        guess = int(request.POST.get('guess', 0))
        request.session['attempts'] += 1
        attempts = request.session['attempts']

        if guess < secret:
            message = "📉 Too low! Try higher."
        elif guess > secret:
            message = "📈 Too high! Try lower."
        else:
            message = f"🎉 You got it in {attempts} attempts!"
            del request.session['secret']  # reset game

    return render(request, 'game/play.html', {'message': message})