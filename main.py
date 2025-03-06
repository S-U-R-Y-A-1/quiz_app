import streamlit as st
import time
from groq import Groq
import base64

import requests

def get_gif_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode()
    else:
        st.error("Failed to load GIF from GitHub.")
        return None

# GitHub raw URL of the GIF
gif_url = "https://raw.githubusercontent.com/S-U-R-Y-A-1/quiz_app/main/anode-avaxnode.gif"
gif_base64 = get_gif_base64(gif_url)

# Use session state to track first load
if "show_gif" not in st.session_state:
    st.session_state.show_gif = True  # Show GIF initially
    st.session_state.start_time = time.time()  # Store the start time

# Display GIF only if it was successfully loaded
if gif_base64 and st.session_state.show_gif and (time.time() - st.session_state.start_time < 7):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/gif;base64,{gif_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}

        .title-box {{
            position: absolute;
            width: 600px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #FFFFFF; /* Solid white background */
            color: black;
            padding: 30px 50px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            margin-top: 200px;
            border: 2px solid black;
            opacity: 0;  /* Initially hidden */
            animation: fadeIn 1s ease-in-out forwards;
            animation-delay: 4s;  /* Delay title appearance by 3 seconds */
        }}
        </style>

        <div class="title-box">
            <h1 style="color: black;">WELCOME TO THE VAULT OF FORTUNE</h1>
            <p>Let the AI Heist Begin!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Wait for 7 seconds
    time.sleep(7)

    # Refresh the page
    st.session_state.show_gif = False
    st.rerun()


else:
# Set page config
    st.set_page_config(page_title="Quiz Game", page_icon="🎯", layout="wide")

# ✅ Load the uploaded image
    image_url = "https://raw.githubusercontent.com/S-U-R-Y-A-1/quiz_app/main/background.jpg"

