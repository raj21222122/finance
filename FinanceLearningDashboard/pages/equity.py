import streamlit as st
import time
from data.content import module_descriptions
from utils import update_module_progress, add_points
from PIL import Image
import os
from data.visualization import equity_visualizations, get_real_world_examples

def show():
    """Display the Equity learning module content"""
    
    st.title("Equity")
    
    # Display the module image
    if os.path.exists("assets/images/equity.png"):
        image = Image.open("assets/images/equity.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    elif os.path.exists("attached_assets/20250427_1401_Investing Pizza Party_simple_compose_01jsv5xd1jf74bsyt1g8dkt38v.png"):
        image = Image.open("attached_assets/20250427_1401_Investing Pizza Party_simple_compose_01jsv5xd1jf74bsyt1g8dkt38v.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    
    # Check if there's a search term to highlight in the description
    if 'search_highlight' in st.session_state and st.session_state.search_highlight:
        from utils import highlight_text
        search_term = st.session_state.search_highlight
        st.info(f"Showing results for: '{search_term}'")
        
        # Highlight the description
        highlighted_description = highlight_text(module_descriptions["Equity"]["description"], search_term)
        st.markdown(highlighted_description, unsafe_allow_html=True)
    else:
        st.write(module_descriptions["Equity"]["description"])
    
    # Navigation tabs
    main_tabs = st.tabs(["Learn", "Examples", "Data & Insights", "Glossary"])
    
    with main_tabs[0]:  # Learn tab
        # Create tabs for different sections
        tab_names = [section["title"] for section in module_descriptions["Equity"]["sections"]]
        learn_tabs = st.tabs(tab_names)
        
        # Track progress
        total_sections = len(tab_names)
        visited_sections = set()
        
        # Check if we need to jump to a specific section
        # Since Streamlit tabs don't support programmatic selection,
        # we'll display the section content directly when jumping from search
        if 'jump_to_section' in st.session_state:
            target_section = st.session_state.jump_to_section
            section_title = tab_names[target_section]
            st.info(f"Showing content for section: {section_title}")
            
            # Display the content of the target section
            content = module_descriptions["Equity"]["sections"][target_section]["content"]
            
            if 'search_highlight' in st.session_state and st.session_state.search_highlight:
                from utils import highlight_text
                search_term = st.session_state.search_highlight
                highlighted_content = highlight_text(content, search_term)
                st.markdown(highlighted_content, unsafe_allow_html=True)
            else:
                st.markdown(content)
                
            # Mark this section as visited
            if st.session_state.username:
                visited_sections.add(target_section)
                
            # Remove the session state after displaying
            del st.session_state.jump_to_section
        
        # Populate each tab with content
        for i, tab in enumerate(learn_tabs):
            with tab:
                # Check if we need to highlight search terms
                if 'search_highlight' in st.session_state and st.session_state.search_highlight:
                    # Get the content and highlight the search term
                    content = module_descriptions["Equity"]["sections"][i]["content"]
                    from utils import highlight_text
                    highlighted_content = highlight_text(content, st.session_state.search_highlight)
                    st.markdown(highlighted_content, unsafe_allow_html=True)
                else:
                    st.markdown(module_descriptions["Equity"]["sections"][i]["content"])
                
                # Mark this section as visited and update progress
                if st.session_state.username:
                    visited_sections.add(i)
                    progress_percentage = (len(visited_sections) / total_sections) * 100
                    update_module_progress("equity", progress_percentage)
                    
                    # Add activity points for reading content
                    if f"equity_section_{i}_read" not in st.session_state:
                        st.session_state[f"equity_section_{i}_read"] = True
                        add_points(2, f"reading Equity: {tab_names[i]}")
        
        # Update progress after visiting sections
        if st.session_state.username and visited_sections:
            progress_percentage = (len(visited_sections) / total_sections) * 100
            update_module_progress("equity", progress_percentage)
    
    with main_tabs[1]:  # Examples tab
        st.header("Real-World Equity Examples")
        
        examples = get_real_world_examples("Equity")
        for example in examples:
            with st.expander(example["title"], expanded=False):
                st.markdown(example["content"])
    
    with main_tabs[2]:  # Data & Insights tab
        st.header("Equity Market Data & Insights")
        st.write("Explore visual representations of equity market data and trends.")
        
        # Display data visualizations
        equity_visualizations()
    
    with main_tabs[3]:  # Glossary tab
        st.header("Equity Glossary of Terms")
        
        # Convert glossary to DataFrame for better display
        glossary_terms = module_descriptions["Equity"]["glossary"]
        
        # Allow search in glossary
        search_term = st.text_input("Search terms", key="equity_glossary_search")
        
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
    st.write("Now that you've learned about Equity, test your knowledge with a quiz!")
    
    quiz_cols = st.columns(3)
    with quiz_cols[0]:
        if st.button("Take Easy Quiz", key="equity_easy_quiz"):
            st.session_state.selected_quiz = "Equity"
            st.session_state.quiz_difficulty = "Easy"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[1]:
        if st.button("Take Moderate Quiz", key="equity_moderate_quiz"):
            st.session_state.selected_quiz = "Equity"
            st.session_state.quiz_difficulty = "Moderate"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[2]:
        if st.button("Take Difficult Quiz", key="equity_difficult_quiz"):
            st.session_state.selected_quiz = "Equity"
            st.session_state.quiz_difficulty = "Difficult"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
