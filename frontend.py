import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://localhost:5000"


def main():
    st.title("HealthTrendAnalyzer")

    # ⚠️ Mandatory disclaimer
    st.warning(
        "This application provides public health trend summaries "
        "for educational purposes only and is not medical advice."
    )

    # Initialize session state
    if "topics" not in st.session_state:
        st.session_state.topics = []

    # Sidebar
    with st.sidebar:
        st.header("Data Sources")
        source_type = st.selectbox(
            "Select source type",
            options=["news", "both"],
            format_func=lambda x: x.capitalize()
        )

    # Topic input
    st.markdown("### Topic Selection")

    col1, col2 = st.columns([4, 1])

    with col1:
        new_topic = st.text_input(
            "Add a public health topic",
            placeholder="Flu Outbreaks"
        )

    with col2:
        if st.button("Add +", disabled=not new_topic.strip()):
            st.session_state.topics.append(new_topic.strip())
            st.rerun()

    # Show selected topics
    if st.session_state.topics:
        st.markdown("### Selected Topics")

        for i, topic in enumerate(st.session_state.topics):
            colA, colB = st.columns([5, 1])
            colA.write(f"{i + 1}. {topic}")

            if colB.button("❌", key=f"remove_{i}"):
                del st.session_state.topics[i]
                st.rerun()

    st.divider()

    # Generate summary
    if st.button("Generate Public Health Summary", disabled=not st.session_state.topics):
        with st.spinner("Analyzing public health news..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate-news-summary",
                    json={
                        "topics": st.session_state.topics,
                        "source_type": source_type
                    },
                    timeout=15
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("Summary generated successfully")

                    for topic, summary in data["summaries"].items():
                        st.markdown(f"## 🩺 {topic}")
                        st.markdown(summary.replace("\n", "  \n"))
                        # -------- Trend Visualization --------
                    if "counts" in data:
                        st.markdown("## 📊 Topic Trend Overview")

                        df = pd.DataFrame(
                            list(data["counts"].items()),
                            columns=["Topic", "Article Count"]
                        )

                        st.bar_chart(df.set_index("Topic"))


                else:
                    st.error(f"Backend error: {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"Cannot connect to backend: {e}")


if __name__ == "__main__":
    main()
