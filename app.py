import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Qudra Properties",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🏠 Qudra Properties")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.selectbox(
        "Choose a page",
        ["Home", "Property Listings", "Add Property", "Search Properties"]
    )

# Initialize session state for storing user requirements
if 'user_requirements' not in st.session_state:
    st.session_state.user_requirements = {}

# Main content area
if page == "Home":
    st.header("Find Your Perfect Property Investment")
    st.write("Tell us about your property needs and requirements, and we'll connect you with the best developments.")
    st.markdown("---")
    
    with st.form("property_requirements_form"):
        st.subheader("📋 Your Property Requirements")
        
        # Personal Information Section
        st.markdown("### 👤 Contact Information")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *", placeholder="John Doe")
            email = st.text_input("Email Address *", placeholder="john@example.com")
        with col2:
            phone = st.text_input("Phone Number *", placeholder="+447775556668")
            preferred_contact = st.selectbox("Preferred Contact Method", ["Email", "Phone", "Either"])
        
        st.markdown("---")
        
        # Property Type & Location
        st.markdown("### 🏘️ Property Preferences")
        col1, col2 = st.columns(2)
        with col1:
            property_type = st.selectbox(
                "Property Type *",
                ["Select...", "Residential Apartment", "Residential House", "Commercial", "Mixed-Use", "Land/Plot", "Other"]
            )
            preferred_location = st.text_input("Preferred Location/City *", placeholder="e.g., New York, Los Angeles")
            location_flexibility = st.selectbox(
                "Location Flexibility",
                ["Very Flexible", "Somewhat Flexible", "Specific Area Only"]
            )
        with col2:
            investment_purpose = st.selectbox(
                "Investment Purpose *",
                ["Select...", "Primary Residence", "Rental Income", "Capital Appreciation", "Vacation Home", "Commercial Use", "Other"]
            )

            timeline = st.selectbox(
                "Purchase Timeline *",
                ["Select...", "Immediately (0-3 months)", "Short-term (3-6 months)", "Medium-term (6-12 months)", "Long-term (12+ months)", "Just Exploring"]
            )
        
        st.markdown("---")
        
        # Budget & Financial
        st.markdown("### 💰 Budget & Financial Information")
        col1, col2, col3 = st.columns(3)
        with col1:
            budget_min = st.number_input("Minimum Budget ($)", min_value=0, step=10000, value=0)
        with col2:
            budget_max = st.number_input("Maximum Budget ($) *", min_value=0, step=10000, value=500000)
        with col3:
            financing_needed = st.selectbox(
                "Financing Required?",
                ["Yes", "No", "Not Sure"]
            )
        
        st.markdown("---")
        
        # Property Specifications
        st.markdown("### 🏠 Property Specifications")
        col1, col2 = st.columns(2)
        with col1:
            bedrooms = st.selectbox(
                "Number of Bedrooms",
                ["Any", "Studio", "1", "2", "3", "4", "5+"]
            )
            bathrooms = st.selectbox(
                "Number of Bathrooms",
                ["Any", "1", "1.5", "2", "2.5", "3", "3+"]
            )
            square_feet_min = st.number_input("Minimum Square Feet", min_value=0, step=100, value=0)
        with col2:
            property_size_preference = st.selectbox(
                "Property Size Preference",
                ["Compact", "Medium", "Large", "Luxury", "No Preference"]
            )
            parking_required = st.selectbox(
                "Parking Required?",
                ["Yes", "No", "Preferred but not required"]
            )
            amenities_priority = st.multiselect(
                "Priority Amenities",
                ["Swimming Pool", "Gym/Fitness Center", "Security", "Parking", "Garden/Balcony", "Elevator", "Near Public Transport", "Shopping Nearby", "Schools Nearby", "Other"]
            )
        
        st.markdown("---")
        
        # Additional Requirements
        st.markdown("### 📝 Additional Requirements")
        special_requirements = st.text_area(
            "Any Special Requirements or Preferences",
            placeholder="e.g., Must be pet-friendly, needs to be wheelchair accessible, specific architectural style, etc.",
            height=100
        )
        
        property_condition = st.selectbox(
            "Preferred Property Condition",
            ["New Construction", "Recently Renovated", "Good Condition", "Needs Renovation", "Any"]
        )
        
        st.markdown("---")
        
        # Submit Button
        submitted = st.form_submit_button("🚀 Submit Requirements", use_container_width=True)
        
        if submitted:
            # Validation
            if not full_name or not email or not phone:
                st.error("⚠️ Please fill in all required fields marked with *")
            elif property_type == "Select..." or investment_purpose == "Select..." or timeline == "Select...":
                st.error("⚠️ Please select all required dropdown options")
            elif not preferred_location:
                st.error("⚠️ Please enter your preferred location")
            else:
                # Store requirements in session state
                st.session_state.user_requirements = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "preferred_contact": preferred_contact,
                    "property_type": property_type,
                    "preferred_location": preferred_location,
                    "location_flexibility": location_flexibility,
                    "investment_purpose": investment_purpose,
                    "timeline": timeline,
                    "budget_min": budget_min,
                    "budget_max": budget_max,
                    "financing_needed": financing_needed,
                    "bedrooms": bedrooms,
                    "bathrooms": bathrooms,
                    "square_feet_min": square_feet_min,
                    "property_size_preference": property_size_preference,
                    "parking_required": parking_required,
                    "amenities_priority": amenities_priority,
                    "special_requirements": special_requirements,
                    "property_condition": property_condition
                }
                
                st.success("✅ Thank you! Your requirements have been submitted successfully.")
                st.balloons()
                
                st.markdown("---")
                st.subheader("📊 Your Requirements Summary")
                
                # Display summary
                summary_col1, summary_col2 = st.columns(2)
                with summary_col1:
                    st.write(f"**Name:** {full_name}")
                    st.write(f"**Email:** {email}")
                    st.write(f"**Phone:** {phone}")
                    st.write(f"**Property Type:** {property_type}")
                    st.write(f"**Location:** {preferred_location}")
                    st.write(f"**Investment Purpose:** {investment_purpose}")
                    st.write(f"**Timeline:** {timeline}")
                
                with summary_col2:
                    st.write(f"**Budget Range:** ${budget_min:,} - ${budget_max:,}")
                    st.write(f"**Bedrooms:** {bedrooms}")
                    st.write(f"**Bathrooms:** {bathrooms}")
                    st.write(f"**Size Preference:** {property_size_preference}")
                    st.write(f"**Parking:** {parking_required}")
                    if amenities_priority:
                        st.write(f"**Priority Amenities:** {', '.join(amenities_priority)}")
                
                st.info("💡 Our team will review your requirements and connect you with matching developments soon!")

