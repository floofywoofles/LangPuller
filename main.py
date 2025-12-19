from gtts import gTTS
import orjson

if __name__ == "__main__":
    with open("./lang_numbers.json", "rb") as f:
        data = orjson.loads(f.read())

    # Access the Spanish dictionary
    spanish_words = data["languages"]["spanish"]

    # Or iterate through all Spanish words:
    for number, word in spanish_words.items():
        # Use Spanish (es) for natural and accurate pronunciation
        # Note: gTTS only supports 'es' (not regional variants like es-mx)
        tts = gTTS(word, lang='es')

        tts.save(f"./output/{number}.mp3")
