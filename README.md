# MultiLanguage Invoice Extractor

This Streamlit application is designed to extract information from invoices using Google Generative AI. Users can upload an image of an invoice and provide input prompts to generate information about the invoice content.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/multi-language-invoice-extractor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd multi-language-invoice-extractor
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google API key:
   - Create a `.env` file in the project root directory.
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app using the following command:
   ```bash
   streamlit run app.py
   ```

2. Access the application in your web browser by opening the URL provided in the terminal.

3. Upload an image of an invoice using the file uploader.

4. Enter input prompts in the provided text input field.

5. Click the "Tell me about the invoice" button to generate information about the invoice content.


## Credits

- [Streamlit](https://streamlit.io/) - Streamlit is an open-source app framework for Machine Learning and Data Science projects.
- [Google Generative AI](https://github.com/google-research/google-research/tree/master/generative_models_in_nlp) - Google Generative AI is a repository containing various generative models in NLP.


---
