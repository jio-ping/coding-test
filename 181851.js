// 전국대회선발고사
function solution(rank, attendance) {
  for (let i = 0; i < attendance.length; i++) {
    if (attendance[i] == false) {
      rank.remove(i);
    }
  }
  rank.sort();
  return rank[0] * 10000 + rank[1] + 100 + rank[2];
}

console.log(
  solution([3, 7, 2, 5, 4, 6, 1], [false, true, true, true, true, false, false])
);

//다른사람풀이
// function solution(rank, attendance) {
//   const [a, b, c] = rank
//     .map((r, i) => [r, i])
//     .filter(([_, i]) => attendance[i])
//     .sort(([a], [b]) => a - b);
//   return 10000 * a[1] + 100 * b[1] + c[1];
// }
