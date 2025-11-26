import streamlit as st



st.title("Welcome to Vans Chai Shop ☕👩🏻‍🦰")
st.header("Our special Combos of Chai  ")
col1,col2,col3=st.columns(3)
with col1:
    st.subheader("Masala Chai")
    st.image("https://budleaf.com/wp-content/uploads/2023/06/History-of-Masala-chai.jpg",
             width=150)
    if st.button("Masala Chai"):
        st.success("Your Masala Chai order is taken")
        st.write("Thank you enjoy")

with col2:
     st.subheader("Adrak Chai")
     st.image("https://static.toiimg.com/thumb/msid-27716213,imgsize-20651,width-400,resizemode-4/27716213.jpg",
              width=150)
     if st.button("Adrak Chai"):
        st.success("Your Adark Chai order is taken")
        st.write("Thank you enjoy")

with col3:
     st.subheader("Kesar Chai")
     st.image("https://cdn.shopify.com/s/files/1/0468/6505/5908/files/Health-Benefits-of-Kesar-Chai_480x480_50e3262a-a45d-460c-b781-2e6c689e215f.webp?v=1739170435",
              width=150)
     if st.button("kesar Chai"):
        st.success("Your kesar Chai order is taken")
        st.write("Thank you enjoy")


name=st.sidebar.text_input("Enter your name")


phon=st.sidebar.text_input("Enter your Number",max_chars=11)

if st.sidebar.button("Done"):
    st.sidebar.success(f"Noted {name}.Thank you for choosing us")



with st.expander("Just a quick show how do we brew your fav chai "):
    st.write("""
1. Boil water with tea leaves
2. Add milk and spices according to your taste
3. Serve hot
""")
st.subheader("Do you want anything to munch with chai!!!🍟🥐")



o = {
    'Biscuits':'https://c.ndtvimg.com/2023-02/7e6ta34_biscuit_625x300_01_February_23.jpg?im=FaceCrop,algorithm=dnn,width=620,height=350',
    'mirchi':'https://i0.wp.com/www.chitrasfoodbook.com/wp-content/uploads/2015/03/andhra-mirapakaya-bajji-recipe.jpg?w=1200&ssl=1',
    'Samosa':'https://www.licious.in/blog/wp-content/uploads/2022/08/Shutterstock_1508653862-750x750.jpg',
    'kachori':'https://purendesi.in/wp-content/uploads/2024/03/raj-kachori-recipe.jpg',
    'Vadapav':'https://www.ohmyveg.co.uk/wp-content/uploads/2023/08/Vada-Pav-4-scaled-e1722868617631.jpg',
    'Alu bujiya':'https://www.indianhealthyrecipes.com/wp-content/uploads/2020/09/aloo-bhujia-recipe.jpg'
}

# multiselect options (same keys as dictionary)
bu = st.multiselect(
    "Please select from the below and enjoy",
    list(o.keys())
)

# show selected images
cols = st.columns(3)  # show 3 images per row

for i, item in enumerate(bu):
    with cols[i % 3]:  # wrap after 3 images
        st.image(o[item], width=180)
        st.caption(item)

if st.button("Done"):
    st.success("Your order is successfully received")
    st.write("Njoy!!!!!! and Thankyou")

