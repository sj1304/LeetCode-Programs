function isDigit(ch) {
    return ch >= '0' && ch <= '9';
}

function isAlpha(ch) {
    return /^[A-Za-z]$/.test(ch);
}

var myAtoi = function(s) {
    let l = "";  // use string instead of array
    let j = 0;

    for (let i = 0; i < s.length; i++) {
        let c = s[i];

        // Skip leading spaces
        if (c === " " && j === 0) continue;

        // Stop if alphabetic character
        if (isAlpha(c)) break;

        // Handle sign at the start
        if (j === 0 && (c === '-' || c === '+')) {
            l += c;
            j++;
            continue;
        }

        // Append digits
        if (isDigit(c)) {
            l += c;
            j++;
        } else {
            // Stop at first non-digit
            break;
        }
    }

    let num = Number(l);

    // If conversion fails, return 0
    if (isNaN(num)) return 0;

    // Clamp to 32-bit signed integer
    if (num < -2147483648) return -2147483648;
    if (num > 2147483647) return 2147483647;

    return num;
};
