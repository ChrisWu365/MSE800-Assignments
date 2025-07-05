import os
import PyPDF2
from openai import OpenAI
import tkinter as tk
from tkinter import filedialog

class RecruiterAdvisorBot:
    def __init__(self):
        # Initialize OpenAI client - you need to set OPENAI_API_KEY environment variable
        # or configure api_key directly: client = OpenAI(api_key="your-api-key")
        self.client = OpenAI()
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text content from a PDF file."""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return None
    
    def analyze_cv(self, cv_text):
        """Analyze CV text using OpenAI API."""
        try:
            prompt = """
            You are an expert recruiter and CV advisor. Please analyze the following CV and provide:
            
            1. A brief summary of the candidate's profile (experience, skills, education)
            2. Strengths of the CV
            3. Areas for improvement
            4. Specific recommendations to enhance the CV
            5. Suggestions for career development based on their profile
            
            Format your response in a structured way with clear headings and bullet points.
            """
            
            response = self.client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": cv_text}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error analyzing CV: {e}")
            return f"An error occurred during analysis: {str(e)}"
    
    def run_gui(self):
        """Run a simple GUI for the CV advisor bot."""
        root = tk.Tk()
        root.title("Recruiter Advisor Bot")
        root.geometry("900x700")
        root.configure(bg="#f5f5f5")
        
        # Style configurations
        title_font = ("Arial", 18, "bold")
        button_font = ("Arial", 12)
        text_font = ("Arial", 11)
        
        # Header
        header = tk.Label(root, text="CV Analysis & Recommendation Tool", 
                          font=title_font, bg="#f5f5f5", fg="#333333")
        header.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(root, text="Upload a CV in PDF format to receive professional analysis and recommendations.",
                               font=("Arial", 12), bg="#f5f5f5", fg="#555555")
        instructions.pack(pady=10)
        
        # Frame for file selection
        file_frame = tk.Frame(root, bg="#f5f5f5")
        file_frame.pack(pady=10)
        
        file_path_var = tk.StringVar()
        file_path_label = tk.Label(file_frame, textvariable=file_path_var, 
                                 width=50, bg="white", fg="#555555")
        file_path_label.pack(side=tk.LEFT, padx=5)
        
        def browse_file():
            filepath = filedialog.askopenfilename(
                filetypes=[("PDF Files", "*.pdf")])
            if filepath:
                file_path_var.set(filepath)
        
        browse_button = tk.Button(file_frame, text="Browse", command=browse_file,
                                 font=button_font, bg="#4a7abc", fg="white")
        browse_button.pack(side=tk.LEFT, padx=5)
        
        # Text area for results
        result_frame = tk.Frame(root, bg="#f5f5f5")
        result_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        result_text = tk.Text(result_frame, font=text_font, wrap=tk.WORD, 
                            bg="white", fg="#333333", padx=10, pady=10)
        result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(result_frame, command=result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        result_text.config(yscrollcommand=scrollbar.set)
        
        def analyze_cv_file():
            file_path = file_path_var.get()
            if not file_path:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Please select a PDF file first.")
                return
            
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Analyzing CV... Please wait.\n\n")
            root.update()
            
            # Extract text from PDF
            cv_text = self.extract_text_from_pdf(file_path)
            if not cv_text:
                result_text.insert(tk.END, "Failed to extract text from the PDF file.")
                return
            
            # Analyze CV
            analysis = self.analyze_cv(cv_text)
            
            # Display results
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, analysis)
        
        analyze_button = tk.Button(root, text="Analyze CV", command=analyze_cv_file,
                                 font=button_font, bg="#4CAF50", fg="white", padx=20, pady=10)
        analyze_button.pack(pady=15)
        
        # Footer
        footer = tk.Label(root, text="Powered by OpenAI GPT-4", 
                        font=("Arial", 8), bg="#f5f5f5", fg="#999999")
        footer.pack(pady=10)
        
        root.mainloop()

if __name__ == "__main__":
    bot = RecruiterAdvisorBot()
    bot.run_gui()