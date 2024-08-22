---
# LangToLang - Language Translator

![LangToLang]((https://github.com/user-attachments/assets/9ce11ae3-905f-45f9-b335-6df62beae0e0))

LangToLang is a language translation web application built using Streamlit and Hugging Face's MarianMT models. It allows users to translate text between various languages, including English, French, German,
Spanish, Italian, Russian, Chinese, Japanese, Korean, Arabic, and Urdu.

## Features
- **Translate Text:** Easily translate text between multiple languages.
- **Language Selection:** Choose source and target languages from a variety of options.
- **User-Friendly Interface:** A clean and intuitive interface built with Streamlit.
- **Real-Time Translation:** Get instant translation results as you type.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Hugging Face Models](#hugging-face-models)
- [Deployed Application](#deployed-application)
- [How to Achieve the Same](#how-to-achieve-the-same)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites
- Python 3.7+
- [Streamlit](https://streamlit.io)
- [PyTorch](https://pytorch.org/get-started/locally/) (for running Hugging Face models)
- Hugging Face Transformers library

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/[Your GitHub Username]/LangToLang.git
   cd LangToLang
   ```

2. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

## Usage
1. Select the source and target languages from the sidebar.
2. Enter the text you wish to translate in the text area.
3. Click the "Translate" button to see the translated text.

## Model Information
LangToLang uses Hugging Face's MarianMT models for translation. These models are pre-trained for various language pairs and provide accurate and efficient translations.

### Hugging Face Models Used
- [Helsinki-NLP/opus-mt-en-fr](https://huggingface.co/Helsinki-NLP/opus-mt-en-fr) (English to French)
- [Helsinki-NLP/opus-mt-en-de](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) (English to German)
- [Helsinki-NLP/opus-mt-en-es](https://huggingface.co/Helsinki-NLP/opus-mt-en-es) (English to Spanish)
- [Helsinki-NLP/opus-mt-en-it](https://huggingface.co/Helsinki-NLP/opus-mt-en-it) (English to Italian)
- [Helsinki-NLP/opus-mt-en-ru](https://huggingface.co/Helsinki-NLP/opus-mt-en-ru) (English to Russian)
- [Helsinki-NLP/opus-mt-en-zh](https://huggingface.co/Helsinki-NLP/opus-mt-en-zh) (English to Chinese)
- [Helsinki-NLP/opus-mt-en-ja](https://huggingface.co/Helsinki-NLP/opus-mt-en-ja) (English to Japanese)
- [Helsinki-NLP/opus-mt-en-ko](https://huggingface.co/Helsinki-NLP/opus-mt-en-ko) (English to Korean)
- [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) (English to Arabic)
- [Helsinki-NLP/opus-mt-en-ur](https://huggingface.co/Helsinki-NLP/opus-mt-en-ur) (English to Urdu)

## Deployed Application
Try out the live version of LangToLang:
- [LangToLang - Language Translator](https://huggingface.co/spaces/mohAhmad/LanguageTranslator)

## How to Achieve the Same

### Step-by-Step Guide
1. **Choose a Model on Hugging Face:**
   - Go to the [Hugging Face Model Hub](https://huggingface.co/models) and search for MarianMT models or any other translation models.

2. **Install the Required Libraries:**
   ```bash
   pip install torch transformers streamlit
   ```

3. **Load the Model and Tokenizer:**
   ```python
   from transformers import MarianMTModel, MarianTokenizer

   model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'  
   model = MarianMTModel.from_pretrained(model_name)
   tokenizer = MarianTokenizer.from_pretrained(model_name)
   ```

4. **Translate Text:**
   ```python
   text = "Hello, how are you?"
   translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
   translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
   print(translated_text)
   ```

5. **Integrate with Streamlit:**
   - Build a simple UI using Streamlit to take user input and display translations, as shown in the provided `LanguageTranslator.py` file.

6. **Deploy the Application:**
   - Deploy your application on platforms like [Streamlit Sharing](https://share.streamlit.io), [Heroku](https://www.heroku.com/), or [AWS](https://aws.amazon.com/).

## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Developer:** [Ahmad Raza]
- **LinkedIn:** [My LinkedIn Profile](https://www.linkedin.com/in/ahmadkhushi)
- **Email:** sktfscm21557034@gmail.com

---

This `README.md` provides an overview of the project, instructions for installation and usage, model information, and a guide for others to replicate the project using Hugging Face models. Make sure to update all the placeholder text with your actual information before uploading it to GitHub.
