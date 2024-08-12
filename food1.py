import streamlit as st

# Initialize lists and total
foods = []
prices = []
total = 0

# Title of the app
st.title("Food Purchase Tracker")

# Input for food item
food = st.text_input("Enter a food item (leave blank to stop adding items):")

if food:
    # Input for the price of the food item
    price = st.number_input(f"Enter the price of {food}: $", min_value=0.0, format="%.2f")

    # Add food and price to lists if price is entered
    if st.button("Add Item"):
        if price > 0:
            foods.append(food)
            prices.append(price)
            st.success(f"Added {food} with price ${price:.2f} to the cart.")
        else:
            st.error("Price must be greater than 0.")
else:
    if st.button("Calculate Total"):
        if foods:
            total = sum(prices)
            st.subheader("----- YOUR CART -----")
            for i in range(len(foods)):
                st.write(f"{foods[i]}: ${prices[i]:.2f}")
            st.write(f"**Total:** ${total:.2f}")
        else:
            st.warning("No items to calculate.")
