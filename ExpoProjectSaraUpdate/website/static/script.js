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
        timerDisplay.value = formatTime(timeLeft);
        timerDisplay.setAttribute("data-time", timeLeft);
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

            // Update the input field before submitting
            timerDisplay.value = timeLeft;

            // Submit the form
            stopButton.closest("form").submit();
            }
        });
});
