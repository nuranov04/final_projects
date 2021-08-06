const $dropdownButtonBtn = document.querySelector('.dropdownButtonBtn');

const $dropdownButtonDiv = document.querySelector('.dropdownButtonDiv');

$dropdownButtonBtn.addEventListener('click' , e => {
    e.preventDefault();

    $dropdownButtonDiv.classList.toggle('displayNone')
})