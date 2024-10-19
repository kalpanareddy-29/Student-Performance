let students = []; // Initialize an empty array to hold student data

// Load CSV data
function loadCSV() {
    Papa.parse('C:\Users\kalpa\Desktop\Hackathon\data.csv', {
        download: true,
        header: true,
        complete: function(results) {
            students = results.data; // Store parsed data in the students array
        },
        error: function(err) {
            console.error("Error loading CSV file: ", err);
        }
    });
}

// Function to display student information based on ID
function displayStudentInfo() {
    const studentId = document.getElementById('studentId').value;
    const studentDetailsDiv = document.getElementById('studentDetails');

    // Clear previous details
    studentDetailsDiv.innerHTML = '';

    // Find the student with the entered ID
    const student = students.find(s => s.id === studentId);

    if (student) {
        // If student found, display their information
        studentDetailsDiv.innerHTML = `
            <h3>Student Details</h3>
            <p><strong>ID Number:</strong> ${student.id}</p>
            <p><strong>Student Name:</strong> ${student.student_name}</p>
            <p><strong>Department:</strong> ${student.department}</p>
            <p><strong>Year:</strong> ${student.year}</p>
            <p><strong>Percentage:</strong> ${student.percentage}%</p>
            <p><strong>Local Hackathons Participated:</strong> ${student.local_hackathons_participated}</p>
            <p><strong>Local Hackathons Won:</strong> ${student.local_hackathons_won}</p>
            <p><strong>Paper Presentations:</strong> ${student.paper_presentations}</p>
            <p><strong>National Level Hackathons Participated:</strong> ${student.national_hackathons_participated}</p>
            <p><strong>National Level Hackathons Won:</strong> ${student.national_hackathons_won}</p>
            <p><strong>Certifications:</strong> ${student.certifications}</p>
            <p><strong>R&D Work Rating:</strong> ${student.rnd_work_rating}</p>
            <p><strong>Social Interactions:</strong> ${student.social_interactions}</p>
            <p><strong>Paper Publications:</strong> ${student.paper_publications}</p>
        `;
    } else {
        // If no student found, display a message
        studentDetailsDiv.innerHTML = '<p style="color:red;">No student found with this ID.</p>';
    }
}

// Load CSV data when the window is loaded
window.onload = loadCSV;
