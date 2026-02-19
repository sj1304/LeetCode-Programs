/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  // step 1: convert array to number
  var num = BigInt(digits.join("")); // BigInt so large numbers are safe

  // step 2: add 1
  num = num + 1n;

  // step 3: convert back to list
  var str = num.toString();    // number → string
  var list = [];
  for (var i = 0; i < str.length; i++) {
    list.push(Number(str[i])); // add one element at a time
  }

  return list;
};

