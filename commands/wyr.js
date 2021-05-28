const { DiscordAPIError } = require("discord.js");

module.exports = {
    name: 'wyr',
    description: "would you rather",
    execute(message, args){


        const sideOne = '1️⃣';
        const sideTwo = '2️⃣';


        //needs improvments, would like to tally reactions then say who wins. Global Percentage


        const { options } = require('./wyroptions.json');

            
        var wyrsay = options[Math.floor(Math.random() * options.length)];
        
        message.channel.send(wyrsay).then(function(sentMessage) {
            sentMessage.react(sideOne).then(() => sentMessage.react(sideTwo)).catch(() => console.error('emoji failed to react.'));
        });


    }
}