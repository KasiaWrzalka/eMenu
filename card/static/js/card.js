let globalState = {
    sort: 'id',
    page: 1
}

let sortButtons = document.querySelectorAll(".js-sort");
let pageButtons = document.querySelectorAll(".js-page");
let cardListItemTemplate = document.querySelector('.js-card-list-item-template');
let cardList = document.querySelector('.js-card-list');


Array.from(sortButtons).forEach(function(button) {
    button.addEventListener("click", function(elem) {
        Array.from(sortButtons).forEach(function(subElem){
            subElem.classList.remove('active');
        });
        elem.target.classList.add('active');
        globalState.sort = elem.target.dataset.sort;
        getData();
}, false);
});

Array.from(pageButtons).forEach(function(button) {
    button.addEventListener("click", function(elem) {
            Array.from(pageButtons).forEach(function(subElem){
            subElem.classList.remove('active');
        });
        elem.target.classList.add('active');
        globalState.page = elem.target.dataset.page;
        getData();
}, false);
});



function getData() {
    let query = Object.keys(globalState)
         .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(globalState[k]))
         .join('&');

    fetch('/get_cards/?' +  query)
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            render(jsonResponse);
        });

}

function render(data) {
    cardList.innerHTML = '';
    for(let item of data) {
        let newNode = cardListItemTemplate.cloneNode(true);
        newNode.classList.remove("js-card-list-item-template");
        newNode.classList.remove("card-list-item-template");
        let href = newNode.querySelector('.js-link').getAttribute('href');
        newNode.querySelector('.js-link').setAttribute('href', href + item.id);
        newNode.querySelector('.js-name').textContent = item.name;
        newNode.querySelector('.js-description').textContent = item.description;
        newNode.querySelector('.js-created_date').textContent = item.created_date;
        newNode.querySelector('.js-updated_date').textContent = item.updated_date;
        newNode.querySelector('.js-number_of_items').textContent = item.number_of_items;

        cardList.appendChild(newNode);
    }
}

getData();