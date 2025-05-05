import streamlit as st
import time
from data.content import module_descriptions
from utils import update_module_progress, add_points
from PIL import Image
import os
from data.visualization import stocks_visualizations, get_real_world_examples

def show():
    """Display the Stocks learning module content"""
    
    st.title("Stocks")
    
    # Display the module image
    if os.path.exists("assets/images/stocks.png"):
        image = Image.open("assets/images/stocks.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    elif os.path.exists("attached_assets/20250429_1857_Investment Growth Metaphor_simple_compose_01jt0vkr9jftk8p45h8wj1x3yq.png"):
        image = Image.open("attached_assets/20250429_1857_Investment Growth Metaphor_simple_compose_01jt0vkr9jftk8p45h8wj1x3yq.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    
    st.write(module_descriptions["Stocks"]["description"])
    
    # Navigation tabs
    main_tabs = st.tabs(["Learn", "Examples", "Data & Insights", "Glossary"])
    
    with main_tabs[0]:  # Learn tab
        # Create tabs for different sections
        tab_names = [section["title"] for section in module_descriptions["Stocks"]["sections"]]
        learn_tabs = st.tabs(tab_names)
        
        # Track progress
        total_sections = len(tab_names)
        visited_sections = set()
        
        # Check if we need to jump to a specific section
        active_tab_index = 0
        if 'jump_to_section' in st.session_state:
            active_tab_index = st.session_state.jump_to_section
            # Remove the session state after using it
            del st.session_state.jump_to_section
        
        # Populate each tab with content
        for i, tab in enumerate(learn_tabs):
            with tab:
                # Check if we need to highlight search terms
                if 'search_highlight' in st.session_state and st.session_state.search_highlight:
                    # Get the content and highlight the search term
                    content = module_descriptions["Stocks"]["sections"][i]["content"]
                    from utils import highlight_text
                    highlighted_content = highlight_text(content, st.session_state.search_highlight)
                    st.markdown(highlighted_content, unsafe_allow_html=True)
                else:
                    st.markdown(module_descriptions["Stocks"]["sections"][i]["content"])
                
                # Mark this section as visited and update progress
                if st.session_state.username:
                    visited_sections.add(i)
                    progress_percentage = (len(visited_sections) / total_sections) * 100
                    update_module_progress("stocks", progress_percentage)
                    
                    # Add activity points for reading content
                    if f"stocks_section_{i}_read" not in st.session_state:
                        st.session_state[f"stocks_section_{i}_read"] = True
                        add_points(2, f"reading Stocks: {tab_names[i]}")
                        
        # Set active tab based on jump_to_section
        if active_tab_index > 0:
            js = f"""
            <script>
                // Wait for the DOM to be fully loaded
                document.addEventListener('DOMContentLoaded', (event) => {{
                    // Find the tabs
                    const tabs = document.querySelectorAll('button[role="tab"]');
                    // Click the specified tab
                    if (tabs.length > {active_tab_index}) {{
                        tabs[{active_tab_index}].click();
                    }}
                }});
            </script>
            """
            st.components.v1.html(js, height=0)
    
    with main_tabs[1]:  # Examples tab
        st.header("Real-World Stock Examples")
        
        examples = get_real_world_examples("Stocks")
        for example in examples:
            with st.expander(example["title"], expanded=False):
                st.markdown(example["content"])
    
    with main_tabs[2]:  # Data & Insights tab
        st.header("Stock Market Data & Insights")
        st.write("Explore visual representations of stock market data and trends.")
        
        # Display data visualizations
        stocks_visualizations()
    
    with main_tabs[3]:  # Glossary tab
        st.header("Stocks Glossary of Terms")
        
        # Convert glossary to DataFrame for better display
        glossary_terms = module_descriptions["Stocks"]["glossary"]
        
        # Allow search in glossary
        search_term = st.text_input("Search terms", key="stocks_glossary_search")
        
        filtered_terms = glossary_terms
        if search_term:
            filtered_terms = [term for term in glossary_terms 
                            if search_term.lower() in term["term"].lower() or 
                               search_term.lower() in term["definition"].lower()]
        
        if not filtered_terms:
            st.info("No matching terms found.")
        else:
            # Display in two columns
            col1, col2 = st.columns(2)
            
            half = len(filtered_terms) // 2
            
            with col1:
                for term in filtered_terms[:half]:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
            
            with col2:
                for term in filtered_terms[half:]:
                    st.markdown(f"**{term['term']}**: {term['definition']}")
    
    # Call-to-action for quiz
    st.header("Test Your Knowledge")
    st.write("Now that you've learned about Stocks, test your knowledge with a quiz!")
    
    quiz_cols = st.columns(3)
    with quiz_cols[0]:
        if st.button("Take Easy Quiz", key="stocks_easy_quiz"):
            st.session_state.selected_quiz = "Stocks"
            st.session_state.quiz_difficulty = "Easy"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[1]:
        if st.button("Take Moderate Quiz", key="stocks_moderate_quiz"):
            st.session_state.selected_quiz = "Stocks"
            st.session_state.quiz_difficulty = "Moderate"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[2]:
        if st.button("Take Difficult Quiz", key="stocks_difficult_quiz"):
            st.session_state.selected_quiz = "Stocks"
            st.session_state.quiz_difficulty = "Difficult"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
