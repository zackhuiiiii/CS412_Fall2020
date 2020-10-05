const pr3 = (str, func) => {
    // let func1 = func(str);
    return func(str);
}

const func1 = str => {
    let arr = [];
    arr = str.split("c");
    for (let i = 1; i < arr.length; i++) {
        arr[i] = "c" + arr[i];
    }
    return arr;
}
const func2 = str => {
    let time = 0;
    let m = "";
    let ob = {
        originalString: str,
        modifiedString: str,
        numberReplaced: "",
        length: '0'
    }
    for (let j = 0; j < str.length; j++) {
        if (str[j] === 'a') {
            m += 'A';
            time++;
        } else {
            m += str[j];
        }
    }
    ob.modifiedString = m;
    ob.length = (m.length).toString(10);
    ob.numberReplaced = time.toString(10);

    return ob;
}

module.exports = {pr3, func1, func2};
console.log(pr3("supercalifragilisticexpialidocious", func1));
console.log(pr3("supercalifragilisticexpialidocious", func2));
