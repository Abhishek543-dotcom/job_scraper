document.addEventListener('DOMContentLoaded', function() {
    // Example: Fetch job data from the backend and populate the table
    fetch('/api/jobs')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#jobTable tbody');
            data.forEach(job => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${job.title}</td>
                    <td>${job.company}</td>
                    <td>${job.location}</td>
                    <td>${job.match}</td>
                    <td><a href="${job.applicationLink}" target="_blank">Apply</a></td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching job data:', error));
});
