import streamlit as st

st.title("Cinema Food Ordering System")

# Tetapkan harga bagi setiap makanan
popcorn_price = 8.50
hotdog_price = 7.00
nachos_price = 6.50
drink_price = 5.00

# Masukkan kuantiti setiap makanan
popcorn = st.number_input("Enter the quantity for Popcorn (RM8.50):", min_value=0, step=1)
hotdog = st.number_input("Enter the quantity for Hotdog (RM7.00):", min_value=0, step=1)
nachos = st.number_input("Enter the quantity for Nachos (RM6.50):", min_value=0, step=1)
drink = st.number_input("Enter the quantity for Soft Drink (RM5.00):", min_value=0, step=1)

# Button
if st.button("Calculate Total"):

    # Kira jumlah harga
    total = (popcorn * popcorn_price) + (hotdog * hotdog_price) + (nachos * nachos_price) + (drink * drink_price)

    # Paparkan jumlah harga
    st.write("Total cost: RM", round(total, 2))

    # Periksa sama ada jumlah mencapai RM50
    if total >= 50:

        # Kira diskaun 5%
        discount = total * 0.05

        # Kira jumlah selepas diskaun
        final_amount = total - discount

        # Paparkan diskaun dan jumlah akhir
        st.write("Discount applied (5%): RM", round(discount, 2))
        st.write("Final amount to pay: RM", round(final_amount, 2))

    else:

        # Tiada diskaun jika jumlah kurang daripada RM50
        st.write("Final amount to pay: RM", round(total, 2))