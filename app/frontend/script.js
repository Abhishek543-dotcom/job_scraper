document.addEventListener('DOMContentLoaded', () => {
    // Function to fetch and display job listings
    const fetchJobs = async () => {
        try {
            const response = await fetch('/api/jobs');
            const jobs = await response.json();

            const jobCardsContainer = document.getElementById('job-cards');
            jobCardsContainer.innerHTML = '';

            jobs.forEach(job => {
                const jobCard = document.createElement('div');
                jobCard.className = 'job-card';

                jobCard.innerHTML = `
                    <h3>${job.title}</h3>
                    <p><strong>Company:</strong> ${job.company}</p>
                    <p><strong>Location:</strong> ${job.location}</p>
                    <p><strong>Description:</strong> ${job.description}</p>
                    <p><strong>Requirements:</strong> ${job.requirements}</p>
                    <a href="${job.applicationLink}" target="_blank">Apply</a>
                `;

                jobCardsContainer.appendChild(jobCard);
            });
        } catch (error) {
            console.error('Error fetching jobs:', error);
        }
    };

    // Fetch jobs on page load
    fetchJobs();
});
