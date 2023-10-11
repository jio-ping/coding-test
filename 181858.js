// 무작위로 k개의 수 뽑기
function solution(arr, k) {
  noDuplicate = new Set(arr);
  console.log(noDuplicate);
  if (noDuplicate.size > k) {
    answer = [];
    for (let num of noDuplicate) {
      answer.push(num);
    }
  }
}

console.log(solution([0, 1, 1, 2, 2, 3], 3));
