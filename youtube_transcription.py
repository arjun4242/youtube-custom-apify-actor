import json
from youtube_transcript_api import YouTubeTranscriptApi as yta

video_id = "EzY1E73EXAU"

transcription = yta.get_transcript(video_id)
transcript_paragraph = " ".join(value['text'] for value in transcription)
transcript_data = {'transcript': transcript_paragraph}
json_transcript = json.dumps(transcript_data, indent=2)

print(json_transcript)