elif page == "Property Listings":
    st.header("Property Listings")
    st.write("View all your properties here.")
    # Placeholder for property listings
    st.info("Property listings will be displayed here.")

elif page == "Add Property":
    st.header("Add New Property")
    
    with st.form("add_property_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            property_name = st.text_input("Property Name")
            property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo", "Townhouse", "Other"])
            address = st.text_input("Address")
            city = st.text_input("City")
            state = st.text_input("State")
        
        with col2:
            zip_code = st.text_input("ZIP Code")
            price = st.number_input("Price ($)", min_value=0, step=1000)
            bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
            bathrooms = st.number_input("Bathrooms", min_value=0.0, step=0.5)
            square_feet = st.number_input("Square Feet", min_value=0, step=100)
        
        description = st.text_area("Description")
        
        submitted = st.form_submit_button("Add Property")
        
        if submitted:
            st.success(f"Property '{property_name}' added successfully!")

elif page == "Search Properties":
    st.header("Search Properties")
    
    search_query = st.text_input("Search by name, address, or city")
    filter_type = st.selectbox("Filter by Type", ["All", "House", "Apartment", "Condo", "Townhouse"])
    
    if st.button("Search"):
        st.info(f"Searching for: {search_query}")
        st.info(f"Filter: {filter_type}")
