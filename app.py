from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

# Global score (simple approach)
user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global user_score, computer_score

    user_choice = request.json['choice']
    computer_choice = random.choice(choices)

    winner = get_winner(user_choice, computer_choice)

    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    match_result = ""
    game_over = False

    if user_score == 3:
        match_result = "🎉 You won the match!"
        game_over = True
    elif computer_score == 3:
        match_result = "💻 Computer won the match!"
        game_over = True

    return jsonify({
        "user": user_choice,
        "computer": computer_choice,
        "round_result": winner,
        "user_score": user_score,
        "computer_score": computer_score,
        "match_result": match_result,
        "game_over": game_over
    })

@app.route('/reset', methods=['POST'])
def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    return jsonify({"message": "Game reset"})

if __name__ == '__main__':
    app.run(debug=True)