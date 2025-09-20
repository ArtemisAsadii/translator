from deep_translator import GoogleTranslator

print("ترجمه متن شما به فارسی")
text = input("لطفاً متن خود را وارد کنید: ")

try:
    translated = GoogleTranslator(source='auto', target='fa').translate(text)
    print("\nمتن ترجمه‌شده به فارسی:")
    print(translated)
except Exception as e:
    print(f"خطا در ترجمه: {e}")

