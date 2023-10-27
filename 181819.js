// 콜라츠 수열 만들기
function solution(n) {
  let answer = [n];
  while (n != 1) {
    n = n % 2 === 0 ? n / 2 : n * 3 + 1;
    answer.push(n);
  }
  return answer;
}

console.log(solution([10, 5, 16, 8, 4, 2, 1]));
