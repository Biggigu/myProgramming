document.addEventListener("DOMContentLoaded", function () {
    let timer;
    let startTime;
    let elapsedTime = 0;
    let running = false;

    const timerDisplay = document.getElementById("timer-display");
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");
    const playerName = document.getElementById("player-name").value;
    const playerSurname = document.getElementById("player-surname").value;

    function formatTime(ms) {
        const totalSeconds = Math.floor(ms / 1000);
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    }

    function updateTimer() {
        const currentTime = Date.now();
        elapsedTime = currentTime - startTime;
        timerDisplay.textContent = formatTime(elapsedTime);
    }

    startButton.addEventListener("click", function () {
        if (!running) {
            running = true;
            startTime = Date.now() - elapsedTime;
            timer = setInterval(updateTimer, 1000);
        }
    });

    stopButton.addEventListener("click", function () {
        if (running) {
            running = false;
            clearInterval(timer);
            const escapeTime = formatTime(elapsedTime);
            fetch("/submit-time", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `name=${playerName}&surname=${playerSurname}&escape_time=${escapeTime}`
            })
            .then(response => response.json())
            .then(data => {
                alert("Time recorded: " + escapeTime);
                window.location.href = "/result";
            })
            .catch(error => console.error("Error submitting time:", error));
        }
    });
});
