var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";

    var start = strs[0];
    var newstr = "";
    var j = 0;

    while (j < start.length) {
        var f = 0;
        for (let temp of strs) {
            if (temp[j] !== start[j]) {
                f = 1;  // mismatch found
                break;
            }
        }

        if (f === 1) break;  // stop adding chars if mismatch
        newstr += start[j];   // add current character
        j += 1;
    }

    return newstr;
};
