import streamlit as st

st.title("My demo website")

st.header("Smartphone Analysis Tool")

st.subheader("Smartphones from Apple")

# text
st.text("This is a sample text")

# markdown
st.markdown("## This is a markdown heading")

# mardown list
st.markdown("""
            **Brands**
            - Apple
            - Samsung
            - Oppo
            """)

# latex
st.latex(r"var = \sum_{i=1}^{n} \frac{(x-\mu)^2}{n-1}")

# code 
st.code("""
        def add(a:int, b:int):
            return a + b
        """, line_numbers=True)

# divider
st.divider()

st.markdown("""
            ```python
            def add(a:int, b:int):
                return a + b
            ```
            """)
# write
st.write("""
         ```python
         def add(a:int, b:int):
                return a + b
        ```
         """)