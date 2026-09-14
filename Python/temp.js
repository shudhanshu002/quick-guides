let obj = {
    name: "sk",
    age: 34,
    address: {
        pinCode: 78292,
        country: "India"
    }
}

let sh = {...obj}

sh.age = 56;

console.log(obj)