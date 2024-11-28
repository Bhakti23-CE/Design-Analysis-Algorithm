'''Problem Statement
Download books from the website in html, text, doc, and pdf format.
Compress these books using Hoffman coding technique. Find the compression ratio
'''
import heapq
from collections import defaultdict
import PyPDF2
from docx import Document
import requests
from bs4 import BeautifulSoup
import os


# Class to represent a node in the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


    # Compare nodes for the priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Count the frequency of each character in the text
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1


    # Create a priority queue (min-heap) from the frequencies
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)


    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)


        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)


    return heap[0]


# Function to generate the Huffman codes
def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}


    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)


    return codebook


# Function to compress the text using the generated Huffman codes
def compress(text, codebook):
    return ''.join(codebook[char] for char in text)


# Function to calculate the compression ratio
def calculate_compression_ratio(original_size, compressed_size):
    return original_size / compressed_size


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


# Function to extract text from a DOCX file
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to extract text from an HTML file
def extract_text_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
    return text


# Function to read a plain text file
def extract_text_from_txt(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Main function
def main():
        # Take input file name from user
        file_path = input("Enter the file path (html, txt, docx, or pdf): ").strip()


        # Check if the file exists
        if not os.path.exists(file_path):
            print("The file does not exist.")
            return
       
        if os.path.getsize(file_path) == 0:
            print("Error: The file is empty.")
            return


        # Step 1: Detect the file type by its extension and extract text accordingly
        file_extension = os.path.splitext(file_path)[1].lower()


        text = ""
        if file_extension == ".txt":
            text = extract_text_from_txt(file_path)
        elif file_extension == ".html":
            text = extract_text_from_html(file_path)
        elif file_extension == ".docx":
            text = extract_text_from_docx(file_path)
        elif file_extension == ".pdf":
            text = extract_text_from_pdf(file_path)
        else:
            print("Unsupported file format. Please provide a valid HTML, DOCX, TXT, or PDF file.")
            return
       


        # Step 2: Apply Huffman coding to compress the text
        root = build_huffman_tree(text)
        codebook = generate_codes(root)
        compressed_text = compress(text, codebook)


        # Step 3: Calculate the compression ratio
        original_size = len(text) * 8  # Original size in bits (assuming 8 bits per character)
        compressed_size = len(compressed_text)  # Compressed size in bits


        compression_ratio = calculate_compression_ratio(original_size, compressed_size)
        print(f"Original Size: {original_size} bits")
        print(f"Compressed Size: {compressed_size} bits")
        print(f"Compression Ratio: {compression_ratio:.2f}")


if __name__ == "__main__":
    main()
