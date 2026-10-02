import streamlit as st

# Cinema package prices
package_price = {
    "Standard": 12.00,
    "VIP": 30.00,
    "Family": 50.00
}

# Customer discounts
discount_rate = {
    "Regular": 0.00,
    "Student": 0.20,
    "Senior": 0.15
}

# Title
st.title("Golden Screen Cinemas Sdn. Bhd.")

st.header("Choose Cinema Package and Customer Type")

# Combo box for Cinema Package
cinema_package = st.selectbox(
    "Cinema Package:",
    ["Standard", "VIP", "Family"]
)

# Combo box for Customer Type
customer_type = st.selectbox(
    "Customer Type:",
    ["Regular", "Student", "Senior"]
)

# Calculate button
if st.button("Calculate Total Payment"):

    # Get package price
    price = package_price[cinema_package]

    # Get discount
    discount = discount_rate[customer_type]

    # Calculate total payment
    total_payment = price - (price * discount)

    # Display result
    st.write(f"Selected Package: {cinema_package}")
    st.write(f"Customer Type: {customer_type}")
    st.write(f"Total Payment: RM{total_payment:.2f}")
