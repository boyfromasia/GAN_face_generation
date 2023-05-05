import streamlit as st
from PIL import Image
import os
import random

network_pkl = "network-snapshot-000240.pkl"
truncation_psi = None


def render_init():
    global truncation_psi, rotate
    st.title('Anime Face Generation')
    truncation_psi = st.slider("Truncation PSI. How much the faces will be different?",
                               min_value=0.0, max_value=1.0)
    st.button("Generate Faces", on_click=get_images)


def get_images():
    global truncation_psi
    seeds = [str(random.randrange(10**7)) for _ in range(6)]
    cmd = f"python stylegan3\gen_images.py --outdir=out --trunc={truncation_psi}" \
          f" --seeds={','.join(seeds)} --network=network-snapshot-000240.pkl"
    os.system(cmd)
    st.balloons()

    st.session_state['images'] = seeds


def render_images():
    if st.session_state['images'] != []:
        st.title('Generated Anime Faces')

    size = 117
    st.image([Image.open(f"out\seed{seed}.png").resize((size, size)) for seed in st.session_state['images']])


if "images" not in st.session_state:
    st.session_state['images'] = []
    render_init()
else:
    render_init()
    render_images()

