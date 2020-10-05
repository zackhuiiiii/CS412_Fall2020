

const del = str => {
    "Take a string as input and return the string with only char"
    let result = "";
    result = str.replace(/[^a-z]+/gi, "");
    return result;
}

const str_to_arr = str => {
    let result = [];
    for(let i = 0 ; i < str.length; i++){
        result.push(str[i]);
    }
    return result;
}
const arr_to_str = arr => {
    let result = "";
    for(let i = 0; i < arr.length; i++){
        result += arr[i];
    }
    return result;
}

const pr1 = s => {
    "Take a string as input and " +
    "return a new string that contains all of the letters in the original string in alphabetical order"
    let result = "";
    result = del(s);
    result = str_to_arr(result);
    result = result.sort();
    result = arr_to_str(result);
    return result;
}
module.exports = {del, arr_to_str, str_to_arr, pr1};
console.log(pr1("supercalifragilisticexpialidocious"));