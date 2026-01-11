import gradio as gr

# ----------------------------------
# Core calculation logic
# ----------------------------------
def calculate_cgpa_percentage(marks):
    if not marks:
        return 0.0, 0.0

    # Convert marks to grade points
    grade_points = [(m / 10) for m in marks]

    # CGPA calculation
    cgpa = sum(grade_points) / len(grade_points)

    # Percentage calculation (standard conversion)
    percentage = cgpa * 9.5

    return round(cgpa, 2), round(percentage, 2)

# ----------------------------------
# Wrapper for Gradio input
# ----------------------------------
def process_marks(marks_text):
    try:
        # Parse comma-separated marks
        marks = [float(m.strip()) for m in marks_text.split(",") if m.strip()]

        # Validation
        for m in marks:
            if m < 0 or m > 100:
                return "Invalid marks entered", ""

        cgpa, percentage = calculate_cgpa_percentage(marks)

        return f"{cgpa}", f"{percentage}%"

    except Exception:
        return "Error", "Please enter valid numbers separated by commas"

# ----------------------------------
# Gradio UI
# ----------------------------------
interface = gr.Interface(
    fn=process_marks,
    inputs=gr.Textbox(
        label="Enter marks for each subject (comma separated)",
        placeholder="Example: 78, 85, 90, 72, 88"
    ),
    outputs=[
        gr.Textbox(label="CGPA"),
        gr.Textbox(label="Percentage")
    ],
    title="Engineering CGPA & Percentage Calculator",
    description="Calculate CGPA and percentage based on number of subjects and obtained marks"
)

# ----------------------------------
# Entry point (required)
# ----------------------------------
interface.launch()
