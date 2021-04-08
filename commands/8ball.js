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
            "No.. Dear God No..",

            "Probably in three... No, four years.",
            "Just shut the fuck up.",
            " ..Really?",
            "Go with your gut.",
            "No Clue What To Do, Pal.",
            "After 31 years. sjsjsjsjsjjsjs",
            "It's not looking too good..",
            "Do anything but that.",
            "Thinking takes time, ask again later.",
            "I mean, if that's what you want to do..",
            "YES HOLY SHIT!",
            "You already know the answer is yes, why ask?",
            "You already know the answer is no, why ask?",
            "I ALREADY ANSWERED YES.",
            "I ALREADY ANSWERED NO."
            

            ];
        var magicsaying = sayings[Math.floor(Math.random() * sayings.length)];
        message.channel.send(magicsaying);

    }
}