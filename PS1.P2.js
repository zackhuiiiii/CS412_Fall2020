const getOperator = str => {
    let left = parseInt(str[0], 10);
    let right = parseInt(str[2], 10);

    switch (str[1]) {

        case '+':
            return () => left + right;
            break;

        case '-':
            return () => left - right;
            break;

        case '*':
            return () => left * right;
            break;

        case '/':
            return () => left / right;
            break;
    }
}
module.exports = {getOperator};

const expression = '8+3';
let operator = getOperator(expression);
console.log(`${expression} = ${operator(expression)}`);