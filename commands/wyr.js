const { DiscordAPIError } = require("discord.js");

module.exports = {
    name: 'wyr',
    description: "would you rather",
    execute(message, args){


        const sideOne = '1️⃣';
        const sideTwo = '2️⃣';


        //needs improvments, would like to tally reactions then say who wins. Global Percentage
        var wyr = [
            "Would you rather lose the ability to read or lose the ability to speak?",
            "Would you rather be covered in fur or covered in scales?",
            "Would you rather have Addict or Nitro?",
            "Would you rather have Ultimato or ToaZuka",
            "Would you rather talk to Lightor for 5 minutes or COMMIT SUICIDE?",
            "Would you rather be the first person to explore a planet or be the inventor of a drug that cures a deadly disease?",
            "Would you rather have to use chopsticks every day for the rest of your life or use a fork?",
            "Would you rather be able to control animals or be able to see into the future?",
            "Would you rather never have a life without air conditioning or never be able to use deodorant?",
            "Would you rather talk with Sock humor or talk with D4C grammar?",
            "Would you rather have five half-sized clones of yourself or one full-sized clone of yourself?",
            "Would you rather have to shave your head or to have your nose pierced?",
            "Would you rather have Addict Racing or Glow Wasting?",
            "Would you rather sit on a cake and eat a dick, or sit on a dick and eat a cake?",
            "Would you rather know every human language, or be able to talk to animals?",

            "Would you rather go into the past and meet your ancestors or go into the future and meet your great-great grandchildren?",
            "Would you rather have more time or more money?",
            "Would you rather have Phy or Dex?",
            "Would you rather have gaspar or EnderNate?",
            "Would you rather talk to dawnii for 5 minutes or kill yourself?",
            "Would you rather listen to music from the 70’s or music from today?",
            "Would you rather go to a movie or to dinner alone?",
            "When you’re old, would you rather die before or after your spouse?",
            "Would you rather get rich through hard work or through winning the lottery?",
            "Would you rather talk with NFMMaster grammar or talk like JV?",
            "Would you rather be too busy or be bored?",
            "Would you rather live in Antarctica or the Sahara Dessert?",
            "Would you rather have Ziadd Racing or Dawnii Wasting?",
            "If you had to give up one thing for the rest of your life, would it be brushing your hair or brushing your teeth?",
            "Would you rather have a family of 12 children or never be able to have children at all?",


            ];

            
        var wyrsay = wyr[Math.floor(Math.random() * wyr.length)];
        
        message.channel.send(wyrsay).then(function(sentMessage) {
            sentMessage.react(sideOne).then(() => sentMessage.react(sideTwo)).catch(() => console.error('emoji failed to react.'));
        });


    }
}