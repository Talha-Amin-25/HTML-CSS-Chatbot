import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="HTML & CSS Tutor Bot", page_icon="🤖", layout="centered")

# Title
st.title("🤖 HTML & CSS Tutor Chatbot")
st.caption("Your interactive Web Development Study Assistant")

# Sidebar
st.sidebar.title("📘 What can I ask?")
st.sidebar.write("""
✅ Greetings (hello, how are you, bye)  
✅ HTML & CSS basics  
✅ HTML boilerplate code  
✅ CSS class & id examples  
✅ Small definitions  
✅ Differences  
✅ Ask for graphs like:
- show html tags graph
""")

st.sidebar.write("### 🧪 Example Questions:")
st.sidebar.code("""
hello
html boilerplate
css class example
css id example
difference between class and id
show html tags graph
bye
""")

# Clear chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Simple predefined responses
basic_responses = {
    "hello": "Hi! How can I help?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm doing great, thanks! 😊",
    "bye": "Goodbye! Have a nice day 👋",
}

# Graph function
def show_graph():
    tags = ["div", "p", "a", "img", "table"]
    usage = [40, 30, 15, 10, 5]

    plt.figure()
    plt.bar(tags, usage)
    plt.title("Common HTML Tag Usage")
    plt.xlabel("HTML Tags")
    plt.ylabel("Usage (%)")
    st.pyplot(plt) # type: ignore

# Knowledge base
def get_response(user_msg):
    msg = user_msg.lower().strip()

    # 1) Basic chat
    if msg in basic_responses:
        return basic_responses[msg]

    # 2) HTML / CSS theory
    if "what is html" in msg:
        return "HTML stands for HyperText Markup Language. It is used to create web pages."

    elif "what is css" in msg:
        return "CSS stands for Cascading Style Sheets. It is used to style HTML pages."

    # 3) HTML Boilerplate
    elif "boiler" in msg or "html boiler" in msg:
        return """Here is the basic HTML boilerplate code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>

    <h1>Hello World</h1>

</body>
</html>
```"""

    # 4) Div example
    elif "div example" in msg:
        return """Here is a simple div example:

```html
<div class="box">
  Hello World
</div>
```"""

    # 5) CSS Class example
    elif "class example" in msg:
        return """CSS Class Example:

```html
<style>
.box {
    color: red;
    font-size: 20px;
}
</style>

<div class="box">This is a class example</div>
```"""

    # 6) CSS ID example
    elif "id example" in msg:
        return """CSS ID Example:

```html
<style>
#main {
    color: blue;
    font-size: 22px;
}
</style>

<div id="main">This is an ID example</div>
```"""

    # 7) Difference
    elif "class and id" in msg or "difference between class and id" in msg:
        return "Class can be used multiple times. ID is unique and used only once."

    # 8) Margin vs Padding
    elif "margin and padding" in msg:
        return "Margin is space outside the element. Padding is space inside the element."

    # 9) Graph
    elif ("show" in msg and "graph" in msg) or ("show" in msg and "chart" in msg):
        show_graph()
        return "📊 I have displayed a sample HTML tag usage graph above."

    else:
        return "❌ Sorry, I can answer greetings and HTML & CSS related questions only."

# Input box
user_msg = st.chat_input("Ask something about HTML, CSS, or say Hello...")

if user_msg:
    st.session_state.chat_history.append(("You", user_msg))
    response = get_response(user_msg)
    st.session_state.chat_history.append(("Bot", response))

# Display chat
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")
