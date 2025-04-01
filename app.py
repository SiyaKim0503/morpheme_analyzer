import streamlit as st
from kiwipiepy import Kiwi

st.title("한국어 형태소 분석기 (Kiwi)")
st.write("텍스트 파일을 업로드하면 문장별로 형태소 분석 결과를 보여줍니다.")

kiwi = Kiwi()

uploaded_file = st.file_uploader("텍스트 파일 업로드 (.txt, UTF-8)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    lines = text.splitlines()
    
    result_lines = []
    for line in lines:
        if line.strip() == "":
            continue
        tokens = kiwi.tokenize(line)
        analyzed = " ".join(f"{t.form}/{t.tag}" for t in tokens)
        result_lines.append(analyzed)

    result_text = "\n".join(result_lines)
    
    st.text_area("형태소 분석 결과", result_text, height=400)

    st.download_button("결과 다운로드", result_text, file_name="kiwi_result.txt")
