// ES 5
var colors = ['red', 'blue', 'green']

for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}

// ES 6+  forEach 끝나고 아무것도 return 하지 않는다.
function logger(x) {
    console.log(x)
}

colors.forEach(logger)  // colors에서 하나하나 빼서 logger에 인자로 넣음

colors.forEach(function (x) {
    console.log(x)
})


// ES 5
const numbers = [1, 2, 3];
const doubledNumbers = []

for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i] * 2);
}
console.log(doubledNumbers);


// ES6+
const tripleNumbers = numbers.map((number) => {
    return number * 3;
})
console.log(tripleNumbers);


// ES5
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegitable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vegitable'},
]

const fruits = [];
for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}
console.log(fruits);

// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';
})
console.log(vegetables);
