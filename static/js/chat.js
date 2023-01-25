function sendMessage(event) {
    var author = document.getElementById("name")
    var text = document.getElementById("message")
    fetch('/', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({ "author": author.value, "message": text.value })
        })

    ws.send(author.value, text.value)
    text.value = ''
    event.preventDefault()
}
