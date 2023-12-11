import streamlit as st
import pandas as pd

# Text input
name = st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}')

# Number input
number = st.number_input('Enter a number: ', min_value=1, max_value=99, step=1)
st.write(f'The current number is {number}')

st.divider()

# button
clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:' * 3)

st.divider()

# checkbox
agree = st.checkbox('I agree')
if agree:
    'Great, you agreed!'

checked = st.checkbox('Continue', value=True)
if checked:
    ':+1:' * 5

df = pd.DataFrame({
    "name": ["John", "Mary", "Peter", "Jeff", "Bill"],
    "age": [23, 78, 22, 19, 45],
})

if st.checkbox('Show data'):
    df

st.divider()

# radio
pets = ['cat', 'dog', 'snake', 'horse']
pet = st.radio('Favourite pet', pets, index=3, key='your_pet')
st.write(f'Your favourite pet: {pet}')
st.write(f'your favourite pet: {st.session_state.your_pet * 3}')

st.divider()

# select
cities = ['London', 'New York', 'Paris', 'Tokyo', 'Berlin', 'Dubai', 'Singapore', 'Hong Kong', 'Jalingo']
city = st.selectbox('Your city', cities, index=2)
st.write(f'You live in {city}')

st.divider()

# slider
age = st.slider('How old are you?', min_value=1, max_value=99, value=5)
st.write(f'I am {age} years old')

st.divider()

# uploader
uploaded_file = st.file_uploader('Upload a file:', type=['txt', 'csv', 'xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)

# camera input
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)

st.image('https://static.streamlit.io/examples/owl.jpg')
