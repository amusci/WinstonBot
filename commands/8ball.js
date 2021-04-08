module.exports = {
    name: '8ball',
    description: "this is a magic eight ball!",
    execute(message, args){

        var sayings = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "Without a doubt.",
            "Yes – definitely.",
            "Can't believe you even asked that.",
            "Yes.",
            "No.",
            "No.. Dear God No.."

            ];
        var magicsaying = sayings[Math.floor(Math.random() * sayings.length)];
        message.channel.send(magicsaying);

    }
}