# Twitter Sentiment Analysis Using Recurrent Neural Networks (RNN)
working link:- https://twitter-sentiment-analysis-using-rnn-aeah4bktvrk23xzo4ncmxd.streamlit.app/
## Project Overview

This project implements a **Twitter Sentiment Analysis system using a Recurrent Neural Network (RNN)** with TensorFlow and Keras. The model analyzes tweets and classifies their sentiment into three categories: Positive, Negative, and Neutral.

The primary objective is to leverage Natural Language Processing (NLP) techniques and deep learning to understand textual data and predict the underlying sentiment expressed in tweets.

## Objectives

- Perform sentiment classification on Twitter text data.
- Apply NLP preprocessing techniques to clean and prepare tweets.
- Convert textual data into numerical sequences using tokenization.
- Apply sequence padding to ensure uniform input dimensions.
- Build and train a Simple Recurrent Neural Network (SimpleRNN).
- Evaluate model performance on validation data.
- Develop a prediction pipeline for classifying unseen tweets.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| Architecture | SimpleRNN |
| NLP | Tokenization, Text Preprocessing, Padding |
| Data Processing | Pandas, NumPy |
| Model Serialization | HDF5 (.h5), Pickle |
| Development | Jupyter Notebook, VS Code |

## Dataset

The project uses the Twitter Entity Sentiment Analysis dataset.

The dataset contains tweets associated with different entities and their corresponding sentiment labels.

**Sentiment Categories:**

- Positive
- Negative
- Neutral
- Irrelevant (present in the original dataset, if retained during preprocessing)

**Dataset Files:**
link :- https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis
- `twitter_training.csv` – Training dataset.
- `twitter_validation.csv` – Validation dataset.

## Project Workflow

The project follows a standard NLP and deep learning pipeline:

1. **Data Loading:** Import training and validation datasets using Pandas.
2. **Exploratory Data Analysis:** Examine data distribution, missing values, and sentiment categories.
3. **Data Preprocessing:** Clean tweets by handling missing values, special characters, and unnecessary text.
4. **Label Encoding:** Convert sentiment labels into numerical representations using LabelEncoder.
5. **Text Tokenization:** Convert tweets into integer sequences using the Keras Tokenizer.
6. **Sequence Padding:** Apply padding to ensure all input sequences have equal length.
7. **Model Development:** Build a SimpleRNN-based neural network.
8. **Model Training:** Train the network using the prepared training sequences.
9. **Model Evaluation:** Evaluate the model using validation data.
10. **Sentiment Prediction:** Predict the sentiment of previously unseen tweets.

## Model Architecture

The project uses a Simple Recurrent Neural Network (SimpleRNN), which is designed to process sequential data.

**Architecture components:**

- **Embedding Layer:** Converts integer-encoded words into dense vector representations.
- **SimpleRNN Layer:** Learns sequential patterns and contextual information from tweet sequences.
- **Dense Layer:** Performs feature transformation before classification.
- **Output Layer:** Predicts the sentiment category.

The model uses a multi-class classification approach.

## Project Structure

```text
RNN project/
│
├── app.py
├── project.ipynb
├── model.h5
├── tokenizer.pkl
├── requirements.txt
├── README.md
│
├── twitter_training.csv
├── twitter_validation.csv
│
├── .gitignore
└── .gitattributes
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd "RNN project"
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / WSL:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Jupyter Notebook

```bash
jupyter notebook
```

Open `project.ipynb` and execute the notebook cells.

### Run the prediction application

```bash
python app.py
```

## Model Files

The trained model and tokenizer are saved separately for reuse during inference.

| File | Description |
|---|---|
| `model.h5` | Trained TensorFlow/Keras RNN model |
| `tokenizer.pkl` | Fitted text tokenizer used for sequence conversion |

The tokenizer must be reused during prediction to maintain consistency with the training vocabulary.
## Model Architecture and Implementation

This project implements a **Twitter Sentiment Analysis model using a Recurrent Neural Network (RNN)** with a SimpleRNN architecture built using TensorFlow and Keras.

The model is designed to perform **three-class sentiment classification**, categorizing tweets into:

- **Negative**
- **Neutral**
- **Positive**

### Architecture Overview

The model uses a many-to-one RNN architecture, where a sequence of input tokens is processed recurrently, and the final representation is used to predict the overall sentiment of the tweet.

The major components include:

1. **Embedding Layer:** Converts integer-encoded words into dense, trainable vector representations, allowing the model to learn semantic patterns from textual data.
2. **SimpleRNN Layer:** Processes the embedded sequence sequentially and maintains a hidden state to capture contextual information across the tweet.
3. **Dense Output Layer:** Produces class scores for the three sentiment categories.
4. **Softmax Activation:** Converts the output scores into probability distributions across Negative, Neutral, and Positive classes.

### Model Performance

The model was evaluated on a test dataset containing **11,497 tweets** and achieved an overall accuracy of **90%**.

| Metric | Score |
|---|---:|
| Test Accuracy | 90% |
| Macro F1-Score | 0.90 |
| Weighted F1-Score | 0.90 |

The classification results demonstrate consistent performance across all three sentiment categories, with F1-scores ranging from 0.89 to 0.91.

### Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

### Key Learning Outcomes

- Understanding recurrent neural network architectures.
- Implementing many-to-one sequence classification.
- Text preprocessing and tokenization.
- Word embeddings and sequential feature learning.
- Multiclass sentiment classification.
- Model evaluation using precision, recall, F1-score, and accuracy.
- GPU-accelerated model training using TensorFlow.## Classification Report

| Class        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| Negative     | 0.92      | 0.91   | 0.91     | 4,248   |
| Neutral      | 0.89      | 0.89   | 0.89     | 3,422   |
| Positive     | 0.90      | 0.91   | 0.90     | 3,827   |
| **Accuracy** |           |        | **0.90** | **11,497** |
| **Macro Avg** | **0.90** | **0.90** | **0.90** | **11,497** |
| **Weighted Avg** | **0.90** | **0.90** | **0.90** | **11,497** |


## Future Improvements

- Experiment with LSTM and GRU architectures.
- Implement Bidirectional RNN layers.
- Apply Word2Vec or GloVe embeddings.
- Experiment with dropout and recurrent dropout to reduce overfitting.
- Perform hyperparameter optimization.
- Evaluate performance using precision, recall, F1-score, and confusion matrix.
- Deploy the model using Streamlit or Flask.
- Explore Transformer-based architectures such as BERT.

## Learning Outcomes

Through this project, the following concepts were explored:

- Natural Language Processing fundamentals.
- Text preprocessing and tokenization.
- Sequence-based deep learning.
- Recurrent Neural Network architecture.
- Embedding representations.
- Multi-class sentiment classification.
- Model training, evaluation, and inference.

## Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/bhaskar0125)

---

*This project was developed for learning and experimentation with Natural Language Processing and Deep Learning using Recurrent Neural Networks.*
