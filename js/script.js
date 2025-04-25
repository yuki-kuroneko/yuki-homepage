function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const chatbox = document.getElementById("chatbox");

    if (userInput.trim() !== "") {
        const userMessage = document.createElement("p");
        userMessage.textContent = "User: " + userInput;
        chatbox.appendChild(userMessage);

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input: userInput })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement("p");
            botMessage.textContent = "Bot: " + data.response;
            chatbox.appendChild(botMessage);
        });

        document.getElementById("userInput").value = "";
        chatbox.scrollTop = chatbox.scrollHeight;
    }
}

