from flask import Flask, render_template, request
app = Flask(__name__)
eng ={
    # Basic emotions
    "love": "❤️",
    "like": "👍",
    "hate": "💀",
    "funny": "😆",
    "sad": "😭",
    "angry": "😡",
    "bored": "🥱",
    "asleep": "😴",
    "excited": "🤩",
    "surprised": "😲",
    "cry": "😢",
    # Food
    "pizza": "🍕",
    "burger": "🍔",
    "fries": "🍟",
    "coffee": "☕",
    "tea": "🫖",
    "cake": "🍰",
    "chocolate": "🍫",
    "icecream": "🍦",
    # Animals
    "cat": "🐱",
    "dog": "🐶",
    "monkey": "🙈",
    "panda": "🐼",
    "turtle": "🐢",
    "fish": "🐠",
    # People & reactions
    "me": "🙋",
    "you": "👉",
    "they": "👥",
    "friend": "🫶",
    "bro": "👊",
    "girl": "💁‍♀️",
    "boy": "🧑",
    "teacher": "👩‍🏫",
    "student": "🎓",
    # Objects & fun stuff
    "computer": "💻",
    "phone": "📱",
    "game": "🎮",
    "music": "🎶",
    "dance": "💃",
    "sleep": "🛌",
    "study": "📚",
    "money": "💸",
    "fire": "🔥",
    "party": "🎉",
    # Random funny slang
    "wow": "🤯",
    "oops": "😅",
    "cool": "😎",
    "ok": "👌",
    "no": "🚫",
    "yes": "✅",
    "help": "🆘",
    "run": "🏃‍♂️",
    "lol": "😂",
    "bruh": "🤦‍♂️",
    "omg": "😱",
    "ghost": "👻",
    "sus": "🕵️",
}
viet={
    "yêu": "❤️",
    "thích": "👍",
    "ghét": "💀",
    "buồn cười": "😆",
    "buồn": "😭",
    "tức giận": "😡",
    "chán": "🥱",
    "đang ngủ": "😴",
    "hào hứng": "🤩",
    "ngạc nhiên": "😲",
    "khóc": "😢",
    # Food
    "pizza": "🍕",
    "burger": "🍔",
    "khoai tây chiên": "🍟",
    "cà phê": "☕",
    "trà": "🫖",
    "bánh": "🍰",
    "socola": "🍫",
    "kem": "🍦",
    # Animals
    "mèo": "🐱",
    "chó": "🐶",
    "khỉ": "🙈",
    "gấu trúc": "🐼",
    "rùa": "🐢",
    "cá": "🐠",
    # People & reactions
    "tôi": "🙋",
    "bạn": "👉",
    "họ": "👥",
    "bạn": "🫶",
    "bro": "👊",
    "con gái": "💁‍♀️",
    "con trai": "🧑",
    "giáo viên": "👩‍🏫",
    "học sinh": "🎓",
    # Objects & fun stuff
    "máy tính": "💻",
    "điện thoại": "📱",
    "game": "🎮",
    "nhạc": "🎶",
    "nhảy": "💃",
    "ngủ": "🛌",
    "học": "📚",
    "tiền": "💸",
    "cháy": "🔥",
    "party": "🎉",
    # Random funny slang
    "wow": "🤯",
    "oops": "😅",
    "cool": "😎",
    "ok": "👌",
    "no": "🚫",
    "yes": "✅",
    "cứu": "🆘",
    "chạy": "🏃‍♂️",
    "lol": "😂",
    "bruh": "🤦‍♂️",
    "omg": "😱",
    "ma": "👻",
    "sus": "🕵️",
}
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        lang = request.form.get("lang")
        sentence = request.form.get("sentence", "")
        string = sentence.lower().split()
        if lang.lower() == "english":
            a=-1
            for s in string:
                a = a+1
                if a == len(string):
                    break
                for d in eng: 
                    if s == d:
                        string[a]=eng[d]
                    else:
                        continue
        elif lang.lower() == "vietnamese":
            b=-1
            for s in string:
                b=b+1
                if b == len(string):
                    break
                for d in eng:
                    if s == d:
                        string[b] = viet[d]
                    else:
                        continue
        output = " ".join(string)
    return render_template("index.html", result=output)
if __name__ == "__main__":
    app.run(debug=True)
