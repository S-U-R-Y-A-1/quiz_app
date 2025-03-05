import streamlit as st
import time
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")
# Define quiz questions in a dictionary
questions = [
    {"question": "To unlock this, use the four letters below and create a seven-letter word: 'UMNI'. \nWin Amount : $1000", "answer": "[77, 73, 78, 73, 77, 85, 77]"},
    {"question": "A robber left a clue: HFXM NX KZQQ GQTTI\nDecipher the shift cipher where the shift is determined by the fifth preceding letter.\nWin Amount : $1000", "answer": "[67, 65, 83, 72, 32, 73, 83, 32, 70, 85, 76, 76, 32, 79, 70, 32, 66, 76, 79, 79, 68]"},
    {"question": "Convert 'MAGADHA BANK' to ASCII values. (Note: Consider capital letter values and neglect the space)\nWin Amount : $1200", "answer": "['M', 'A', 'G', 'A', 'D', 'H', 'A', 'B', 'A', 'N', 'K']"},
    {"question": "Find the cube's side length given a volume of 1728 cubic meters.\nWin Amount : $2300", "answer": "[49,50]"},
    {"question": "The passcode is a 5-character alphanumeric sequence. The first two are the initials of a famous cricketer with a biopic. The last three digits have a sum of 5, with the first and last being consecutive.\nWin Amount : $2500", "answer": "[77, 83, 50, 48, 51]"},
    {"question": "Convert the three-digit number from the previous question into binary.\nWin Amount : $2800", "answer": "203"},
    {"question": "To unlock this locker, Solve this riddle:\n\nShapeless, yet I carve through stone, \n\nDancing swiftly, yet never alone. \n\nI follow paths both old and new, \n\nFrom mountain peaks to oceans blue.\n\nTurn me around, and you shall find,\n\n A beast that hunts, fierce and unkind.\n\nWhat am I?\nWin Amount : $3000", "answer": "[70, 76, 79, 87]"},
    {"question": "Use the bubble sort algorithm to sort: 5 4 2 3 1. Enter the number of swaps needed. \nWin Amount : $3200", "answer": "[57]"},
    {"question": "To unlock this, solve the equation where each letter represents a unique digit (0-9): B + A + N + K = 10\nM + O + N + E + Y = 15\nFind the correct digits for BANKMONEY to unlock.\nWin Amount : $3500", "answer": ""},
    {"question": "Unlock the locker by removing the screws based on directional hints: ↓→↑↑←↓←↑→↑←↓↓←↑←. Organize them into four batches.\nWin Amount : $4500", "answer": "1 up down right left, 2 left left right down"},
    {"question": "A six-digit balance has a digit sum of 36. The first and last digits are the same, the middle two are identical, and the second and fifth digits are twice the middle. The sum of the second and third is equal to the first. Find the number.\nWin Amount : $5000", "answer": "[57, 51, 54, 54, 51, 57]"},
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
time_limit = 20  # seconds

# Function to validate answers using Groq API
def validate_answer(index, user_answer):
    correct_answer = questions[index]["answer"]

    # If answer is already known, compare directly
    if user_answer.strip().lower() == correct_answer.lower():
        return "Correct ✅"

    # Otherwise, send to Groq API for validation
    validation_prompt = f"""
    Given the question: "{questions[index]['question']}"
    The correct answer is: "{correct_answer}"
    The user answered: "{user_answer}"
    If the correct answer is null check that the user answer satisfies the logic for the question asked and evaluate it.
    Respond only with "Correct ✅" or "Incorrect ❌".
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

# Display the quiz
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    
    st.write(f"### Question {st.session_state.current_question + 1}:")
    st.write(q["question"])  # Display the current question

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

    countdown_placeholder.write(f"⏳ Time left: **{st.session_state.remaining_time} seconds**")

    # Refresh the timer every second
    if st.session_state.remaining_time > 0:
        time.sleep(1)
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

else:
    st.write("### Quiz Completed! 🎉")
    st.write("Your Answers:", st.session_state.user_answers)
    st.write("### Validation Results:")
    for i, result in enumerate(st.session_state.validation_results):
        st.write(f"Question {i+1}: {result}")
