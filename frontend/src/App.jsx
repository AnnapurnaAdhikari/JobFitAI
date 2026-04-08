import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload-resume", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    console.log(data);
    setResult(data);
  };

  return (
  <div className="container">
    <h1 className="title"> AI Career Assistant</h1>

    <div className="upload-box">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload Resume</button>
    </div>

    {result && (
      <div className="card">
        <div className="section-title">Skills</div>
        <div className="skills">
          {result.skills?.join(", ")}
        </div>

        <div className="section-title">Recommended Jobs</div>

        {result.recommended_jobs?.map((job, index) => (
          <div className="job-card" key={index}>
            <h3>{job.job_title}</h3>
            <p><b>Match Score:</b> {job.match_score}</p>

            <p className="match">
              <b>Matched:</b> {job.matched_skills?.join(", ")}
            </p>

            <p className="missing">
              <b>Missing:</b> {job.missing_skills?.join(", ")}
            </p>

            <div className="section-title">Learning Roadmap</div>

            {job.learning_roadmap?.map((item, i) => (
              <div key={i} className="roadmap">
                <p><b>{item.skill}</b> ({item.category})</p>
                <ul>
                  {item.resources.map((r, j) => (
                    <li key={j}>{r}</li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        ))}
      </div>
    )}
  </div>
);
}
export default App;