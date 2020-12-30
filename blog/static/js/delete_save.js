const del = document.querySelector('#deleter')
del.addEventListener('click', function (event) {
    event.stopPropagation()
    const confirme = confirm("Вы точно хотите удалить вашу запись?")
    if (confirme === true) {
    } else {
        event.preventDefault()
    }
})

// const xhr = new XMLHttpRequest();
// xhr.open('GET', 'http://127.0.0.1:8000')
// xhr.addEventListener('load', () => {
//     console.log(xhr.getAllResponseHeaders())
// })
//
// xhr.send()