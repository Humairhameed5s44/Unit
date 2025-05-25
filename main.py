import streamlit as st
import math

def convert_length(value, from_unit, to_unit):
    """Convert length units to meters first, then to target unit"""
    # Convert to meters
    to_meters = {
        "millimeters": 0.001,
        "centimeters": 0.01,
        "meters": 1,
        "kilometers": 1000,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34
    }
    
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    """Convert weight units to grams first, then to target unit"""
    # Convert to grams
    to_grams = {
        "milligrams": 0.001,
        "grams": 1,
        "kilograms": 1000,
        "ounces": 28.3495,
        "pounds": 453.592,
        "stones": 6350.29,
        "tons": 1000000
    }
    
    grams = value * to_grams[from_unit]
    result = grams / to_grams[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature units"""
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # Celsius
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        result = celsius * 9/5 + 32
    elif to_unit == "Kelvin":
        result = celsius + 273.15
    else:  # Celsius
        result = celsius
    
    return result

def convert_volume(value, from_unit, to_unit):
    """Convert volume units to liters first, then to target unit"""
    # Convert to liters
    to_liters = {
        "milliliters": 0.001,
        "liters": 1,
        "cubic_meters": 1000,
        "fluid_ounces": 0.0295735,
        "cups": 0.236588,
        "pints": 0.473176,
        "quarts": 0.946353,
        "gallons": 3.78541
    }
    
    liters = value * to_liters[from_unit]
    result = liters / to_liters[to_unit]
    return result

def main():
    st.set_page_config(
        page_title="Unit Converter",
        page_icon="🔄",
        layout="wide"
    )
    
    st.title("🔄 Universal Unit Converter")
    st.markdown("Convert between various units of measurement")
    
    # Create tabs for different conversion types
    tab1, tab2, tab3, tab4 = st.tabs(["📏 Length", "⚖️ Weight", "🌡️ Temperature", "🥤 Volume"])
    
    with tab1:
        st.header("Length Conversion")
        col1, col2 = st.columns(2)
        
        with col1:
            length_value = st.number_input("Enter value:", key="length_value", value=1.0)
            length_from = st.selectbox(
                "From:",
                ["millimeters", "centimeters", "meters", "kilometers", "inches", "feet", "yards", "miles"],
                key="length_from"
            )
        
        with col2:
            length_to = st.selectbox(
                "To:",
                ["millimeters", "centimeters", "meters", "kilometers", "inches", "feet", "yards", "miles"],
                index=2,
                key="length_to"
            )
        
        if st.button("Convert Length", key="convert_length"):
            result = convert_length(length_value, length_from, length_to)
            st.success(f"{length_value:,.6f} {length_from} = {result:,.6f} {length_to}")
    
    with tab2:
        st.header("Weight Conversion")
        col1, col2 = st.columns(2)
        
        with col1:
            weight_value = st.number_input("Enter value:", key="weight_value", value=1.0)
            weight_from = st.selectbox(
                "From:",
                ["milligrams", "grams", "kilograms", "ounces", "pounds", "stones", "tons"],
                key="weight_from"
            )
        
        with col2:
            weight_to = st.selectbox(
                "To:",
                ["milligrams", "grams", "kilograms", "ounces", "pounds", "stones", "tons"],
                index=2,
                key="weight_to"
            )
        
        if st.button("Convert Weight", key="convert_weight"):
            result = convert_weight(weight_value, weight_from, weight_to)
            st.success(f"{weight_value:,.6f} {weight_from} = {result:,.6f} {weight_to}")
    
    with tab3:
        st.header("Temperature Conversion")
        col1, col2 = st.columns(2)
        
        with col1:
            temp_value = st.number_input("Enter value:", key="temp_value", value=0.0)
            temp_from = st.selectbox(
                "From:",
                ["Celsius", "Fahrenheit", "Kelvin"],
                key="temp_from"
            )
        
        with col2:
            temp_to = st.selectbox(
                "To:",
                ["Celsius", "Fahrenheit", "Kelvin"],
                index=1,
                key="temp_to"
            )
        
        if st.button("Convert Temperature", key="convert_temp"):
            result = convert_temperature(temp_value, temp_from, temp_to)
            st.success(f"{temp_value:,.2f}° {temp_from} = {result:,.2f}° {temp_to}")
    
    with tab4:
        st.header("Volume Conversion")
        col1, col2 = st.columns(2)
        
        with col1:
            volume_value = st.number_input("Enter value:", key="volume_value", value=1.0)
            volume_from = st.selectbox(
                "From:",
                ["milliliters", "liters", "cubic_meters", "fluid_ounces", "cups", "pints", "quarts", "gallons"],
                key="volume_from"
            )
        
        with col2:
            volume_to = st.selectbox(
                "To:",
                ["milliliters", "liters", "cubic_meters", "fluid_ounces", "cups", "pints", "quarts", "gallons"],
                index=1,
                key="volume_to"
            )
        
        if st.button("Convert Volume", key="convert_volume"):
            result = convert_volume(volume_value, volume_from, volume_to)
            st.success(f"{volume_value:,.6f} {volume_from} = {result:,.6f} {volume_to}")
    
    # Add some helpful information
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.markdown("""
    - **Length**: Common conversions include meters to feet, kilometers to miles
    - **Weight**: Remember that 1 kg = 2.205 pounds approximately
    - **Temperature**: Water freezes at 0°C (32°F) and boils at 100°C (212°F)
    - **Volume**: 1 liter = 1000 milliliters = 0.264 gallons (US)
    """)

if __name__ == "__main__":
    main()