# ✅ Function to fetch image from URL and convert to Base64
    def get_base64_from_url(image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
        else:
            st.error("Failed to load background image from GitHub.")
            return None

# ✅ Convert image to Base64
    image_base64 = get_base64_from_url(image_url)

# ✅ Custom CSS for Full-Page Background    
    background_css = f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
    box_css = """
<style>
    .centered-box {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: 0px;
    margin-top: 100px;
    background-color: white; /* Fully solid white */
    border: 2px solid black;
    transform: translate(-50%, -50%);
    padding: 40px 60px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    width: 50%;
    
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: normal;
    overflow: hidden;
}



    
    .centered-box1 {
        position: absolute;
        width: 300px;
        height: 250px;
        top: 50%;
        left: 50%;
        margin-left: 0px;
        margin-top: 300px;
        background-color: white; /* Changed to solid white */
    border: 2px solid black; /* Added black border */

        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.7);
        color:black;
        padding: 40px 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        width: 50%;
         word-wrap: break-word; /* Ensures long words wrap */
    overflow-wrap: break-word; /* Ensures text doesn't overflow */
    white-space: normal; /* Allows text wrapping */
    overflow: hidden; /* Hides any overflowing content */
    }
    .centered-box2 {
        position: absolute;
        width: 300px;
        height: 200px;
        top: 50%;
        left: 50%;
        margin-left: 0px;
        margin-top: 450px;
        background-color: white; /* Changed to solid white */
    border: 2px solid black; /* Added black border */

        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.2);
        padding: 40px 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        width: 50%;
    }
    
    

    .timer {
        font-size: 20px;
        font-weight: bold;
        color: #FFD700;
    }
    .next-btn {
        background-color: #FFD700 !important;
        color: black !important;
        font-size: 18px !important;
        border-radius: 5px !important;
    }
</style>
"""

    st.markdown(box_css, unsafe_allow_html=True)  # Open Glassmorphic Box
    

# ✅ UI Content



# Initialize Groq client
    client = Groq(api_key="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")
# Define quiz questions in a dictionary
    questions = [
    {"question": "To unlock this, use the four letters below and create a seven-letter word: 'UMNI'. \n\nWin Amount : $1000", "answer": [77, 73, 78, 73, 77, 85, 77],"amount":1000},
    {"question": "A robber left a clue: HFXM NX KZQQ GQTTI\nDecipher the shift cipher where the shift is determined by the fifth preceding letter. (eg: H -> C)\n\nWin Amount : $1000", "answer": [67, 65, 83, 72, 32, 73, 83, 32, 70, 85, 76, 76, 32, 79, 70, 32, 66, 76, 79, 79, 68],"amount":1000},
    {"question": "To unlock this locker convert the bank name 'MAGADHA BANK' to ASCII values. (Note: Consider only the values of capital letters and neglect the space)\n\nWin Amount : $1200", "answer": ['M', 'A', 'G', 'A', 'D', 'H', 'A', 'B', 'A', 'N', 'K'],"amount":1200},
    {"question": "Create a bomb to break this cube shaped locker whose volume is given by 1728 cubic meters. Now you have to give the measure of the locker's side.\n\nWin Amount : $2300", "answer": [49,50],"amount":2300},
    {"question": "The passcode is a 5-character alphanumeric sequence. The first two are the initials of a famous cricketer with a biopic. The last three digits have a sum of 5, with the first and last being consecutive.\n\nWin Amount : $2500", "answer": [77, 83, 50, 48, 51],"amount":2500},
    {"question": "To break this locker convert the three-digit number from the previous question into binary.\n\nWin Amount : $2800", "answer": 203,"amount":2800},
    {"question": "To unlock this locker, Solve this riddle:\nShapeless, yet I carve through stone, \nDancing swiftly, yet never alone. \nI follow paths both old and new, \nFrom mountain peaks to oceans blue.\nTurn me around, and you shall find,\n A beast that hunts, fierce and unkind.\nWhat am I?\n\nWin Amount : $3000", "answer": [70, 76, 79, 87],"amount":3000},
    {"question": "Use the bubble sort algorithm to sort: 5 4 2 3 1. Enter the number of swaps needed. \n\nWin Amount : $3200", "answer": [57],"amount":3200},
    {"question": "To unlock the vault, you need a five-letter word.\nIt is something that everyone expects a lot in a MASS HERO MOVIE\nIt contains the first 3 letters as acronym for a specific health dept.\nThe first letter is the same as the last letter of EYE and last letter is the last letter of the word SPY.\nThe word contextually speaks about allowing.\n\nWin Amount : $3500", "answer": [69, 78, 84, 82, 89],"amount":3500},
    {"question": "Solve the riddle to unlock the locker:\nI come from notes, both big and small, Add them up, you will find it all.\n Take two notes of 500, bold and grand,\n Then add five of 200, just as planned.  Drop in four of 100, crisp and neat, Now tell me, what sum do you meet?  The color you seek, bold and bright, Is on the note that held this height!\n\nWin Amount : $4500", "answer": [77, 65, 71, 69, 78, 84, 65],"amount":4500},
    {"question": "A six-digit balance has a digit sum of 36. The first and last digits are the same, the middle two are identical, and the second and fifth digits are twice the middle. The sum of the second and third is equal to the first. Find the number.\n\nWin Amount : $5000", "answer": [57, 51, 54, 54, 51, 57],"amount":5000},
]

# Initialize session state variables
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []
    if "validation_results" not in st.session_state:
        st.session_state.validation_results = []
    if "timer_running" not in st.session_state:
        st.session_state.timer_running = False
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    if "remaining_time" not in st.session_state:
        st.session_state.remaining_time = 10  # Set initial timer

# Time limit per question
    time_limit = 180  # seconds

# Function to validate answers using Groq API
    def validate_answer(index, user_answer):
        correct_answer = questions[index]["answer"]
        ans = ""
        if index == 2:
            for i in correct_answer:
                ans += str(ord(i))
        elif index == 5:
            ans = str(bin(correct_answer)[2:])
        else:
            for i in correct_answer:
                ans += chr(int(i))
                
        correct_answer = ans
    # If answer is already known, compare directly
        if user_answer.strip().lower() == correct_answer.lower():
            return "Correct"

    # Otherwise, send to Groq API for validation
        validation_prompt = """
        Given the question: "{questions[index]['question']}"
        The correct answer is: "{correct_answer}"
        The user answered: "{user_answer}"
        Check whether the correct answer is presented in the user answer.
        Respond only with "Correct" or "Incorrect".
        """

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": validation_prompt}],
            temperature=0,
            max_completion_tokens=20,
            top_p=1,
            stream=False,
        )

        result = completion.choices[0].message.content.strip()
        return result  # Either 'Correct ✅' or 'Incorrect ❌'
    # ✅ Custom CSS to position text input at the bottom
    input_css = """
<style>
    .input-container {
        position: absolute;
        bottom: 15%;  /* Adjust this value to move it up/down */
        left: 50%;
        margin-left: 0px;
        margin-top: 150px;
        transform: translateX(-50%);
        background: rgba(255, 255, 255, 0.2); /* Glassmorphic effect */
        padding: 10px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        width: 50%;
        z-index: 100;  /* Ensures it stays on top */
    }
    
    
</style>
"""

