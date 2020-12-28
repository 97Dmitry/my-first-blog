const del = document.querySelector('#deleter')
del.addEventListener('click', function (event) {
    const confirme = confirm("Вы точно хотите удалить вашу запись?")
    if (confirme === true) {
        del
    } else {
        event.preventDefault()
    }
})
