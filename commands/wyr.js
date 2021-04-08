module.exports = {
    name: 'wyr',
    description: "would you rather",
    execute(message, args){


        //needs improvments, would like to show reactions.
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
            "Would you rather know every human language, or be able to talk to animals?"

            ];
        var wyrsay = wyr[Math.floor(Math.random() * wyr.length)];
        message.channel.send(wyrsay);

    }
}