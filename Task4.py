from flask import Flask, render_template, request
import string

app = Flask(__name__)

# Task 1
def count_consonants(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

# Task 2
def find_smallest(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Task 3
def validate_password(password):
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)
    return has_upper and has_lower and has_digit and has_special


@app.route("/", methods=["GET", "POST"])
def index():
    result1 = result2 = result3 = None

    if request.method == "POST":
        if "text_input" in request.form:
            text = request.form["text_input"]
            result1 = f"Number of consonants: {count_consonants(text)}"

        if "numbers_input" in request.form:
            try:
                numbers = list(map(int, request.form["numbers_input"].split(",")))
                result2 = f"The smallest number is: {find_smallest(numbers)}"
            except:
                result2 = "Invalid input. Please enter numbers separated by commas."

        if "password_input" in request.form:
            password = request.form["password_input"]
            if validate_password(password):
                result3 = "Strong password. Account created."
            else:
                result3 = "Invalid password. Too weak."

    return render_template("index.html", result1=result1, result2=result2, result3=result3)


if __name__ == "__main__":
    app.run(debug=True)


[
    {
        "type": "command",
        "details": {
            "key": "python.execInTerminal"
        }
    }
]