
/*
Todo:
Unprefixed Messages
Emoji Racing
Coach
wyr json stuff
truth or dare json stuff
refine heads or tails
*/


const Discord = require('discord.js');

const client = new Discord.Client();

const prefix ='-';

const token = 'ODI5NTQyNzY2OTcxMzIyNDI4.YG5p5w.zhdu3Eqy_IwagjvnnY0R092Rvp4'

const fs = require('fs');

client.commands = new Discord.Collection();

const commandfiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));

for(const file of commandfiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);
}


client.on('ready', () => {
    console.log('Winston at your service.');
    client.user.setPresence({
        status: 'online',
        activity: {
            name: "with Aidan's mom || -help for commands!",
            type: 'STREAMING',
            url: 'https://www.twitch.tv/antoniohatesyou'
        }
    })
});

    //prefix messages
    client.on('message', message =>{
        if(!message.content.startsWith(prefix) || message.author.bot) return;

        const args = message.content.slice(prefix.length).split(/ +/);
        const command = args.shift().toLowerCase();

        if(command === 'ping'){
            client.commands.get('ping').execute(message, args);
        }
        else if(command === 'youtube'){
            client.commands.get('youtube').execute(message, args);
        }
        else if(command === '8ball'){
            client.commands.get('8ball').execute(message, args);
        }
        else if(command === 'pun'){
            client.commands.get('pun').execute(message, args);
        }
        else if(command === 'help'){
            client.commands.get('help').execute(message, args);
        }
        else if(command === 'o7'){
            client.commands.get('o7').execute(message, args);
        }
        else if(command === 'wyr'){
            client.commands.get('wyr').execute(message, args);
        }
        else if(command === 'tord'){
            client.commands.get('tord').execute(message, args);
        }
        else if(command === 'hort'){
            client.commands.get('hort').execute(message, args);
        }

    });



//lastline
client.login(token);