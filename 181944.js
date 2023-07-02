//홀짝 구분하기
function solution(number) {
  if (number % 2 == 0) {
    return `${number} is even`;
  }
  return `${number} is odd`;
}

console.log(solution(101));
