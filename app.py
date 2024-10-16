import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def main():
    # Add a header with an icon
    st.markdown("# 🌡️ Temperature Converter")
    st.markdown("### Easily convert temperatures between Celsius and Fahrenheit.")

    # Add a sidebar for conversion selection
    st.sidebar.title("Settings")
    option = st.sidebar.radio("Select conversion type:",
                              ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    # Display an image based on the option selected
    if option == "Celsius to Fahrenheit":
        st.image("https://cdn-icons-png.flaticon.com/512/1684/1684424.png", width=100)
        celsius = st.slider("Select temperature in Celsius:", min_value=-100, max_value=100, value=0)
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"🌡️ {celsius}°C is equal to {fahrenheit:.2f}°F")
            st.balloons()  # Adds balloons animation for fun

    elif option == "Fahrenheit to Celsius":
        st.image("https://cdn-icons-png.flaticon.com/512/1684/1684426.png", width=100)
        fahrenheit = st.slider("Select temperature in Fahrenheit:", min_value=-200, max_value=200, value=32)
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"🌡️ {fahrenheit}°F is equal to {celsius:.2f}°C")
            st.snow()  # Adds a snow animation for winter-like effect

    # Add footer information
    st.sidebar.markdown("### Created with ❤️ using Streamlit")
    st.sidebar.markdown("[GitHub Repo](https://github.com) | [Contact Us](mailto:support@converter.com)")

if __name__ == "__main__":
    main()
