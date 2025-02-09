from flask import Flask, request, jsonify, send_file
import yt_dlp
import os

app = Flask(__name__)

# Create a downloads folder if not exists
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Test function to check if the backend is working
@app.route("/download", methods=["POST"])
def test_download():
    return jsonify({"message": "Your backend is working fine!"}), 200

# Main download function (currently disabled for testing)
# @app.route("/download", methods=["POST"])
# def download_audio():
#     data = request.get_json()
#     url = data.get("url")

#     if not url:
#         return jsonify({"error": "No URL provided"}), 400

#     try:
#         # Download audio using yt-dlp
#         ydl_opts = {
#             "format": "bestaudio/best",
#             "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
#             "postprocessors": [{
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",
#                 "preferredquality": "192",
#             }],
#             "postprocessor_args": [
#                 "-ac", "2",  # Ensure stereo output
#             ],
#             "prefer_ffmpeg": True,  # Use ffmpeg for audio extraction
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
        
#         # Ensure you're sending the correct file (which should now be mp3)
#         return send_file(filename, as_attachment=True)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
