async function sendMessage() {

    let inputField = document.getElementById("user-input");

    let message = inputField.value;

    if (message.trim() === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    // USER MESSAGE
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    inputField.value = "";

    // SEND TO FLASK
    let response = await fetch("/get_response", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    // BOT MESSAGE
    chatBox.innerHTML += `
        <div class="bot-message">
            ${data.response}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    // VOICE
    if ('speechSynthesis' in window) {

        let speech = new SpeechSynthesisUtterance(data.response);

        speech.lang = "en-US";

        speech.volume = 1;

        speech.rate = 1;

        speech.pitch = 1;

        window.speechSynthesis.speak(speech);
    }
}