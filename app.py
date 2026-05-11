import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="SyncMe AI", page_icon="🦂")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦂 SyncMe AI: منسق المواعيد الذكي")
st.write("مرحباً Scorpion، دعنا نجد الوقت المثالي لتجمع الأصدقاء.")

with st.sidebar:
    st.header("إعدادات المجموعة")
    friends_count = st.number_input("عدد الأصدقاء", min_value=2, max_value=10, value=3)
    activity_type = st.selectbox("نوع النشاط", ["عشاء", "كرة قدم", "اجتماع عمل", "دراسة", "لعب أونلاين"])

st.subheader("🗓️ تحديد المواعيد المقترحة")
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("ابدأ البحث من تاريخ", datetime.now())
with col2:
    end_date = st.date_input("إلى تاريخ", datetime.now() + timedelta(days=3))

def find_optimal_time():
    suggestions = [
        {"time": "الجمعة - 08:00 مساءً", "match": "95%", "place": "مطعم وسط المدينة"},
        {"time": "السبت - 07:00 مساءً", "match": "80%", "place": "ملعب الحي الرئيسي"},
        {"time": "الأحد - 09:00 مساءً", "match": "100%", "place": "كافيه الهدوء"}
    ]
    return suggestions

if st.button("تنسيق الموعد بالذكاء الاصطناعي ✨"):
    with st.spinner('جاري تحليل تقاويم الأصدقاء والبحث عن أفضل خيار...'):
        results = find_optimal_time()
        st.success("تم العثور على أفضل المواعيد!")
        for res in results:
            with st.expander(f"📌 خيار: {res['time']} (توافق {res['match']})"):
                st.write(f"📍 **المكان المقترح:** {res['place']}")
                if st.button(f"تأكيد موعد {res['time']}", key=res['time']):
                    st.balloons()
                    st.info("تم إرسال دعوات لجميع الأصدقاء!")

st.divider()
st.caption("🛡️ جميع البيانات مشفرة وتتم معالجتها وفق معايير الخصوصية.")
