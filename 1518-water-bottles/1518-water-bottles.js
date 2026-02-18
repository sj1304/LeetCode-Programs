/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    var rem=numBottles;
    var sum=numBottles;
    while(rem>=numExchange)
    {
      fullrem=parseInt(rem/numExchange);
      sum=sum+fullrem;
      rem=fullrem+parseInt(rem%numExchange);         
    }

    return (sum);
};