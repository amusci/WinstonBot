module.exports = {
    name: 'pun',
    description: "funny puns",
    execute(message, args){

        var puns = [
            "How can you spot a nosy pepper? It gets Jalapeño business!",
            "I’m addicted to brake fluid, but it’s OK because I can stop at any time.",
            "What did the perscriptivist owl say? Whom whom.",
            "What do you call an alligator in a vest? An investigator.",
            "Did you know deer can jump higher than the average house? It’s because of their strong hind legs and the fact that the average house can’t jump.",
            "What did one eye say to the other? Just between you and me, something smells.",
            "What do you say to a Llama that loves picnicking? Alpaca lunch.",
            "A photon checks into a hotel. The front desk asks if it has any luggage. It replies “no, I’m traveling light”",
            "I can’t stand Russian dolls. They’re so full of themselves.",
            "Why did the hipster burn his mouth on pizza? Because he ate it before it was cool.",
            "Don’t ever believe an atom, they make up everything.",
            "Be kind to dentists. They have fillings too, you know.",

            "Did you hear about the silk worm race? It ended in a tie.",
            "I saw an ad for burial plots, but that’s the last thing I need.",
            "Clones are people two.",
            "I wanted to learn how to drive a stick shift, but I couldn’t find a manual.",
            "The machine at the coin factory just suddenly stopped working. It doesn’t make any cents.",
            "I tried to make a belt out of watches. It was a waist of time.",
            "Yesterday a clown held the door open for me. It was such a nice jester.",
            "Becoming a vegetarian is a big missed steak.",
            "Please don’t make my funeral too early. I’m not really a mourning person.",
            "Someone stole the police station’s toilets. They have nothing to go on.",
            "I quit my job at the donut factory. I was fed up with the hole business.",
            "I’m reading a book about anti-gravity. It’s impossible to put down.",

            ];
        var saypuns = puns[Math.floor(Math.random() * puns.length)];
        message.channel.send(saypuns);

    }
}