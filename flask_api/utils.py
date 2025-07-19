from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
 
def calculate_cosine_similarity(text1, text2):
   vectorizer = TfidfVectorizer()
   tfidf = vectorizer.fit_transform([text1, text2])
   return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
 
def highlight_matching_text(text1, text2):
   matcher = difflib.SequenceMatcher(None, text1, text2)
   blocks = matcher.get_matching_blocks()
 
   def highlight(text, blocks, is_text1=True):
       result = []
       last = 0
       for block in blocks:
           start = block.a if is_text1 else block.b
           size = block.size
           if size == 0:
               continue
           result.append(text[last:start])
           result.append(f"<mark>{text[start:start+size]}</mark>")
           last = start + size
       result.append(text[last:])
       return ''.join(result)
 
   return highlight(text1, blocks, True), highlight(text2, blocks, False)