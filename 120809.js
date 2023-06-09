// 배열두배만들기
function solution(numbers) {
  let array = numbers.map((x) => x * 2);
  return array;
}
console.log(solution([1, 2, 3, 4, 5, 6, 7]));

const solution = (numbers) => numbers.map((number) => number * 2);

// 다른사람풀이
function solution(numbers) {
  return numbers.reduce((a, b) => [...a, b * 2], []);
}
// reduce : 배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값);
