// 가까운 1 찾기
function solution(arr, idx) {
  for (idx; idx < arr.length; idx++) {
    if (arr[idx] == 1) {
      return idx;
    }
  }
  return -1;
}

console.log(solution([1, 1, 1, 1, 0], 3));
