/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    let total = numBottles;
    let empty = numBottles;

    while (empty >= numExchange) {
        empty -= numExchange;   // use empties for 1 full
        numExchange++;          // cost increases
        total++;                // drink the new bottle
        empty++;                // that bottle becomes empty
    }

    return total;

};