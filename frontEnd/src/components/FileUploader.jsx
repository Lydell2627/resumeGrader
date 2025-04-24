// frontend/src/components/FileUploader.jsx

import React, { useState, useEffect } from 'react';

export default function FileUploader() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [highScores, setHighScores] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchHighScores();
  }, []);

  const onChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError(null);
  };

  const fetchHighScores = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/high-scores');
      if (res.ok) setHighScores(await res.json());
    } catch (e) {
      console.error('Failed to fetch high scores:', e);
    }
  };

  const onSubmit = async () => {
    if (!file) return;
    const data = new FormData();
    data.append('file', file);

    try {
      const res = await fetch('http://localhost:8000/api/score', {
        method: 'POST',
        body: data,
      });
      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Upload failed');
      }
      const json = await res.json();
      setResult(json);
      fetchHighScores();
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  return (
    <div className="p-4 flex max-w-4xl mx-auto gap-6">
      {/* Uploader */}
      <div className="flex-1 bg-gray-100 p-4 rounded">
        <h2 className="text-xl font-semibold mb-2">Upload Resume</h2>
        <input type="file" accept=".pdf,.docx,.txt" onChange={onChange} className="mb-2" />
        <button onClick={onSubmit} className="px-4 py-2 bg-blue-500 text-white rounded">
          Grade Document
        </button>

        {error && <p className="text-red-500 mt-2">{error}</p>}
        {result && (
          <div className="mt-4">
            <p><strong>Score:</strong> {result.score}%</p>
            <p><strong>Keywords Found:</strong> {result.found_keywords.join(', ') || 'None'}</p>
          </div>
        )}
      </div>

      {/* High Scores Panel */}
      <div className="w-1/3 bg-white p-4 rounded shadow">
        <h3 className="text-lg font-semibold mb-2">High Scorers (&gt;60%)</h3>
        <ul className="list-disc list-inside">
          {highScores.length > 0
            ? highScores.map((item, i) => (
                <li key={i}>{item.filename} — {item.score}%</li>
              ))
            : <li>No high scores yet.</li>
          }
        </ul>
      </div>
    </div>
  );
}
