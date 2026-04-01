import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_desc", jobDesc);

    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data.result);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Resume Scanner</h2>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br /><br />

      <textarea
        placeholder="Paste Job Description"
        rows="10"
        cols="50"
        onChange={(e) => setJobDesc(e.target.value)}
      />
      <br /><br />

      <button onClick={handleSubmit}>Analyze</button>

      <h3>Result:</h3>
      <pre>{result}</pre>
    </div>
  );
}

export default App;