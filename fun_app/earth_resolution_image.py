import streamlit as st
import base64
from PIL import Image

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

st.markdown("<h1 style='text-align: center; color: blue;'>PICTURE OF THE WORLD</h1>", unsafe_allow_html=True)

#Slider
label = ':red[RESOLUTION]'
minValue = 0
maxValue = 4
value = st.slider(label, minValue, maxValue, 1)
if value == 0:
    st.markdown("<h2 style='text-align: center; color: red;'>Slide to enhance the resolution</h2>", unsafe_allow_html=True)
elif value == 1:
    st.markdown("<h2 style='text-align: left; color: red;'>244Hz</h2>", unsafe_allow_html=True)
    img = Image.open("fun_app/low-resolution.jpg")
    st.image(img,use_column_width=True )
elif value == 2:
    st.markdown("<h2 style='text-align: left; color: red;'>480Hz</h2>", unsafe_allow_html=True)
    img = Image.open("fun_app/medium_resolution.jpg")
    st.image(img)
elif value == 3:
    st.markdown("<h2 style='text-align: left; color: red;'>720Hz</h2>", unsafe_allow_html=True)
    img = Image.open("fun_app/near_high_resolution.jpg")
    st.image(img)
else:
    st.markdown("<h2 style='text-align: left; color: red;'>1080Hz</h2>", unsafe_allow_html=True)
    set_png_as_page_bg("fun_app/background.jpg")
    img = Image.open("fun_app/high_resolution.jpg")
    st.image(img)
