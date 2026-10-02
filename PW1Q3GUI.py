import streamlit as st

st.title("Cinema Snack Bar")

# Prices
popcorn_price = 8.50
hotdog_price = 7.00
nachos_price = 6.50
drink_price = 5.00

# Input
st.subheader("Choose Your Snacks")

popcorn = st.number_input("Popcorn - RM8.50", 0, step=1)
hotdog = st.number_input("Hotdog - RM7.00", 0, step=1)
nachos = st.number_input("Nachos - RM6.50", 0, step=1)
drink = st.number_input("Soft Drink - RM5.00", 0, step=1)

# Calculate
if st.button("Calculate Bill"):

    total = (popcorn * popcorn_price) + (hotdog * hotdog_price) + \
            (nachos * nachos_price) + (drink * drink_price)


    if total >= 50:
        discount = total * 0.05
    else:
        discount = 0

    final = total - discount

    # Output
    st.subheader("Receipt")
    st.write("Total: RM", round(total, 2))
    st.write("Discount: RM", round(discount, 2))
    st.write("Final Amount: RM", round(final, 2))