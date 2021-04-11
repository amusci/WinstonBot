module.exports = {
    name: 'hort',
    description: "Heads or Tails!",
    execute(message, args){

        x = (Math.floor.apply(Math.random() * 2) ==0);
        if (x >= 1)
        
        {

            message.channel.send('Heads!');

        }

        else

        {

            message.channel.send('Tails!');

        }

        

      




        

    }
}