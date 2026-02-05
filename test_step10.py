from utils.language import detect_language, normalize_text

english_text = "This Agreement shall be governed by the laws of India."
hindi_text = "यह समझौता भारत के कानूनों द्वारा शासित होगा।"

print(detect_language(english_text))
print(detect_language(hindi_text))
