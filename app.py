import streamlit as st
from PIL import Image
from rembg import remove
import io

# Mobile-friendly Page Config
st.set_page_config(
    page_title="Artisan Market Linkage",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Smart Artisan Cataloging")
st.caption("AI-Powered Tool for Marginalized Artisans")

st.divider()

# Step 1: Artisan Details & Voice/Text Input
st.subheader("1. Product Basic Info")
artisan_name = st.text_input("Artisan Name", placeholder="e.g. Ramesh Kumar")
language = st.selectbox("Preferred Language", ["Hindi", "English", "Bengali", "Tamil"])
product_speech = st.text_area("Product Details (Type or Voice Dictate)", placeholder="Product ke baare mein batayein...")

# Step 2: Camera Capture / Image Upload
st.subheader("2. Capture Product Photo")
image_file = st.camera_input("Take a photo of the product")

if image_file is not None:
    # Display Original Image
    raw_image = Image.open(image_file)
    st.image(raw_image, caption="Original Photo", use_container_width=True)
    
    # Step 3: AI Background Removal (Rembg)
    with st.spinner("AI is cleaning background..."):
        img_bytes = image_file.getvalue()
        output_bytes = remove(img_bytes)
        processed_image = Image.open(io.BytesIO(output_bytes))
        
        st.success("Background Removed Successfully!")
        st.image(processed_image, caption="Smart Catalog Ready Photo", use_container_width=True)

    # Step 4: Auto-Generate Tags & Price Suggestion
    st.subheader("3. AI Generated Catalog Details")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Suggested Price", value="₹1,250")
    with col2:
        st.metric(label="Category", value="Handicrafts / Pottery")

    st.write("**Auto-Generated Description:**")
    st.info(f"Authentic handmade item by {artisan_name}. High quality, eco-friendly traditional craftsmanship.")

    # Step 5: Direct WhatsApp Market Linkage
    st.divider()
    st.subheader("4. Instant Market Linkage")
    
    whatsapp_number = "919876543210" # Replace with actual number
    message = f"Hello! I am interested in buying this product by {artisan_name}."
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message}"
    
    st.link_button("📲 Connect Direct on WhatsApp", whatsapp_url, use_container_width=True)

