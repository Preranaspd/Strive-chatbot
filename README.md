# Strive-chatbot

Chatbot app built with Streamlit and Groq.

## Run locally

1. Install dependencies:
	`pip install -r requirements.txt`
2. Set your API key:
	`GROQ_API_KEY=your_key_here`
3. Run the app:
	`python -m streamlit run app.py`

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Cloud, create a new app and set main file path to `app.py`.
3. In App Settings -> Secrets, add:

	```toml
	GROQ_API_KEY = "your_key_here"
	```

4. Deploy/reboot the app.
