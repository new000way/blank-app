import streamlit as stimport streamlit as st
import pandas as pd
import numpy as np
import time

# --- 앱 설정 및 제목 ---
st.set_page_config(
    page_title="Streamlit 배포 실습 데모",
    page_icon="🚀",
    layout="wide" # 화면을 넓게 사용하도록 설정
)

st.title("🚀 Streamlit 배포 실습 환영 페이지")
st.markdown("### 안녕하세요! 이 앱은 Streamlit Community Cloud를 통해 배포되었습니다.")

# --- 소개 섹션 ---
with st.container():
    st.header("1. 배포 성공 확인 체크리스트")
    col1, col2 = st.columns(2)

    with col1:
        st.info("✅ **코드 소스:** GitHub 저장소를 사용했는지 확인")
        st.success("✅ **독립적인 URL:** 본인 계정의 고유한 `.streamlit.app` 주소를 확인")

    with col2:
        st.warning("⚠️ **실시간 반영:** 이 코드를 GitHub에서 수정하면 1분 내로 앱이 자동 업데이트되는지 확인")
        st.error("❌ **에러 확인:** 만약 앱이 작동하지 않는다면 로그를 확인하고 `requirements.txt` 파일을 점검하세요.")

# --- 데이터 시각화 섹션 ---
st.header("2. 데이터 시각화 및 위젯 테스트")
st.write("간단한 데이터프레임과 인터랙티브 위젯을 테스트합니다.")

# 1. 데이터프레임 표시
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['컬럼 A', '컬럼 B', '컬럼 C']
)
st.dataframe(data, use_container_width=True)

# 2. 라인 차트 표시
st.line_chart(data)

# --- 인터랙티브 위젯 섹션 ---
st.header("3. 사용자 입력 테스트")
st.write("슬라이더와 버튼을 움직여 상호작용을 확인하세요.")

# 슬라이더 위젯
slider_value = st.slider(
    '반복 횟수를 선택하세요:',
    min_value=1,
    max_value=10,
    value=5,
    step=1
)
st.write(f"현재 선택된 반복 횟수: **{slider_value}회**")


# 버튼 위젯 및 상태 업데이트
if st.button('작업 시작 버튼'):
    st.text('작업을 시작합니다...')
    my_bar = st.progress(0)
    status_text = st.empty()

    for i in range(slider_value):
        # 진행 상태 업데이트
        percent_complete = int((i + 1) / slider_value * 100)
        my_bar.progress(percent_complete)
        status_text.text(f"현재 {i+1} / {slider_value} 회 반복 중 ({percent_complete}%)")
        time.sleep(0.1) # 짧은 딜레이

    status_text.success('✅ 모든 작업이 성공적으로 완료되었습니다!')
    st.balloons()

# --- 사이드바 테스트 ---
st.sidebar.title("앱 정보")
st.sidebar.markdown("""
Streamlit 버전 1.0 이상에서 테스트되었습니다.
이 앱은 **파이썬으로 웹 앱을 만드는 것이 얼마나 쉬운지** 보여줍니다.
""")
st.sidebar.info("문의사항은 말해주세요.")

# --- 필수 라이브러리 체크 ---
# 참고: 이 코드가 실행되려면 requirements.txt에 다음이 포함되어야 합니다.
# streamlit
# pandas
# numpy
