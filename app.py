import streamlit as st

def main():
    st.title("Semiconductor Physics App")
    st.header("Equations")
    st.write("Conductivity of a semiconductor is given by the formula:")
    st.latex(r'''
             \sigma = qn\mu_{e} + qp\mu_{p} = \frac{1}{\rho}
             ''')
    st.write("Conductivity as a function of scattering lifetime and effective mass:")
    st.latex(r'''
             \sigma = n q^{2} \frac{\tau_{e}}{m_{e}^{*}}
             ''')
    
    st.write("Example of a Taylor series:")
    st.latex(r'''
             e^x = \sum_{n=0}^\infty \frac{x^n}{n!}
             ''')

if __name__ == "__main__":
    main()
