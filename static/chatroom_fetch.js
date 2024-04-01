var last_received_message_id = -1
const msgContainer = document.querySelector(".chatbot-messages")

async function fetchMessages() {
        console.log("requested_message")
        var request_data = JSON.stringify({
            "last_received_message_id": last_received_message_id
        })
        var response = await fetch('request_messages', {
            method: "FETCH",
            body: request_data,
            headers: {
                "Content-Type": "application/json"
            }
        })
        var response_data = await response.json()
        console.log(response_data)

        response_data.forEach((element) => {
            last_received_message_id = Math.max(last_received_message_id, element.id)

            var message = document.createElement("div")
            message.classList.add('bot-message')
            message.classList.add('message')
            msgContainer.appendChild(message)

            var user = document.createElement("div")
            user.classList.add('sender')
            user.textContent = element.username
            message.appendChild(user)

            var text = document.createElement("p")
            text.textContent = element.text
            message.appendChild(text)
        });

        msgContainer.scrollTop = msgContainer.scrollHeight
}


// Fetch messages every 1 second
setInterval(fetchMessages, 1000);