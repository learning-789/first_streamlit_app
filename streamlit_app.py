import streamlit
streamlit.title( 'My Mom"s New Healthy Dinner ')

streamlit.header( 'breakfast Menu')
streamlit.text( '🥣Omega 3 & blueberry Oatmeal')
streamlit.text( '🥗Kale ,Spanish & Rocket Smoothie')
streamlit.text( '🐔Hard-boiled free - Range Egg')
streamlit.text( '🍞🥑Avocado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
