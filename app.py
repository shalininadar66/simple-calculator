import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.title("🧮 Simple Calculator Web App")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operator = st.selectbox(
    "Select operator",
    ["+", "-", "*", "/"]
)

# Calculate button
if st.button("Calculate"):

    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                st.error("Cannot divide by zero.")
            else:
                result = num1 / num2

        if operator != "/" or num2 != 0:
            st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
