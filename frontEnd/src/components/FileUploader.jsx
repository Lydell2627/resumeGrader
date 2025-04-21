import React, { useState } from 'react';

export default function FileUploader() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const onChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError(null);
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
        setError(err.detail || 'An error occurred.');
        return;
      }

      const json = await res.json();
      setResult(json);
    } catch (err) {
      setError('Failed to connect to backend.');
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto text-white">
      <input type="file" accept=".pdf,.docx" onChange={onChange} className="mb-2" />
      <button onClick={onSubmit} className="px-4 py-2 bg-blue-500 text-white rounded">
        Grade Document
      </button>

      {error && (
        <div className="mt-4 text-red-500">
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div className="mt-4 bg-gray-800 p-4 rounded">
          <p><strong>Score:</strong> {result.score}%</p>
          <p><strong>Keywords Found:</strong> {result.found_keywords.join(', ') || 'None'}</p>
        </div>
      )}
    </div>
  );
}
