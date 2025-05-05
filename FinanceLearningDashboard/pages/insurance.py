import streamlit as st
import time
from data.content import module_descriptions
from utils import update_module_progress, add_points
from PIL import Image
import os
from data.visualization import insurance_visualizations, get_real_world_examples

def show():
    """Display the Insurance learning module content"""
    
    st.title("Insurance")
    
    # Display the module image
    if os.path.exists("assets/images/insurance.png"):
        image = Image.open("assets/images/insurance.png")
        # Use a column to control image width
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)
    elif os.path.exists("attached_assets/20250427_1359_Life's Protective Helmet_simple_compose_01jsv5ryrweha9ws2ssw67jvyy.png"):
        image = Image.open("attached_assets/20250427_1359_Life's Protective Helmet_simple_compose_01jsv5ryrweha9ws2ssw67jvyy.png")
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
        highlighted_description = highlight_text(module_descriptions["Insurance"]["description"], search_term)
        st.markdown(highlighted_description, unsafe_allow_html=True)
    else:
        st.write(module_descriptions["Insurance"]["description"])
    
    # Navigation tabs
    main_tabs = st.tabs(["Learn", "Examples", "Data & Insights", "Glossary"])
    
    with main_tabs[0]:  # Learn tab
        # Create tabs for different sections
        tab_names = [section["title"] for section in module_descriptions["Insurance"]["sections"]]
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
            content = module_descriptions["Insurance"]["sections"][target_section]["content"]
            
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
                # Check if there's a search term to highlight in the section content
                if 'search_highlight' in st.session_state and st.session_state.search_highlight:
                    from utils import highlight_text
                    search_term = st.session_state.search_highlight
                    
                    # Highlight the section content
                    content = module_descriptions["Insurance"]["sections"][i]["content"]
                    highlighted_content = highlight_text(content, search_term)
                    st.markdown(highlighted_content, unsafe_allow_html=True)
                else:
                    st.markdown(module_descriptions["Insurance"]["sections"][i]["content"])
                
                # Mark this section as visited and update progress
                if st.session_state.username:
                    visited_sections.add(i)
                    progress_percentage = (len(visited_sections) / total_sections) * 100
                    update_module_progress("insurance", progress_percentage)
                    
                    # Add activity points for reading content
                    if f"insurance_section_{i}_read" not in st.session_state:
                        st.session_state[f"insurance_section_{i}_read"] = True
                        add_points(2, f"reading Insurance: {tab_names[i]}")
        
        # Update progress after visiting sections
        if st.session_state.username and visited_sections:
            progress_percentage = (len(visited_sections) / total_sections) * 100
            update_module_progress("insurance", progress_percentage)
    
    with main_tabs[1]:  # Examples tab
        st.header("Real-World Insurance Examples")
        
        examples = get_real_world_examples("Insurance")
        for example in examples:
            with st.expander(example["title"], expanded=False):
                st.markdown(example["content"])
    
    with main_tabs[2]:  # Data & Insights tab
        st.header("Insurance Market Data & Insights")
        st.write("Explore visual representations of insurance market data and trends.")
        
        # Display data visualizations
        insurance_visualizations()
    
    with main_tabs[3]:  # Glossary tab
        st.header("Insurance Glossary of Terms")
        
        # Convert glossary to DataFrame for better display
        glossary_terms = module_descriptions["Insurance"]["glossary"]
        
        # Check if there's a global search highlight first
        global_search = None
        if 'search_highlight' in st.session_state and st.session_state.search_highlight:
            global_search = st.session_state.search_highlight
            st.text_input("Search terms", value=global_search, key="insurance_glossary_search")
        else:
            # Allow search in glossary
            search_term = st.text_input("Search terms", key="insurance_glossary_search")
        
        # Use the global search if available, otherwise use the local search
        active_search_term = global_search if global_search else st.session_state.insurance_glossary_search
        
        filtered_terms = glossary_terms
        if active_search_term:
            filtered_terms = [term for term in glossary_terms 
                            if active_search_term.lower() in term["term"].lower() or 
                               active_search_term.lower() in term["definition"].lower()]
        
        if not filtered_terms:
            st.info("No matching terms found.")
        else:
            # Display in two columns
            col1, col2 = st.columns(2)
            
            half = len(filtered_terms) // 2
            
            # Import highlight function if needed
            from utils import highlight_text
            
            with col1:
                for term in filtered_terms[:half]:
                    if active_search_term:
                        # Highlight both term and definition
                        highlighted_term = highlight_text(term["term"], active_search_term)
                        highlighted_def = highlight_text(term["definition"], active_search_term)
                        st.markdown(f"**{highlighted_term}**: {highlighted_def}", unsafe_allow_html=True)
                    else:
                        st.markdown(f"**{term['term']}**: {term['definition']}")
            
            with col2:
                for term in filtered_terms[half:]:
                    if active_search_term:
                        # Highlight both term and definition
                        highlighted_term = highlight_text(term["term"], active_search_term)
                        highlighted_def = highlight_text(term["definition"], active_search_term)
                        st.markdown(f"**{highlighted_term}**: {highlighted_def}", unsafe_allow_html=True)
                    else:
                        st.markdown(f"**{term['term']}**: {term['definition']}")
    
    # Call-to-action for quiz
    st.header("Test Your Knowledge")
    st.write("Now that you've learned about Insurance, test your knowledge with a quiz!")
    
    quiz_cols = st.columns(3)
    with quiz_cols[0]:
        if st.button("Take Easy Quiz", key="insurance_easy_quiz"):
            st.session_state.selected_quiz = "Insurance"
            st.session_state.quiz_difficulty = "Easy"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[1]:
        if st.button("Take Moderate Quiz", key="insurance_moderate_quiz"):
            st.session_state.selected_quiz = "Insurance"
            st.session_state.quiz_difficulty = "Moderate"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
    
    with quiz_cols[2]:
        if st.button("Take Difficult Quiz", key="insurance_difficult_quiz"):
            st.session_state.selected_quiz = "Insurance"
            st.session_state.quiz_difficulty = "Difficult"
            st.session_state.page = "Quiz Zone"
            time.sleep(0.1)
            st.rerun()
