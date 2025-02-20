document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            
            const formData = new FormData(registerForm);
            fetch("/register", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                window.location.href = "/leaderboard";
            })
            .catch(error => console.error("Error:", error));
        });
    }

    function fetchLeaderboard() {
        fetch("/leaderboard-data")
            .then(response => response.json())
            .then(data => {
                const leaderboardBody = document.getElementById("leaderboard-body");
                leaderboardBody.innerHTML = "";
                
                data.forEach((entry, index) => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${index + 1}</td>
                        <td>${entry.name}</td>
                        <td>${entry.escape_time} seconds</td>
                    `;
                    leaderboardBody.appendChild(row);
                });
            })
            .catch(error => console.error("Error fetching leaderboard:", error));
    }

    if (document.getElementById("leaderboard-body")) {
        fetchLeaderboard();
        setInterval(fetchLeaderboard, 30000); // Refresh leaderboard every 30s
    }
});