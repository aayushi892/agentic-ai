import streamlit as st
from agents.research_agent import research_industry
from agents.usecase_agent import generate_usecases
from agents.dataset_agent import collect_datasets

st.title("Multi-Agent AI Use Case Generator")

company = st.text_input("Enter a Company or Industry Name")
if st.button("Generate Insights"):
    with st.spinner("Researching..."):
        industry_info = research_industry(company)
        usecases = generate_usecases(industry_info)
        datasets = collect_datasets(usecases)
    
    st.subheader("Industry Research")
    st.write(industry_info)
    
    st.subheader("Generated Use Cases")
    for uc in usecases:
        st.markdown(f"- {uc}")
    
    st.subheader("Dataset Resources")
    for ds in datasets:
        st.markdown(f"- [{ds}]({ds})")
