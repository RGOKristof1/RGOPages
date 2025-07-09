let all = Number(localStorage.getItem('all')) || 0;
console.log('local storage pulled')
document.getElementById('output').innerHTML = all;

function buttonClicked() {
  console.log('button clicked');
  let input = document.getElementById('number-input');
  let inputNumber = Number(document.getElementById('number-input').value);
  console.log('input took');
  console.log(inputNumber);
  input.value = '';
  console.log('input cleared');
  all += inputNumber;
  console.log('input added to all')
  console.log(all);
  localStorage.setItem('all',all);
  console.log('local storage refreshed');
  document.getElementById('output').innerHTML = all;
  console.log('output refreshed');
}

function clearThing() {
  console.log('button clickekkkes')
  all = 0;
  localStorage.setItem('all',all);
  console.log('cleared local storage');
  document.getElementById('output').innerHTML = all;
  console.log('output refreshed');
}