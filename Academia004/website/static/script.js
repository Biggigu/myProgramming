let countdown;
let timeLeft = 0;
let running = false;

const formatTime = (seconds) => {
    let minutes = Math.floor(seconds / 60);
    let secs = seconds % 60;
    return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
};

function updateTimer() {
    const timerDisplay = document.getElementById("timer-display");
    if (timerDisplay) {
        timerDisplay.value = formatTime(timeLeft);
        timerDisplay.setAttribute("data-time", timeLeft);
    }

    // Store value in localStorage so both screens can read the same
    localStorage.setItem("sharedTimeLeft", timeLeft);
}

function startTimer() {
    if (!running) {
        running = true;
        updateTimer();

        countdown = setInterval(() => {
            timeLeft++;
            updateTimer();
        }, 1000);
    }
}

function stopTimer() {
    running = false;
    clearInterval(countdown);
    localStorage.setItem("sharedTimeLeft", timeLeft);
    return timeLeft;
}

window.startTimer = startTimer;
window.stopTimer = stopTimer;

document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");
    const timerDisplay = document.getElementById("timer-display");

    // 🟢 Restore shared time on load (if exists)
    if (localStorage.getItem("sharedTimeLeft")) {
        timeLeft = parseInt(localStorage.getItem("sharedTimeLeft"));
        updateTimer();
    }

    // 🎮 Button Controls (Monitor 1 only)
    if (startButton) {
        startButton.addEventListener("click", () => {
            localStorage.setItem('displayMode', 'timer');
            startTimer();
        });
    }

    if (stopButton) {
        stopButton.addEventListener("click", () => {
            if (running) {
                const seconds = stopTimer();

                // Update screen mode
                localStorage.setItem("displayMode", "result");

                // Set value to raw seconds for backend
                if (timerDisplay) {
                    timerDisplay.value = seconds;
                }

                // Submit
                stopButton.closest("form").submit();
            }
        });
    }

    // For timerDisplay auto-start
    if (!startButton && !stopButton && localStorage.getItem('displayMode') === 'timer') {
        startTimer();
    }
});
