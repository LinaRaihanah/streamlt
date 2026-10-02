import streamlit as st


def calculate_payment(package, customer):

    if package == "Standard":
        price = 12
    elif package == "VIP":
        price = 30
    else:
        price = 50

    if customer == "Student":
        discount = 0.20
    elif customer == "Senior":
        discount = 0.15
    else:
        discount = 0

    total = price - (price * discount)

    return total


def main():

    st.title("Choose Cinema Package and Customer Type")

    package = st.selectbox(
        "Cinema Package:",
        ["Standard", "VIP", "Family"]
    )

    customer = st.selectbox(
        "Customer Type:",
        ["Regular", "Student", "Senior"]
    )

    if st.button("Calculate Total Payment"):

        total = calculate_payment(package, customer)

        st.write("Total Payment: RM", round(total, 2))


main()