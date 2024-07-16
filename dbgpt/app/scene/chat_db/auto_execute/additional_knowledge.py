import re
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # 使用正则表达式保留英文和中文字符
    text = re.sub(r'[^\w\s]', '', text)
    # 分词处理，对中文和英文分别处理
    words = []
    for word in text.split():
        # 如果包含中文字符，则使用jieba进行分词
        if re.search(r'[\u4e00-\u9fff]', word):
            words.extend(jieba.cut(word))
        else:
            words.append(word.lower())  # 英文直接加入列表，并转为小写
    return ' '.join(words)

def calculate_relevance(input_info, file_path):
    # 读取文本文件并分割成段落
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    paragraphs = re.split(r'\n', text)
    
    # 预处理输入信息和段落
    preprocessed_input_info = preprocess_text(input_info)
    preprocessed_paragraphs = [preprocess_text(paragraph) for paragraph in paragraphs]
    # 计算TF-IDF向量
    vectorizer = TfidfVectorizer()
    input_vector = vectorizer.fit_transform([preprocessed_input_info])
    paragraph_vectors = vectorizer.transform(preprocessed_paragraphs)
    
    # 计算输入向量和段落向量之间的余弦相似度
    similarities = cosine_similarity(input_vector, paragraph_vectors)
    
    # 返回每个段落的相关性得分
    relevance_scores = similarities[0]
    return relevance_scores
# Example usage
def extract_additional_info(input_info, file_path):
    relevance_scores = calculate_relevance(input_info, file_path)
    max_score_index = relevance_scores.argmax()
    return max_score_index
