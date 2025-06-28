let mem = [];
document.addEventListener('keydown', (event)=> {
    keyDown(event.key)
});
function keyDown(key) {
  if (key === '1') {
    mem.push(10)
  } else if (key === '2') {
    mem.push(20)
  } else if (key === '3') {
    mem.push(5)
  } else if (key === 'q') {
    mem.push(100)
  } else if (key === 'w') {
    mem.push(200)
  } else if (key === 'e') {
    mem.push(50)
  } else if (key === 'Backspace') {
    deleteLast()
  } else if (key === 'ji') {
    deleteLast()
  }

  console.log(mem.length)
  if (mem.length === 0) {
    document.querySelector('.js-osszeg').innerHTML = '0ft'
  } else {
    let i = 0
    let osszeg = 0

    while (i < mem.length) {
    osszeg += mem[i]
    i++
  }
  document.querySelector('.js-osszeg').innerHTML = osszeg+'ft'
  }
  
  
}

function reset() {
  mem = []
  document.querySelector('.js-osszeg').innerHTML = '0ft'
}
function deleteLast() {
  mem.splice(mem.length-1,1)
}