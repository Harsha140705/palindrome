from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Palindrome Checker Application</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 520px; margin: 40px auto; padding: 20px; }
    label { display: block; margin-top: 14px; }
    input { width: 100%; padding: 9px; box-sizing: border-box; margin-top: 4px; }
    button { margin-top: 18px; padding: 10px 18px; cursor: pointer; }
    #result { margin-top: 20px; padding: 12px; border: 1px solid #ccc; display: none; }
    #error { margin-top: 16px; color: red; }
  </style>
</head>
<body>
  <h2>Palindrome Checker Application</h2>
  <form id="palindromeForm">
    <label for="word">Enter a string *</label>
    <input id="word" name="word" type="text" placeholder="e.g., MADAM" required>

    <button id="checkBtn" type="submit">Check</button>
  </form>

  <p id="error" role="alert"></p>
  <div id="result" role="status">
    <h3>Result</h3>
    <p><strong>Input String:</strong> <span id="outWord"></span></p>
    <p><strong>Status:</strong> <span id="outStatus"></span></p>
  </div>

  <script>
    document.getElementById("palindromeForm").addEventListener("submit", async function (event) {
      event.preventDefault();
      const word = document.getElementById("word").value.trim();
      const errorEl = document.getElementById("error");
      const resultEl = document.getElementById("result");

      errorEl.textContent = "";
      resultEl.style.display = "none";

      if (!word) {
        errorEl.textContent = "Please enter a string.";
        return;
      }

      try {
        const response = await fetch(`/check?word=${encodeURIComponent(word)}`);
        const data = await response.json();

        if (!response.ok) {
          errorEl.textContent = data.error || "Failed to check palindrome.";
          return;
        }

        document.getElementById("outWord").textContent = data.word;
        const statusEl = document.getElementById("outStatus");
        if (data.palindrome) {
          statusEl.textContent = "The given string is a Palindrome";
          statusEl.style.color = "green";
        } else {
          statusEl.textContent = "The given string is Not a Palindrome";
          statusEl.style.color = "red";
        }
        resultEl.style.display = "block";
      } catch (err) {
        errorEl.textContent = "Error connecting to server.";
      }
    });
  </script>
</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML_PAGE)

@app.get("/check")
def check():
    word = request.args.get("word", "")
    normalized = word.lower()
    return jsonify({
        "word": word,
        "palindrome": normalized == normalized[::-1]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
