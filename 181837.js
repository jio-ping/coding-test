// 커피심부름
const solution = (order) =>
  order.reduce(
    (acc, cur) => acc + (cur.includes("cafelatte") ? 5000 : 4500),
    0
  );
console.log(
  solution(["cafelatte", "americanoice", "hotcafelatte", "anything"])
);
