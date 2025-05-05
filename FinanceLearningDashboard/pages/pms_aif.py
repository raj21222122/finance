import streamlit as st
import time
from data.content import module_descriptions
from utils import update_module_progress, add_points
from PIL import Image
import os
from data.visualization import pms_aif_visualizations, get_real_world_examples

def show():
    """Display the PMS & AIF learning module content"""
    
    st.title("Portfolio Management Services & Alternative Investment Funds")
    
    # Display the module image
    if os.path.exists("assets/images/pms_aif.png"):
        image = Image.open("assets/images/pms_aif.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    elif os.path.exists("attached_assets/20250429_1902_Tailored Investment Solutions_simple_compose_01jt0vxd90fn2th5k7cf250914.png"):
        image = Image.open("attached_assets/20250429_1902_Tailored Investment Solutions_simple_compose_01jt0vxd90fn2th5k7cf250914.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    
    st.write(module_descriptions["PMS & AIF"]["description"])
    
    # Navigation tabs
    main_tabs = st.tabs(["Learn", "Examples", "Data & Insights", "Glossary"])
    
    with main_tabs[0]:  # Learn tab
        # Create tabs for different sections
        tab_names = [section["title"] for section in module_descriptions["PMS & AIF"]["sections"]]
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
                    content = module_descriptions["PMS & AIF"]["sections"][i]["content"]
                    from utils import highlight_text
                    highlighted_content = highlight_text(content, st.session_state.search_highlight)
                    st.markdown(highlighted_content, unsafe_allow_html=True)
                else:
                    st.markdown(module_descriptions["PMS & AIF"]["sections"][i]["content"])
                
                # Mark this section as visited and update progress
                if st.session_state.username:
                    visited_sections.add(i)
                    progress_percentage = (len(visited_sections) / total_sections) * 100
                    update_module_progress("pms_aif", progress_percentage)
                    
                    # Add activity points for reading content
                    if f"pms_aif_section_{i}_read" not in st.session_state:
                        st.session_state[f"pms_aif_section_{i}_read"] = True
                        add_points(2, f"reading PMS & AIF: {tab_names[i]}")
        
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
        st.header("Real-World PMS & AIF Examples")
        
        examples = get_real_world_examples("PMS & AIF")
        for example in examples:
            with st.expander(example["title"], expanded=False):
                st.markdown(example["content"])
    
    with main_tabs[2]:  # Data & Insights tab
        st.header("PMS & AIF Market Data & Insights")
        st.write("Explore visual representations of PMS & AIF market data and trends.")
        
        # Display data visualizations
        pms_aif_visualizations()
    
    with main_tabs[3]:  # Glossary tab
        st.header("PMS & AIF Glossary of Terms")
        
        # Convert glossary to DataFrame for better display
        glossary_terms = module_descriptions["PMS & AIF"]["glossary"]
        
        # Allow search in glossary
        search_term = st.text_input("Search terms", key="pms_aif_glossary_search")
        
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
    st.write("Now that you've learned about PMS & AIF, test your knowledge with a quiz!")
    
    quiz_cols = st.columns(3)
    with quiz_cols[0]:
        if st.button("Take Easy Quiz", key="pms_aif_easy_quiz"):
            st.session_state.selected_quiz = "PMS & AIF"
            st.session_state.quiz_difficulty = "Easy"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[1]:
        if st.button("Take Moderate Quiz", key="pms_aif_moderate_quiz"):
            st.session_state.selected_quiz = "PMS & AIF"
            st.session_state.quiz_difficulty = "Moderate"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[2]:
        if st.button("Take Difficult Quiz", key="pms_aif_difficult_quiz"):
            st.session_state.selected_quiz = "PMS & AIF"
            st.session_state.quiz_difficulty = "Difficult"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
