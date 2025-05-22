from flask import Flask, render_template
import random

app = Flask(__name__)

# List of motivational quotes in Hinglish
quotes = [
    "Kabhi kabhi jeetne ke liye, kuch haarna padta hai. - Sometimes to win, you need to lose something.",
    "Mehnat itni khamoshi se karo ki success shor macha de. - Work so silently that your success makes all the noise.",
    "Apne sapno ko itna bada banao ki log hans na sake, sirf dekhte reh jaye. - Make your dreams so big that people can't laugh, they can only stare.",
    "Life me kabhi bhi give up mat karo, kyunki aaj nahi to kal, kal nahi to parso success zaroor milega. - Never give up in life, because if not today then tomorrow, if not tomorrow then the day after, success will surely come.",
    "Mushkil waqt, mushkil insaan, aur mushkil raaste, ye sab milkar hi toh strong banate hai. - Difficult times, difficult people, and difficult paths, all these together make you strong.",
    "Haar kar jeetne wale ko hi baazigar kehte hain. - The one who wins after losing is called a champion.",
    "Koshish karne walon ki kabhi haar nahi hoti. - Those who try never lose.",
    "Safalta ek journey hai, destination nahi. - Success is a journey, not a destination.",
    "Apni khushiyan khud create karo, doosron ke decisions pe depend mat karo. - Create your own happiness, don't depend on others' decisions.",
    "Zindagi me kuch bhi impossible nahi hai, bas himmat chahiye. - Nothing is impossible in life, you just need courage."
]

@app.route('/')
def home():
    # Select a random quote
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')