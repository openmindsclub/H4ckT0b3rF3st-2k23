const colors = ["#008080", "#6A5ACD"];
const time = 5;
var lost = false;
var moveLeft = false,
  moveRight = false;
var x = 10,
  y = 200;
var stepX = 2,
  stepY = -2;
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var bar = {
  x: 100,
  y: 394,
  width: 100,
  height: 6,
};
document.body.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") moveLeft = true;
  else if (e.key === "ArrowRight") moveRight = true;
  else if (e.key === "Enter" && lost) {
    lost = false;
    x = 50;
    y = 50;
    stepX = 2;
    stepY = -2;
    document.getElementsByClassName("shutdown")[0].classList.remove("show");
    play();
  }
});
document.body.addEventListener("keyup", (e) => {
  if (e.key === "ArrowLeft") moveLeft = false;
  else if (e.key === "ArrowRight") moveRight = false;
});

const play = () => {
  var interval = setInterval(() => {
    if (!lost) {
      move();
      draw();
      if (
        ((x + 10 >= bar.x && x + 10 <= bar.x + bar.width) ||
          (x - 10 >= bar.x && x - 10 <= bar.x + bar.width)) &&
        y + 10 === bar.y
      ) {
        stepY *= -1;
        if (moveLeft && Math.sign(stepX) === 1) stepX *= -1;
        else if (moveRight && Math.sign(stepX) === -1) stepX *= -1;
      }
      if ((x + 10 === bar.x || x - 10 === bar.x + bar.width) && y + 10 > bar.y)
        stepX *= -1;

      if (x + 10 >= c.width || x - 10 <= 0) stepX *= -1;
      if (y - 10 <= 0) stepY *= -1;
      if (y + 10 > c.height + 20) lost = true;
    } else {
      console.log("lost");
      clearInterval(interval);
      shutdown();
    }
  }, time);
};

play();

function draw() {
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI * 2);
  ctx.fillStyle = "black";
  ctx.strokeStyle = "#000";
  ctx.stroke();
  ctx.fill();
  ctx.closePath();
  x += stepX;
  y += stepY;

  ctx.fillRect(bar.x, bar.y, bar.width, bar.height);
}

const move = () => {
  if (moveLeft) {
    if (bar.x > 0) bar.x -= 2;
  }
  if (moveRight) {
    if (bar.x + bar.width < c.width) bar.x += 2;
  }
};
const shutdown = () => {
  document.getElementsByClassName("shutdown")[0].classList.add("show");
};
