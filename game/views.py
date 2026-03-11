import random
from django.shortcuts import render


def play(request):
    # Start a new game: pick a random number and store in session
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 100)
        request.session['attempts'] = 0

    message = ''
    won = False

    if request.method == 'POST':
        try:
            guess = int(request.POST.get('guess', 0))
            secret = request.session['secret_number']
            request.session['attempts'] = request.session.get('attempts', 0) + 1
            attempts = request.session['attempts']

            if guess < 1 or guess > 100:
                message = '⚠️ Please enter a number between 1 and 100!'
            elif guess < secret:
                message = f'📉 Too low! Try a higher number. (Attempt #{attempts})'
            elif guess > secret:
                message = f'📈 Too high! Try a lower number. (Attempt #{attempts})'
            else:
                message = f'🎉 CORRECT! You guessed {secret} in {attempts} attempt{"s" if attempts > 1 else ""}! Amazing!'
                won = True
                # Reset for next game
                del request.session['secret_number']
                del request.session['attempts']
        except (ValueError, TypeError):
            message = '⚠️ Please enter a valid number!'

    return render(request, 'game/play.html', {'message': message, 'won': won})
