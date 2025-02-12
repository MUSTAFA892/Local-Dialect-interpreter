document.addEventListener("DOMContentLoaded", function () {
    const inputText = document.getElementById("input-text");
    const outputText = document.getElementById("output-text");
    const translateBtn = document.getElementById("translate-btn");
    const startBtn = document.getElementById("start-btn");

    // Set up Speech Recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;  // Stop after a single phrase

    // Start Speech Recognition
    startBtn.addEventListener("click", () => {
        recognition.start();
        console.log("Listening...");
    });

    // Capture Speech Result
    recognition.onresult = function (event) {
        const speechText = event.results[0][0].transcript;
        inputText.value = speechText;  // Display recognized speech in the input text box
        console.log(`Recognized: ${speechText}`);
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
        alert("Speech recognition error. Try again.");
    };

    translateBtn.addEventListener("click", function () {
        const text = inputText.value.trim();

        if (!text) {
            alert("Please enter text to translate!");
            return;
        }

        fetch("http://127.0.0.1:8000/generate-response", {  /* Change the api url */ 
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: text })  // Send the text to the backend for translation
        })
        .then(response => response.json())
        .then(data => {
            const formattedResponse = data.response.replace(/(Language:.*?)(Figurative Meaning:)/, "$1\n$2");
            outputText.innerHTML = formattedResponse.replace(/\n/g, "<br>");
            console.log(data);  // Log the data for debugging
        })
        .catch(error => {
            console.error("Error:", error);
            outputText.textContent = "Translation failed. Try again.";
        });
    });
});
