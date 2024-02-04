import streamlit as st
from midas.email_ingest import EmailIngest
from midas.agent import Midas
from tempfile import NamedTemporaryFile
from dotenv import load_dotenv
from datetime import datetime
import json
load_dotenv()

example_prompt = """
For each item that the buyer agreed to purchase, return the item name and item description directly under "description" without nesting them within another object, along with the quantity purchased, unit price in dollars, unit discount in dollars, and final total price per item calculated as (quantity * (unit price - unit discount)). Treat each SKU of the purchased item as a separate entry under "lineItems". 

Output the result in JSON format, ensuring all non-quantity and price-related details of the order and buyer are fully completed, including order number, contact phone, and shipping address. Follow the example structure below, but adjust it to directly include item name and description details under "description" for improved clarity and adherence to the expected output structure.

{
  "orderDetails": {
    "orderDate": "",
    "orderNum": "",
    "buyer": {
      "companyName": "",
      "pointOfContact": "",
      "contactEmail": "",
      "contactPhone": "",
      "shippingAddress": ""
    },
    "lineItems": [
      {
        "itemNumber": "",
        "description": {
          "itemName": "",
          "itemDescription": ""
        },
        "quantity": "",
        "unitPrice": "",
        "discount": "",
        "totalPrice": ""
      }
    ]
  }
}
"""

def parse_date(d):
    return datetime.strptime(d['metadata']['date'], '%m/%d/%Y, %H:%M')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Demo Application")

st.write("""
Try out our Midas agent for your sales emails and calls!
""")

st.subheader("0. Choose your favorite number between 10 and 100")
convo_id = st.text_input("My favorite number is...")

st.subheader("1. Upload one email PDF:")
uploaded_file = st.file_uploader("Sales email thread in PDF format", type='pdf')

st.subheader("2. Write initial prompt for what you want extracted and how it should be formatted:")
raw_prompt = st.text_area(
    f"""Example:
    {example_prompt}
    """
)

st.subheader("3. Add any other explicit requirements:")
criteria = st.text_area(
    """
    We will generate criteria for a good output based on your prompt in step 2, 
    but if you have anything you want to make sure is in there, please write it here in JSON.
    Example:
    [
        {"format": "the format should be outputted as a single 
                    string representing a JSON object containing no newlines"},
        {"no_markdown": "the output should not be in markdown, it should not contain backticks"}
    ]
    """
)

st.subheader("Optionally, load an existing agent and ignore above:")
loaded_agent = st.file_uploader("Agent JSON file", type='json')


midas_agent = None

agent_button = st.button("Create Agent")
if agent_button:
    with st.spinner('Creating...'):
        with NamedTemporaryFile(dir='.', suffix='.pdf') as f:
            if uploaded_file is not None:
                f.write(uploaded_file.getbuffer())
                file_path = f.name
                EmailIngest(file_path).run()
        midas_agent = Midas()
        midas_agent.set_objective(raw_prompt)
        midas_agent.add_criteria(json.loads(criteria))

load_button = st.button("Load Agent")
if load_button:
    with st.spinner('Loading agent...'):
        with NamedTemporaryFile(dir='.', suffix='.json') as f:
            if uploaded_file is not None:
                f.write(uploaded_file.getbuffer())
                file_path = f.name
                midas_agent = Midas()
                midas_agent.load(file_path)

if midas_agent is not None:
    train_button = st.button("Train Agent")
    if train_button:
        with st.spinner('Training...'):
            midas_agent.train(convo_ids=[convo_id], sort_key=parse_date)
            st.write("Training complete!")

    generate_button = st.button("Generate Output")
    if generate_button:
        with st.spinner("Generating..."):
            midas_agent.run(convo_id=convo_id, sort_key=parse_date)

    st.download_button('Download Agent', json.dumps(midas_agent.export_structure()), 'text/json')
