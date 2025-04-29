# ResumeGrader

**ResumeGrader** is a full-stack web application that automates the evaluation and scoring of resumes. By parsing uploaded documents, matching keywords, and analyzing structure, it provides job seekers with instant feedback to optimize their resumes for Applicant Tracking Systems (ATS) and recruiters.

---

## 📋 Features

- **Document Upload**: Accepts PDF and Word (`.docx`) files.  
- **Text Extraction**: Parses and extracts text content from resumes.  
- **Keyword Analysis**: Compares resume content against a configurable set of keywords.  
- **Scoring Engine**: Assigns a numerical score based on keyword matches, layout, and section completeness.  
- **Dashboard**: Displays a list of graded resumes with name, score, and detailed breakdown.  
- **Responsive UI**: Built with React for a modern, interactive experience.

---

## 🛠️ Tech Stack

- **Frontend**: React, JavaScript, HTML5, CSS3  
- **Backend**: FastAPI (Python), JavaScript  
- **Parsing**: `python-docx`, `pdfminer.six` (or similar libraries)  
- **Build Tools**: Node.js, npm, Uvicorn  

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v14+)
- **npm** (v6+)
- **Python** (v3.8+)
- **pip**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Lydell2627/resumeGrader.git
   cd resumeGrader
   ```

2. **Setup Backend**
   ```bash
   cd backEnd
   pip install -r requirements.txt        # Install Python dependencies
   uvicorn app.main:app --reload           # Run FastAPI server on http://127.0.0.1:8000
   ```

3. **Setup Frontend**
   ```bash
   cd ../frontEnd
   npm install                             # Install Node packages
   npm start                               # Run React dev server on http://localhost:3000
   ```

4. **Access the App**
   - Open your browser and navigate to `http://localhost:3000`.
   - Upload a resume file to see instant grading!

---

## 📁 Project Structure

```
resumeGrader/
├── backEnd/           # FastAPI backend project
│   ├── app/           # Main application code
│   ├── requirements.txt
│   └── ...
└── frontEnd/          # React frontend project
    ├── src/           # React components and assets
    ├── public/
    └── package.json
```

---

## 🎯 Future Improvements

- 🎓 **AI-Powered Suggestions**: Integrate NLP models to offer personalized improvement tips.  
- 💾 **Database Integration**: Store uploaded resumes and scores in MongoDB or PostgreSQL.  
- 📊 **Analytics**: Provide aggregate statistics and visualizations of resume performance.  
- 📝 **More Formats**: Support text, RTF, and other document types.  

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/YourFeature`).  
3. Commit your changes (`git commit -m 'Add awesome feature'`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a Pull Request and describe your changes.


---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

> Built with ❤️ and curiosity. Keep your resumes sharp and stand out!
