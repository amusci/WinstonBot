module.exports = {
    name: 'help',
    description: "shows all commands",
    execute(message, args){
        message.channel.send('commands are tord, hort, wyr, 8ball, pun, youtube, ping, and help!');

    }
}