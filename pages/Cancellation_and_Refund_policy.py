import streamlit as st
from st_pages import add_page_title, hide_pages


hide_pages(["Thank you"])


st.title("Cancellation and Refund Policy")

st.write(
    """
    At ContentCartHub, we strive to provide you with the best shopping experience. We understand that there may be instances where you need to cancel an order or request a refund. Please read our policy carefully to understand your rights and obligations.

    **Cancellation Policy:**

    1. **Cancellation before Shipping:** You can cancel your order any time before it has been shipped. To cancel, please contact our customer support team with your order details. We will initiate the cancellation process and refund the full amount to your original payment method.

    2. **Cancellation after Shipping:** Once your order has been shipped, it cannot be cancelled. In such cases, you can return the product(s) in accordance with our Returns Policy.

    **Refund Policy:**

    1. **Eligibility for Refund:** You may be eligible for a refund under the following circumstances:
        - You received the wrong item(s).
        - The item(s) received is damaged or defective.
        - You are not satisfied with the quality of the product(s) received.

    2. **Refund Process:** To request a refund, please contact our customer support team within [number of days] days of receiving the order. Provide us with your order details and the reason for the refund request. Our team will review your request and guide you through the return process, if applicable.

    3. **Refund Timeline:** Once your return is received and inspected, we will notify you of the approval or rejection of your refund. If approved, the refund will be processed within [number of days] days, and a credit will automatically be applied to your original method of payment.

    4. **Non-Refundable Items:** Certain items are not eligible for a refund, including:
        - Digital downloads or services.
        - Customized or personalized products.
        - Products marked as final sale or clearance.

    **Changes to Policy:**

    ContentCartHub reserves the right to modify or update this Cancellation and Refund Policy at any time. Any changes will be effective immediately upon posting on our website. We encourage you to review this policy periodically for any updates.

    Thank you for shopping at ContentCartHub!
    """
)
