from youtube_transcript_api import YouTubeTranscriptApi


video_id = 'xpVfcZ0ZcFM'
transcript = ""
resultlst = YouTubeTranscriptApi.get_transcript(video_id)
for sentenceSegment in resultlst:
  sentenceSegmentText = sentenceSegment['text'] + ' '
  transcript += sentenceSegmentText 

print(transcript)