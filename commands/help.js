module.exports = {
    name: 'help',
    description: "shows all commands",
    execute(message, args){
        message.channel.send('commands are -8ball, -youtube, -pun, -wyr and -ping!');

    }
}