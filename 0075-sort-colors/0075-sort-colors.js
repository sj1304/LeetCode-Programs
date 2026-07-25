var sortColors = function(nums) {

    let zero = 0, one = 0, two = 0;

    for (let num of nums) {
        if (num === 0)
            zero++;
        else if (num === 1)
            one++;
        else
            two++;
    }

    let i = 0;

    while (zero--) nums[i++] = 0;
    while (one--) nums[i++] = 1;
    while (two--) nums[i++] = 2;
};