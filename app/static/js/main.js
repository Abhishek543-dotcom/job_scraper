document.addEventListener('DOMContentLoaded', function() {
    const highMatchJobsList = document.getElementById('high-match-jobs');
    const moderateMatchJobsList = document.getElementById('moderate-match-jobs');
    const lowMatchJobsList = document.getElementById('low-match-jobs');
    const errorMessage = document.getElementById('error-message');

    function fetchJobs() {
        fetch('/api/jobs')
            .then(response => response.json())
            .then(data => {
                displayJobs(data.highMatch, highMatchJobsList);
                displayJobs(data.moderateMatch, moderateMatchJobsList);
                displayJobs(data.lowMatch, lowMatchJobsList);
            })
            .catch(error => {
                errorMessage.textContent = 'Error fetching job data: ' + error;
            });
    }

    function displayJobs(jobs, listElement) {
        listElement.innerHTML = '';
        jobs.forEach(job => {
            const li = document.createElement('li');
            li.textContent = job.title + ' at ' + job.company + ' - ' + job.location;
            listElement.appendChild(li);
        });
    }

    fetchJobs();
});
</write_to_file>
