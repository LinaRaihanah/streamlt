import streamlit as st

def check_loan(loan, salary):

    if loan < salary * 3:
        return "approved"
    else:
        return "rejected"


def main():

    st.title("Instant Loan")

    st.write("If the loan value is less than 3 times")
    st.write("the salary, the application is approved.")

    loan = st.number_input(
        "Loan value",
        min_value=0,
        step=1000
    )

    salary = st.number_input(
        "Salary value",
        min_value=0,
        step=1000
    )

    if st.button("Calculate"):

        status = check_loan(loan, salary)

        st.write("Loan value:", loan)
        st.write("Salary value:", salary)

        if status == "approved":
            st.success("Your application has been approved")
        else:
            st.error("Your application has not been approved")


main()