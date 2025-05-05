import streamlit as st
from data.quizzes import video_resources, pdf_resources
from data.content import comprehensive_glossary
from datetime import datetime
from utils import add_points

def show():
    """Display learning resources including videos, PDFs, and glossary"""
    
    st.title("Learning Resources")
    st.write("Access additional learning materials to deepen your understanding of financial concepts.")
    
    # Create tabs for different resource types
    resource_tabs = st.tabs(["Videos", "Comprehensive Glossary"])
    
    # Videos tab
    with resource_tabs[0]:
        st.header("Video Tutorials")
        st.write("Watch these video tutorials to enhance your learning experience.")
        
        # Create an expander for each module
        modules = ["Insurance", "Equity", "PMS & AIF", "Stocks", "Bonds"]
        
        for module in modules:
            with st.expander(f"{module} Videos"):
                if module in video_resources:
                    for video in video_resources[module]:
                        st.markdown(f"* [{video['title']}]({video['url']})")
                else:
                    st.write("No videos available for this module yet.")
    
    # Glossary tab
    with resource_tabs[1]:
        st.header("Finance Glossary")
        st.write("A comprehensive glossary of financial terms used across all modules.")
        
        # Add a search box for glossary
        search_term = st.text_input("Search for a term", "")
        
        # Display glossary
        if search_term:
            # Filter glossary based on search term
            filtered_terms = [term for term in comprehensive_glossary 
                             if search_term.lower() in term["term"].lower() or 
                                search_term.lower() in term["definition"].lower()]
            
            if filtered_terms:
                for term in filtered_terms:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
            else:
                st.write("No matching terms found.")
        else:
            # Display glossary in 3 columns
            col1, col2, col3 = st.columns(3)
            
            # Sort glossary alphabetically
            sorted_glossary = sorted(comprehensive_glossary, key=lambda x: x["term"])
            
            # Split into three equal parts
            chunk_size = len(sorted_glossary) // 3
            remainder = len(sorted_glossary) % 3
            
            chunk1_end = chunk_size + (1 if remainder > 0 else 0)
            chunk2_end = 2 * chunk_size + (2 if remainder > 1 else 1 if remainder > 0 else 0)
            
            # Display in columns
            with col1:
                for term in sorted_glossary[:chunk1_end]:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
            
            with col2:
                for term in sorted_glossary[chunk1_end:chunk2_end]:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
            
            with col3:
                for term in sorted_glossary[chunk2_end:]:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
    
    # Additional section for external resources
    st.header("External Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Regulatory Bodies")
        st.markdown("""
        * [SEBI - Securities and Exchange Board of India](https://www.sebi.gov.in/)
        * [RBI - Reserve Bank of India](https://www.rbi.org.in/)
        * [IRDAI - Insurance Regulatory and Development Authority of India](https://www.irdai.gov.in/)
        * [PFRDA - Pension Fund Regulatory and Development Authority](https://www.pfrda.org.in/)
        """)
    
    with col2:
        st.subheader("Market Information")
        st.markdown("""
        * [NSE - National Stock Exchange](https://www.nseindia.com/)
        * [BSE - Bombay Stock Exchange](https://www.bseindia.com/)
        * [AMFI - Association of Mutual Funds in India](https://www.amfiindia.com/)
        * [CRISIL - Credit Rating Information Services of India Limited](https://www.crisil.com/)
        """)
    
    # Interactive tool suggestion
    st.header("Interactive Learning Tools")
    st.write("Enhance your learning with these interactive tools and calculators.")
    
    tool_tabs = st.tabs(["Investment Calculators", "Risk Assessment Tools"])
    
    with tool_tabs[0]:
        st.markdown("""
        * [SIP Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) - Calculate returns on Systematic Investment Plans
        * [Lumpsum Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) - Calculate returns on one-time investments 
        * [Goal Planning Calculator](https://www.investor.gov/financial-tools-calculators/calculators/savings-goal-calculator) - Plan for your financial goals
        * [PPF Calculator](https://cleartax.in/s/ppf-calculator) - Calculate Public Provident Fund returns
        """)
    
    with tool_tabs[1]:
        st.markdown("""
        * [Risk Tolerance Quiz](https://www.investor.gov/introduction-investing/getting-started/assessing-your-risk-tolerance) - Understand your risk profile
        """)
    
    # Let users suggest additional resources
    st.header("Suggest a Resource")
    st.write("Know a helpful resource that should be included here? Share it with us!")
    
    with st.form("resource_suggestion"):
        resource_title = st.text_input("Resource Title")
        resource_type = st.selectbox("Resource Type", ["Video", "PDF", "Website", "Tool", "Other"])
        resource_url = st.text_input("URL")
        resource_description = st.text_area("Brief Description")
        resource_module = st.selectbox("Related Module", ["General", "Insurance", "Equity", "PMS & AIF", "Stocks", "Bonds"])
        
        submitted = st.form_submit_button("Submit Suggestion")
        if submitted:
            st.success("Thank you for your suggestion! Our team will review it.")
            
            # In a real application, this would save to a database
            if st.session_state.username:
                # Record activity
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                activity = f"{timestamp}: Suggested a resource: {resource_title}"
                st.session_state.activity.insert(0, activity)
                
                # Award points for contribution
                add_points(5, "suggesting a learning resource")
