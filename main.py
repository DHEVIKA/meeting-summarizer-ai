import gradio as gr
from transformers import pipeline

# Load summarization model (you can replace with any other free model)
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",  # lightweight and free
    device=-1  # CPU (use device=0 if GPU available)
)

def summarize_meeting(transcript):
    """
    Takes a meeting transcript string and returns a concise summary.
    """
    if not transcript.strip():
        return "Please enter the meeting transcript to summarize."
    
    try:
        # Summarize the transcript
        summary_list = summarizer(
            transcript,
            max_length=150,  # adjust max length
            min_length=40,   # adjust min length
            do_sample=False
        )
        return summary_list[0]['summary_text']
    except Exception as e:
        return f"Error summarizing transcript: {str(e)}"

# Create Gradio UI
iface = gr.Interface(
    fn=summarize_meeting,
    inputs=gr.Textbox(
        lines=10,
        placeholder="Paste your meeting transcript here..."
    ),
    outputs="text",
    title="Meeting Summarizer AI",
    description=(
        "Paste your meeting transcript and get a concise summary instantly!\n"
        "This AI helps you save time by extracting key points from meetings."
    ),
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()
