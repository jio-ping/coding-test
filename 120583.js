// 중복된 숫자 개수
function solution(array, n) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] == n) {
      count++;
    }
  }
  return count;
}
console.log(solution([1, 1, 1, 1, 1, 1], 1));

// 다른사람풀이
function solution(array, n) {
  var answer = 0;
  let Array = array.filter((item) => item === n);
  answer = Array.length;

  return answer;
}
