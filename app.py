import streamlit as st 

#Text/Title
st.title("어제 먹은 연어는 너무 맛있어서 울었다")
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
- 더이상 무슨 말이 필요?
''')
# error / colorful text
st.success("회색부엉이의 연어손질")
st.info('연어종류 맞추기')
st.warning('연어장 담그기 최적화 안하면 먹지마')
st.error('에러는 무슨 먹고싶은대로 먹기')
st.exception("NameError('name three not defined')")

# get help info about python

st.help(range)

# Writing Text
st.write("한글 잘 먹히나?")
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
    st.text('아직 보여줄것도 없는데 그냥 숨겨봄')