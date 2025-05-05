import streamlit as st
import os
import pandas as pd
from utils import initialize_session_state
from data.content import module_descriptions

# Import all page modules at the beginning
import pages.insurance
import pages.equity
import pages.pms_aif
import pages.stocks
import pages.bonds
import pages.quiz
import pages.resources
import pages.user_dashboard

# Set page configuration
st.set_page_config(
    page_title="Finance Education Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
initialize_session_state()

# Sidebar navigation
st.sidebar.title("Navigation")

# User info in sidebar
if st.session_state.username:
    st.sidebar.write(f"Welcome, {st.session_state.username}!")
    st.sidebar.write(f"Level: {st.session_state.level_name}")
    st.sidebar.progress(st.session_state.level_progress)
    st.sidebar.write(f"Total Points: {st.session_state.points}")
    
    # Display badges
    if st.session_state.badges:
        st.sidebar.subheader("Your Badges")
        badges_text = ", ".join(st.session_state.badges)
        st.sidebar.write(badges_text)
    
    if st.sidebar.button("Log Out"):
        for key in list(st.session_state.keys()):
            if key != "pages":
                del st.session_state[key]
        initialize_session_state()
        st.rerun()
else:
    # Login/signup form
    login_tab, signup_tab = st.sidebar.tabs(["Login", "Sign Up"])
    
    with login_tab:
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            if login_username:
                st.session_state.username = login_username
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please enter a username")
    
    with signup_tab:
        signup_username = st.text_input("Choose Username", key="signup_username")
        signup_password = st.text_input("Choose Password", type="password", key="signup_password")
        if st.button("Sign Up"):
            if signup_username:
                st.session_state.username = signup_username
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please enter a username")

# Navigation links
page_names = ["Home", "Insurance", "Equity", "PMS & AIF", "Stocks", "Bonds", "Quiz Zone", "Resources", "Dashboard"]

# Check if there's a page stored in session state (e.g., from button navigation)
if 'page' in st.session_state:
    current_page = st.session_state.page
    # Find the index of the current page in page_names
    try:
        current_index = page_names.index(current_page)
    except ValueError:
        current_index = 0  # Default to Home if page not found
else:
    current_index = 0  # Default to Home

# Display the radio buttons with the current page selected
page = st.sidebar.radio("Go to", page_names, index=current_index)

# Update session state if the page changes via the radio button
if 'page' not in st.session_state or st.session_state.page != page:
    st.session_state.page = page

# Advanced search functionality in sidebar
st.sidebar.subheader("Search")
search_term = st.sidebar.text_input("Search topics")
if search_term:
    st.sidebar.write(f"Showing results for: {search_term}")
    results = []
    
    # Store detailed search results with content matches
    detailed_results = {}
    # Store specific section matches
    section_matches = {}
    
    # Search in module descriptions and content
    for module, content in module_descriptions.items():
        module_found = False
        
        # First, check if any specific section titles match the search
        for i, section in enumerate(content.get("sections", [])):
            section_title = section.get("title", "").lower()
            if search_term.lower() in section_title:
                if module not in section_matches:
                    section_matches[module] = []
                section_matches[module].append({
                    "section_title": section["title"],
                    "section_index": i
                })
                module_found = True
                
        # Then check content
        content_str = str(content).lower()
        if search_term.lower() in module.lower() or search_term.lower() in content_str:
            if not module_found:
                results.append(module)
            
            # Store where the term was found in the content
            if search_term.lower() in content_str:
                # Find the paragraph containing the search term
                paragraphs = content_str.split('\n')
                for para in paragraphs:
                    if search_term.lower() in para:
                        if module not in detailed_results:
                            detailed_results[module] = []
                        # Store only the first 150 characters of the matching paragraph
                        detailed_results[module].append(para[:150] + "...")
    
    if section_matches or results:
        # First, display section-specific matches
        if section_matches:
            st.sidebar.write("Found in specific sections:")
            for module, sections in section_matches.items():
                for section in sections:
                    # Button to navigate directly to the section
                    btn_label = f"{module}: {section['section_title']}"
                    if st.sidebar.button(btn_label, key=f"section_{module}_{section['section_index']}"):
                        st.session_state.page = module
                        st.session_state.search_highlight = search_term
                        # Store the section index to jump directly to it
                        st.session_state.jump_to_section = section['section_index']
                        st.rerun()
        
        # Then display module-level matches
        if results:
            st.sidebar.write("Found in modules:")
            for result in results:
                # Show a snippet of the content match if available
                if result in detailed_results:
                    for i, snippet in enumerate(detailed_results[result][:2]):  # Show up to 2 snippets
                        st.sidebar.markdown(f"*{snippet}*")
                
                # Button to navigate to the module
                if st.sidebar.button(f"Go to {result}", key=f"search_{result}"):
                    st.session_state.page = result
                    # Store search term to highlight on the destination page
                    st.session_state.search_highlight = search_term
                    st.rerun()
    else:
        st.sidebar.write("No results found")
else:
    # Clear the highlight term when search is cleared
    if 'search_highlight' in st.session_state:
        del st.session_state.search_highlight
    if 'jump_to_section' in st.session_state:
        del st.session_state.jump_to_section

# Global search bar at the top
st.markdown("### Search all modules")
global_search = st.text_input("Type keywords to find content across all modules", key="global_search_bar")

if global_search:
    st.subheader(f"Search results for: '{global_search}'")
    
    # Store detailed search results with content matches
    detailed_results = {}
    # Store specific section matches
    section_matches = {}
    
    # Count total results
    total_results = 0
    
    # Search in module descriptions and content
    for module, content in module_descriptions.items():
        # First, check if any specific section titles match the search
        for i, section in enumerate(content.get("sections", [])):
            section_title = section.get("title", "").lower()
            section_content = section.get("content", "").lower()
            
            if global_search.lower() in section_title or global_search.lower() in section_content:
                if module not in section_matches:
                    section_matches[module] = []
                
                # Extract a snippet of content containing the search term
                content_excerpt = ""
                if global_search.lower() in section_content:
                    # Find the position of the search term
                    pos = section_content.find(global_search.lower())
                    # Get a window of text around the match
                    start = max(0, pos - 100)
                    end = min(len(section_content), pos + 100)
                    content_excerpt = f"...{section_content[start:end]}..."
                
                section_matches[module].append({
                    "section_title": section["title"],
                    "section_index": i,
                    "excerpt": content_excerpt
                })
                total_results += 1
    
    if total_results > 0:
        st.success(f"Found {total_results} matching results")
        
        # Display section-specific matches
        for module, sections in section_matches.items():
            st.markdown(f"### In {module} module:")
            
            for section in sections:
                with st.expander(f"{section['section_title']}"):
                    if section["excerpt"]:
                        from utils import highlight_text
                        highlighted_excerpt = highlight_text(section["excerpt"], global_search)
                        st.markdown(highlighted_excerpt, unsafe_allow_html=True)
                    
                    # Button to navigate directly to the section
                    if st.button(f"Go to this section", key=f"global_section_{module}_{section['section_index']}"):
                        st.session_state.page = module
                        st.session_state.search_highlight = global_search
                        # Store the section index to jump directly to it
                        st.session_state.jump_to_section = section['section_index']
                        st.rerun()
    else:
        st.warning("No matching content found. Try different keywords.")

# Main page content
if page == "Home":
    st.title("Finance Education Dashboard")
    
    st.write("""
    ## Welcome to the Finance Education Portal!
    
    This platform is designed to help you learn about various financial topics in a structured and interactive way.
    Explore different modules, test your knowledge with quizzes, and track your progress.
    """)
    
    # Display modules
    st.header("Learning Modules")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Insurance")
        st.write("Learn about different types of insurance, policies, and how to choose the right coverage.")
        if st.button("Explore Insurance"):
            st.session_state.page = "Insurance"
            st.rerun()
    
    with col2:
        st.subheader("Equity")
        st.write("Understand stock markets, equity investments, and strategies for long-term wealth creation.")
        if st.button("Explore Equity"):
            st.session_state.page = "Equity"
            st.rerun()
    
    with col3:
        st.subheader("PMS & AIF")
        st.write("Discover Portfolio Management Services and Alternative Investment Funds for high-value investors.")
        if st.button("Explore PMS & AIF"):
            st.session_state.page = "PMS & AIF"
            st.rerun()
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.subheader("Stocks")
        st.write("Master the fundamentals of stock market investing, analysis, and trading strategies.")
        if st.button("Explore Stocks"):
            st.session_state.page = "Stocks"
            st.rerun()
    
    with col5:
        st.subheader("Bonds")
        st.write("Learn about fixed income securities, government and corporate bonds, and debt investments.")
        if st.button("Explore Bonds"):
            st.session_state.page = "Bonds"
            st.rerun()
    
    with col6:
        st.subheader("Quiz Zone")
        st.write("Test your knowledge, earn points, and unlock badges through interactive quizzes.")
        if st.button("Take Quizzes"):
            st.session_state.page = "Quiz Zone"
            st.rerun()
    
    # Quick stats for logged-in users
    if st.session_state.username:
        st.header("Your Learning Journey")
        
        # Progress overview
        st.subheader("Module Progress")
        modules = ["Insurance", "Equity", "PMS & AIF", "Stocks", "Bonds"]
        progress_data = {
            "Module": modules,
            "Progress (%)": [
                st.session_state.get(f"insurance_progress", 0),
                st.session_state.get(f"equity_progress", 0),
                st.session_state.get(f"pms_aif_progress", 0),
                st.session_state.get(f"stocks_progress", 0),
                st.session_state.get(f"bonds_progress", 0)
            ]
        }
        
        progress_df = pd.DataFrame(progress_data)
        st.dataframe(progress_df, hide_index=True)
        
        # Recent activity
        st.subheader("Recent Activity")
        if not st.session_state.activity:
            st.write("No recent activity. Start exploring modules!")
        else:
            for activity in st.session_state.activity[-5:]:
                st.write(f"- {activity}")
    
    # Quick tips
    st.header("Finance Quick Tips")
    tips = [
        "Diversification is key to reducing investment risk.",
        "Start investing early to leverage the power of compounding.",
        "Always read the fine print in insurance policies.",
        "Maintain an emergency fund covering 3-6 months of expenses.",
        "Tax planning should be integrated with your investment strategy."
    ]
    
    for tip in tips:
        st.markdown(f"* {tip}")

elif page == "Insurance":
    pages.insurance.show()
elif page == "Equity":
    pages.equity.show()
elif page == "PMS & AIF":
    pages.pms_aif.show()
elif page == "Stocks":
    pages.stocks.show()
elif page == "Bonds":
    pages.bonds.show()
elif page == "Quiz Zone":
    pages.quiz.show()
elif page == "Resources":
    pages.resources.show()
elif page == "Dashboard":
    pages.user_dashboard.show()
