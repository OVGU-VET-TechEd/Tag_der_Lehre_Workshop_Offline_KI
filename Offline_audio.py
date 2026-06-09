# Offline audio transcription with faster-whisper
# Runs 100% locally — no internet needed after first model download

from faster_whisper import WhisperModel
import sys, os

# --- Configuration ---
AUDIO_FILE = "Otto-von-Guericke-Universitat.mp3"    # change to your file
MODEL_SIZE = "small"         # tiny | base | small | medium | large-v3
LANGUAGE   = None            # None = auto-detect, or "de", "en", "fr" ...

# --- Load model (downloads once, cached in ~/.cache/huggingface/) ---
print(f"Loading {MODEL_SIZE} model ...")
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

# --- Transcribe ---
print(f"Transcribing {AUDIO_FILE} ...\n")
segments, info = model.transcribe(AUDIO_FILE, language=LANGUAGE)

print(f"Detected language: {info.language} (confidence: {info.language_probability:.0%})\n")
print("--- Transcript ---")

full_text = []
for seg in segments:
    line = f"[{seg.start:5.1f}s → {seg.end:5.1f}s]  {seg.text.strip()}"
    print(line)
    full_text.append(seg.text.strip())

# --- Save output ---
out_file = os.path.splitext(AUDIO_FILE)[0] + "_transcript.txt"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(full_text))
print(f"\n✓ Saved to {out_file}")