// let - змінна
// var - застарілий спосіб створення змінних
// const - константа, значення якої змінюватись не може 
// селектор - атрибути у html тегах під назвою class (.name_class) або id(#name_id)
const listLinks = document.querySelectorAll('.buy')
// python 
// for el in listLinks:
//     
// js
for (let count = 0; count < listLinks.length; count++){
    // python: button = listLinks[count]
    let button = listLinks[count]
    button.addEventListener(
        type = 'click',
        // Функція python: def назва_функції(параметри):
        // Функція - 1 JS: function (параметри){} - анонімна 
        // Функція - 2 JS: function назва_функції(параметри){} - іменована
        // Функція - 3 JS: (параметри) => {} - стрілочна
        listener = function (event){
            // Умова python: if умова :
            // умова JS: if (умова) {}
            if (document.cookie == ''){
                // динамічний рядок в python - f'{}'
                // динамічний рядок в js - `${}`
                document.cookie = `list_products = ${button.id}; path = /`
            }
            else{
                productId = document.cookie.split('=')[1]
                document.cookie = `list_products = ${productId} ${button.id}; path = /`
            }
        }
    )
}