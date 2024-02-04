# problem.py
import streamlit as st

def sales_order_use_case():
    st.title("Unlocking Possibilities with Midas: A Sample Use Case")

    st.markdown(
        """
        Sales representatives often face the challenge of managing numerous customer interactions, negotiating deals,
        and ensuring that sales orders accurately reflect the final agreed-upon details. This can be a daunting task,
        especially with a high volume of calls and email communications.

        **The Challenge:**
        
        - Keeping track of negotiated deals
        - Ensuring sales orders are up to date
        - Managing details like discounts, shipping, and order specifics
        """
    )

    st.image("frontend/images/negotiation.jpg", caption="Sales Negotiation Cycle", use_column_width=True)

    st.markdown(
        """
        **How Midas Solves It:**
        
        Midas revolutionizes the sales order creation process by seamlessly integrating with the sales representative's email 
        client and any audio transcript service they are already using. In doing so, there is no need for the sales rep to take 
        any manual action. Once a deal is agreed upon in their communications, LlamaLogic automatically converts call transcripts 
        and email communications into an up-to-date sales order, capturing the most recent agreed-upon details.

        This no-touch solution ensures that sales representatives can focus on building relationships and closing deals without 
        the added burden of manual data entry. Midas' automation not only saves valuable time but also guarantees the 
        creation of accurate and timely sales orders, enhancing efficiency in the sales workflow.

        **Benefits:**
        
        - Time savings for sales representatives
        - Accuracy in reflecting final negotiated details
        - Efficient management of sales orders
        """
    )

    st.image("frontend/images/chaos.jpg", caption="Creating Order from Chaos", use_column_width=True)

    st.markdown(
        """
        **Beyond Sales Orders:**
        
        While this use case focuses on sales order creation, it's just one example of how Midas can add significant
        value to businesses and individuals. Midas' capabilities extend across diverse scenarios, showcasing its
        versatility in structuring large amounts of data efficiently.

        This is just a glimpse into the potential applications of Midas. Imagine the possibilities and how it can
        revolutionize data structuring across various use cases!
        """
    )

if __name__ == "__main__":
    sales_order_use_case()
