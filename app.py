import streamlit as st

from apputil import *


st.write(
'''
# Week 2: Coins

...
''')

# currently set for integer input
amount = st.number_input("Exercise Input: ", 
                         value=None, 
                         step=1, 
                         format="%d")

if amount is not None:
    st.write(f"There are {ways(amount)} differnet ways to make {amount} cents using only pennies and nickels.")

