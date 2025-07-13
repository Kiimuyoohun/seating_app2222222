import streamlit as st
from random import shuffle

st.title("< 102 교실 랜덤 자리 배치 >")

# 사용자 입력
people = st.number_input("학생 수", min_value=1, value=20)
except_input = st.text_input("제외할 사람 번호들을 쉼표로 구분해서 입력해 주세요 (예: 2,4,6)", "")
hang = st.number_input("행 (가로)", min_value=1, value=4)
yeal = st.number_input("열 (세로)", min_value=1, value=5)

if st.button("START"):
    people_list = list(range(1, people + 1))
    except_people = [int(num.strip()) for num in except_input.split(",") if num.strip().isdigit()]

    for person in except_people:
        if person in people_list:
            people_list.remove(person)
        else:
            st.warning(f"{person}번은 명단에 없거나 이미 제외되었습니다.")

    total_seats = hang * yeal

    if len(people_list) != total_seats:
        st.error(f"⚠️ 남은 인원 수({len(people_list)})와 행×열({hang*yeal})이 일치하지 않습니다.")
    else:
        shuffle(people_list)

        # 자리 배치 2차원 배열 생성
        seat = []
        for i in range(hang):
            start = i * yeal
            end = (i + 1) * yeal
            row = people_list[start:end]
            seat.append(row)

        # 칠판 출력
        st.markdown("### --- 칠판 (교실 앞) ---")
        st.markdown("---")

        # 좌석 시각화 (텍스트 기반)
        for i, row in enumerate(seat):
            row_str = "   ".join([f"🟫 {num:2}" for num in row])
            st.text(row_str)

        st.markdown("---")
        st.success("배치 완료!")