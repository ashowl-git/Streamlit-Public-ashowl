import streamlit as st 

#Text/Title
st.title("이것이 타이틀?")
st.header("이것은 헤더이다")
st.subheader("이것은 서브 헤더이다")
st.text('이것은 그냥 텍스트이다')

# martkdown
st.markdown(
'''
# 이것은
## 마크
### 다운
- 입니다 
''')
# error / colorful text
st.success("Successful")
st.info('Infomation')
st.warning('This is a warning')
st.error('This is an error Danger')
st.exception("NameError('name three not defined')")

# get help info about python

st.help(range)

# Writing Text
st.write("Text with write")
st.write(range(10))


# Images
from PIL import Image 
img = Image.open("img100.jpg")
st.image(img)
st.image(img, width=300, caption="이미지 각주")


# Videos
# vid_file = open('example.mp4', 'rb').read()
# st.video(vid_file)

# Audio
# audio_file = open('example.mp3', 'rb').read()
# st.audio(audio_file, format='audio/mp3')

#Widget
# Checkbox
if st.checkbox('show/Hide'):
    st.text('Showing or Hiding Widget')