// Church numerals
const ZERO = f => x => x;
const ONE = f => x => f(x);
const TWO = f => x => f(f(x));
const THREE = f => x => f(f(f(x)));

const SUCC = n => f => x => f(n(f)(x));

// Esempio
const inc = x => x + 1;
console.log(THREE(inc)(0)); // 3
console.log(SUCC(THREE)(inc)(0)); // 4
