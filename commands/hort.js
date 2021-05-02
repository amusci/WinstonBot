module.exports = {
    name: 'hort',
    description: "Heads or Tails!",
    execute(message, args){

        x = Math.floor(Math.random() * 2);
        if (x == 0)
        
        {

            message.channel.send('Heads!');

        }

        else

        {

            message.channel.send('Tails!');

        }
        // message.channel.send(x);

        

      




        

    }
}