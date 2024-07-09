import matplotlib.pyplot as plt
import string
from collections import Counter
from PIL import Image
import pytesseract

# Function to extract text from resume image using OCR (Tesseract)
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return ""

# Function to clean and extract words from text
def extract_words(text):
    words = text.split()
    cleaned_words = [''.join(filter(str.isalpha, word.lower())) for word in words]
    cleaned_words = [word for word in cleaned_words if word]  # Remove empty strings
    return cleaned_words

# Function to count frequency of each word
def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts

# Function to plot word frequencies
def plot_word_frequencies(word_counts, num_words=10):
    top_words = dict(word_counts.most_common(num_words))
    words = list(top_words.keys())
    frequencies = list(top_words.values())

    plt.figure(figsize=(10, 6))  # Adjust the figure size as per your preference
    plt.bar(words, frequencies, color='skyblue')
    plt.title(f'Top {num_words} Most Frequent Words in Resume Text')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the process
def main():
    # Replace with your resume image path
    resume_image_path = 'path_to _your_resume_image'

    # Extract text from resume image
    resume_text = extract_text_from_image(resume_image_path)

    # Extract words and count frequency
    words = extract_words(resume_text)
    word_counts = count_word_frequency(words)

    # Plot word frequencies
    plot_word_frequencies(word_counts)

if __name__ == "__main__":
    main()
