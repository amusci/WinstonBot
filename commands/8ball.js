module.exports = {
    name: '8ball',
    description: "this is a magic eight ball!",
    execute(message, args){

        const { sayings } = require('./json/8ballsayings.json');


        
        var magicsaying = sayings[Math.floor(Math.random() * sayings.length)];
        
        console.log(sayings);
        message.channel.send(magicsaying);

    }
}