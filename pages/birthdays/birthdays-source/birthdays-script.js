fetch('birthdays-source/birthdays-data.txt')
.then(
  function(valasz) {
    return valasz.text()
  }
)
.then(
  function(text) {
    console.log(text)
  }
)