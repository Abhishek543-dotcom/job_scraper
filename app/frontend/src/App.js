import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [jobs, setJobs] = useState([]);
  const [highMatchJobs, setHighMatchJobs] = useState([]);
  const [moderateMatchJobs, setModerateMatchJobs] = useState([]);
  const [lowMatchJobs, setLowMatchJobs] = useState([]);

  useEffect(() => {
    // Fetch job data from the backend API
    fetch('/api/jobs')
      .then(response => response.json())
      .then(data => {
        setJobs(data);
        // Match jobs with the user's resume
        const matchedJobs = matchJobsWithResume(data);
        setHighMatchJobs(matchedJobs.highMatch);
        setModerateMatchJobs(matchedJobs.moderateMatch);
        setLowMatchJobs(matchedJobs.lowMatch);
      })
      .catch(error => console.error('Error fetching jobs:', error));
  }, []);

  const matchJobsWithResume = (jobs) => {
    // Placeholder function for matching jobs with the user's resume
    // This will be replaced with actual NLP-based matching logic
    const highMatch = jobs.filter(job => job.matchScore >= 80);
    const moderateMatch = jobs.filter(job => job.matchScore >= 50 && job.matchScore < 80);
    const lowMatch = jobs.filter(job => job.matchScore < 50);

    return { highMatch, moderateMatch, lowMatch };
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Job Application Tracker</h1>
      </header>
      <main>
        <section>
          <h2>High Match Jobs</h2>
          <ul>
            {highMatchJobs.map(job => (
              <li key={job.id}>{job.title} at {job.company} - {job.location}</li>
            ))}
          </ul>
        </section>
        <section>
          <h2>Moderate Match Jobs</h2>
          <ul>
            {moderateMatchJobs.map(job => (
              <li key={job.id}>{job.title} at {job.company} - {job.location}</li>
            ))}
          </ul>
        </section>
        <section>
          <h2>Low Match Jobs</h2>
          <ul>
            {lowMatchJobs.map(job => (
              <li key={job.id}>{job.title} at {job.company} - {job.location}</li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  );
}

export default App;
