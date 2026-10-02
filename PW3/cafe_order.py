import streamlit as st

def main():
    #paparkan tajuk 
    st.title("Cafe Order Calculator")
    #bina text box untuk user masukkan name customer
    customer_name = st.text_input("Customer Name")
    #selectbox untuk bina dropdown list sebagai pilihan
    food_item = st.selectbox(
        "Food Item",
        ["Nasi Lemak", "Fried Rice", "Chicken Burger", "Spaghetti"]
    )
    #bina text box untuk masukkan quantity
    quantity = st.text_input("Quantity")
    #bina text box untuk user masukkan harga
    price = st.text_input("Price Per Item (RM)")

    if st.button("Calculate"):
        #start exeception handling
        try:
            # convert quantity to integer and price to float
            quantity = int(quantity)
            price = float(price)

            # VALIDATION
            #Check kalau name customer kosong maka akan papar error
            if customer_name == "":
                st.warning("Please enter customer name.")
            #check kalau quantity kurang dari 0 maka akan papar error
            elif quantity <= 0:
                st.error("Quantity must be greater than 0.")
            #check kalau harga kurang dari 0 makan akan papar error
            elif price <= 0:
                st.error("Price must be greater than 0.")
            #jika semua input di atas valid maka
            else:
                #darapkan kuantiti dengan harga
                subtotal = quantity * price
                #kalau lebih rm 50 customer akan dapat discount
                if subtotal >= 50:
                    discount = subtotal * 0.10
                else:
                #jika tidak discount 0 sahaja
                    discount = 0
                #harga final lepas discount
                final_amount = subtotal - discount

                #subjeader sebagai smaller heading
                st.subheader("Order Summary")
                #paparkan output 
                st.write("Customer Name:", customer_name)
                st.write("Food Item:", food_item)
                st.write("Quantity:", quantity)
                st.write("Subtotal: RM", round(subtotal, 2))
                st.write("Discount: RM", round(discount, 2))
                st.write("Final Amount: RM", round(final_amount, 2))
        #akan error kalau input tak boleh convert ke number
        except ValueError:
            #akan muncul error mesej untuk isi invalid input
            st.error("Invalid input. Please enter numbers for quantity and price.")

main()