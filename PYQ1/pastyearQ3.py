import streamlit as st

st.title("Instant Loan")

st.write(
    "If the loan value is less than 3 times "
    "the salary, the application is approved."
)

loan_value = st.number_input(
    "Loan value",
    min_value=0,
    step=1000
)

salary_value = st.number_input(
    "Salary value",
    min_value=0,
    step=500
)

if st.button("Calculate"):
    if loan_value < 3 * salary_value:
        st.write(f"Loan value: {loan_value}")
        st.write(f"Salary value: {salary_value}")
        st.success("Your application has been approved")
    else:
        st.write(f"Loan value: {loan_value}")
        st.write(f"Salary value: {salary_value}")
        st.error("Your application has not been approved")
