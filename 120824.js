// 짝수 홀수 개수
function solution(num_list) {
  let even_count = 0;
  for (let i = 0; i < num_list.length; i++) {
    if (num_list[i] % 2 == 0) {
      even_count += 1;
    }
  }
  return [even_count, num_list.length - even_count];
}
solution([1, 2, 3, 4, 5]);
