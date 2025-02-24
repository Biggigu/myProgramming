document.addEventListener("DOMContentLoaded", function () {
    let countdown;
    let timeLeft = 900; // 15 minutes in seconds
    let running = false;

    const timerDisplay = document.getElementById("timer-display");
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");

    function formatTime(seconds) {
        let minutes = Math.floor(seconds / 60);
        let secs = seconds % 60;
        return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
    }

    function updateTimer() {
        timerDisplay.textContent = formatTime(timeLeft);
    }

    startButton.addEventListener("click", function () {
        if (!running) {
            running = true;
            updateTimer();
            countdown = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateTimer();
                } else {
                    clearInterval(countdown);
                    alert("Time is up!");
                    running = false;
                }
            }, 1000);
        }
    });

    stopButton.addEventListener("click", function () {
        if (running) {
            running = false;
            clearInterval(countdown);
            alert("Timer stopped at: " + formatTime(timeLeft));
        }
    });

    updateTimer();
});

function stopTimer() {
    if (running) {
        running = false;
        clearInterval(countdown);
        
        let escapeTime = 900 - timeLeft; // Calculate time taken (15 min - remaining time)
        
        alert("Timer stopped at: " + formatTime(timeLeft));

        // Send the escape time to Flask
        fetch("/submit-time", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ escapeTime: escapeTime })
        })
        .then(response => response.json())
        .then(data => console.log(data)) // Logs response in browser console
        .catch(error => console.error("Error:", error));
    }
}
