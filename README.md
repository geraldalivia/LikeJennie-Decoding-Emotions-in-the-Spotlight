# LikeJennie: Decoding Emotions in the Spotlight

Welcome to **Like Jennie**, a sentiment analysis project that explores public opinions and emotions surrounding **Jennie Kim**, 
a member of the global K-pop group BLACKPINK. Using Natural Language Processing (NLP), I uncover how fans express admiration, 
critique, or emotional reactions across online platforms.

![Like Jennie](https://media1.tenor.com/m/Ah65OU_AfigAAAAd/like-jennie-jennie.gif)

---

## 💡 Project Overview

This project analyzes user-generated comments (e.g., from YouTube) related to Jennie to classify them as **positive**, 
**negative**, or **neutral**. The goal is to:

- Understand sentiment trends over time
- Visualize emotional responses to Jennie's music, performances, or news
- Build a reproducible NLP pipeline for social media text

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** - data manipulation
- **Scikit-learn** - machine learning models (SVM, RF, Logistic Regression)
- **NLTK** - text preprocessing (stopwords, tokenization)
- **Regex(re)** - text cleaning
- **Matplotlib / Seaborn** *(optional)* - evaluation visualization
- **Jupyter Notebook / Google Colab** - experiment execution

---

## ✨ Project Features

- Scraping YouTube comments (with YouTube API)
- Text preprocessing: lowercase, remove emoji, punctuation, URL, HTML entity, etc.
- Auto-labeling using sentiment keywords
- Machine Learning model with 3 training schemes:
  - SVM + TF-IDF (80/20)
  - Random Forest + TF-IDF (70/30)
  - Logistic Regression + TF-IDF (80/20)
- Accuracy evaluation with minimum 85%
- Inference: Test new comments and automatically predict their sentiment

---

## 📚 Dataset

- Dataset collected from comment sections of Jennie's music videos on YouTube (e.g., from Like JENNIE MV, Like Jennie - Coachella, and Like Jennie - NPOP Video)
- Important fields:
  - `author`: YouTube username
  - `text`: comment content
  - `label`: (positive/neutral/negative)

---

## 🧼 Data Preparation & Preprocessing

Preprocessing steps applied:

1. **Lowercasing** - converts all text to lowercase.
2. **Remove Emoji & Symbol** - cleaning unicode characters.
3. **Remove URL & HTML** - removes links and HTML code.
4. **Remove Mention/Hashtag** - removes `@user`, `#hashtag`.
5. **Remove Punctuation & Numbers** - leaves only the alphabet.
6. **Tokenization and Join** - reunite text.
7. **Auto-labeling** - sentiment labeling based on a list of `positive` & `negative` words.

### 🔤 Most Frequent Words
> *positive_words = [
    "love", "amazing", "awesome", "beautiful", "great", "good", "nice", "incredible",
    "cool", "sweet", "like", "wonderful", "perfect", "adorable", "favorite", "talented",
    "legend", "slay", "iconic", "queen", "happy", "enjoy", "best", "vibe", "fire", "insane"
]*

> *negative_words = [
    "hate", "bad", "worst", "boring", "ugly", "terrible", "awful", "annoying", "lame",
    "dislike", "cringe", "trash", "garbage", "weak", "overrated", "disappointed", "sucks",
    "poor", "mediocre", "meh", "waste", "stupid", "noisy", "fail"
]*

---

## 🧠 Model & Training Scheme

| Scheme |       Algorithm      | Feature Extraction | Split Data | Accuracy |
|--------|----------------------|--------------------|------------|----------|
|   1    | SVM                  |       TF-IDF       |    80/20   |  > 85%   |
|   2    | Random Forest        |   TF-IDF (bi-gram) |    70/30   |  > 85%   |
|   3    | Logistic Regression  |       TF-IDF       |    80/20   |  > 85%   |

> Catatan: Label awal diberikan secara otomatis menggunakan daftar kata positif dan negatif umum dalam bahasa Inggris.

---

## 🧪 Contoh Inference

```
komentar = "Thats, Special edition and your AI could'nt copy"
print(predict_sentiment(komentar))
# Output: positif
```

![Like Jennie](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXpha3JoMXAwcDBkcHJmeWoxd2ozbTFpdnR1Zmw5Y3AzMWx2aDBqeCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/smOK5xsYzZ28zhKR3h/200.webp)

---

💖 Credits

Made with passion for DEEPLEARNING and BLACKPINK 🎶
By Geralda Livia (alddar)
