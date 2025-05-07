let countdown;
let timeLeft = 900;
let running = false;
let mirrorInterval;

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
    localStorage.setItem("sharedTimeLeft", timeLeft); // Save value globally
}

function startTimer() {
    if (!running) {
        running = true;
        localStorage.setItem("timerStopped", "false");
        countdown = setInterval(() => {
            timeLeft--;
            updateTimer();
        }, 1000);
    }

    // If this is Monitor 2, sync display every 0.5s
    if (window.location.pathname === "/timerDisplay") {
        mirrorInterval = setInterval(() => {
            const shared = parseInt(localStorage.getItem("sharedTimeLeft")) || 0;
            timeLeft = shared;
            updateTimer();

            // Check redirect trigger
            const mode = localStorage.getItem("displayMode");
            if (mode === "result") {
                clearInterval(mirrorInterval);
                window.location.href = "/result";
            }

            if (localStorage.getItem("timerStopped") === "true") {
                clearInterval(mirrorInterval);
            }
        }, 500);
    }
}

function stopTimer() {
    running = false;
    clearInterval(countdown);
    localStorage.setItem("timerStopped", "true");
    return timeLeft;
}

// GLOBAL
window.startTimer = startTimer;
window.stopTimer = stopTimer;

document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.getElementById("start-button");
    const stopButton = document.getElementById("stop-button");
    const hiddenField = document.getElementById("hidden-time-field");

    // Restore if available
    if (localStorage.getItem("sharedTimeLeft")) {
        timeLeft = parseInt(localStorage.getItem("sharedTimeLeft"));
        updateTimer();
    }

    // START
    if (startButton) {
        startButton.addEventListener("click", () => {
            timeLeft = 900;
            localStorage.setItem("sharedTimeLeft",900);
            localStorage.setItem("displayMode", "timer");
            localStorage.setItem("timerStopped", "false");
            startTimer();
        });
    }

    // STOP
    if (stopButton) {
        stopButton.addEventListener("click", () => {
            if (running) {
                const seconds = stopTimer();

                // Update values for next screens
                localStorage.setItem("displayMode", "result");

                // Hidden field for backend
                if (hiddenField) {
                    hiddenField.value = seconds;
                }

                stopButton.closest("form").submit();
            }
        });
    }

    // Monitor 2: autostart when on /timerDisplay
    if (!startButton && !stopButton && localStorage.getItem("displayMode") === "timer") {
        startTimer();
    }
});
