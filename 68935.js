// 3진법 뒤집기
function solution(n) {
  let answer = [];
  while (n != 0) {
    answer.push(n % 3);
    n = Math.floor(n / 3);
  }
  return parseInt(answer.join(""), 3);
}

console.log(solution(45));

// 다른사람풀이
function solution(n) {
  n = n.toString(3).split("").reverse().join("");
  return parseInt(n, 3);
}
