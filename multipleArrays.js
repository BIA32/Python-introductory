const multipleArrays = (a , b) => {
    let arr = [];
    let x = 1;
    for (let i = 1; i <= b; i++) {
        arr.push(a * x);
        x++;
    }
    return arr;
}

console.log(multipleArrays(1 , 5))