# Display the quiz
    if st.session_state.current_question < len(questions):
        
        q = questions[st.session_state.current_question]

    
        st.markdown(
    f'<div class="centered-box">'
    f'<h2 style="color: black; font-weight: bold;">Question {st.session_state.current_question + 1}:</h2>'
    f'</div>',
    unsafe_allow_html=True
        )
        st.markdown(f'<div class="centered-box1"><p style="color: black; font-weight: bold;">{q["question"]}</p></div>', unsafe_allow_html=True)
        st.markdown(input_css, unsafe_allow_html=True)

# ✅ Wrap st.text_input inside a div positioned at the bottom
        st.markdown("<div style='margin-top: 375px;'></div>", unsafe_allow_html=True)  # Adjust margin as needed

    # User input box
        user_answer = st.text_input("Your Answer:", key=f"answer_{st.session_state.current_question}")

    # Countdown Timer Display
        countdown_placeholder = st.empty()

    # Timer logic
        if not st.session_state.timer_running:
            st.session_state.start_time = time.time()
            st.session_state.remaining_time = time_limit
            st.session_state.timer_running = True

        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.remaining_time = max(0, int(time_limit - elapsed_time))

        countdown_placeholder.write(f"⏳ Time left: *{st.session_state.remaining_time} seconds*")

    # Refresh the timer every second
        if st.session_state.remaining_time > 0:
            time.sleep(10)
            st.rerun()  # ✅ Fixed: Uses st.rerun() instead of deprecated st.experimental_rerun()

    # Auto-move to next question when timer runs out
        if st.session_state.remaining_time == 0:
            st.session_state.user_answers.append(user_answer if user_answer else "No answer")
            validation_result = validate_answer(st.session_state.current_question, user_answer)
            st.session_state.validation_results.append(validation_result)
            st.session_state.current_question += 1
            st.session_state.timer_running = False  # Reset timer for next question
            st.session_state.remaining_time = time_limit  # Reset timer for next question
            st.rerun()  # ✅ Fixed: Uses st.rerun()

    # Manual "Next" button
        if st.button("Next") and user_answer:
            st.session_state.user_answers.append(user_answer)
            validation_result = validate_answer(st.session_state.current_question, user_answer)
            st.session_state.validation_results.append(validation_result)
            st.session_state.current_question += 1
            st.session_state.timer_running = False  # Reset timer for next question
            st.session_state.remaining_time = time_limit  # Reset timer for next question
            st.rerun()  # ✅ Fixed: Uses st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


    else:
        st.write("### Quiz Completed! 🎉")
        st.write("Your Answers:", st.session_state.user_answers)
        st.write("### Validation Results:")
        points = 0
        for i, result in enumerate(st.session_state.validation_results):
            if result == "Correct":
                points += questions[i]["amount"] 
            st.write(f"Question {i+1}: {result}")
        st.write(f"Points : ${points}")
