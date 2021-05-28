module.exports = {
    name: 'socials',
    description: "sends social link",
    execute(message, args){
        message.channel.send('https://www.youtube.com/channel/UCj0_shizWwVL00J8GiUTE2g');
        message.channel.send('https://www.twitch.tv/antoniohatesyou');
        message.channel.send('https://github.com/antoniomusciano');
    }
}