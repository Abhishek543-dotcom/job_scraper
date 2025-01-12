document.addEventListener('DOMContentLoaded', function() {
    // Example: Fetch job data from the backend and populate the dashboard
    fetch('/api/jobs')
        .then(response => response.json())
        .then(data => {
            const highMatchSection = document.getElementById('high-match');
            const moderateMatchSection = document.getElementById('moderate-match');
            const lowMatchSection = document.getElementById('low-match');

            data.forEach(job => {
                const li = document.createElement('li');
                li.textContent = `${job.title} at ${job.company} - ${job.location}`;
                if (job.match === 'high') {
                    highMatchSection.appendChild(li);
                } else if (job.match === 'moderate') {
                    moderateMatchSection.appendChild(li);
                } else if (job.match === 'low') {
                    lowMatchSection.appendChild(li);
                }
            });
        })
        .catch(error => console.error('Error fetching job data:', error));
});
