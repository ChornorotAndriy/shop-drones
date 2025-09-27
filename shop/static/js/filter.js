// let doc = document.querySelector()
$(document).ready(function(){
    $('#filter').on('click', function(){
        $.ajax({
            contentType: 'application/json',
            url: "/shop/filter",
            type: 'post',
            data: $('#select').val(),
            success: function(response){
                // 1 
                // $('#products').html('')
                // 2
                $('#products').empty()
                // 
                for (let product of response['products']){
                    let productDiv = $('<div>', {class: 'product'})
                    productDiv.append($('<hr>'))
                    productDiv.append($('<img>', {src: `/shop/static/images/products/${product.product_name}.png`, width: '300px', height: '300px'}))
                    productDiv.append($('<h4>', {text: 'Назва продукту: ' + product.product_name}))
                    productDiv.append($('<p>', {text: 'Ціна продукту: ' + product.price}))
                    productDiv.append($('<p>', {text: 'знижка на продукт: ' + product.discount}))
                    productDiv.append($('<p>', {text: 'Кількість продукту: ' + product.count}))
                    productDiv.append($('<p>', {text: 'Опис продукту: ' + product.description}))
                    productDiv.append($('<button>', {class: "buy", id: `${product.id}`, type:"button", text: "buy"}))

                    productDiv.append($('<hr>'))
                    
                    if(response['is_admin']) {
                        productDiv.append($('<a>', {href: `/delete_product?id=${product.product_id}`, text: 'Delete'}))
                    }
                    $("#products").append(productDiv)
                }
                // let html = ''
                // response['products'].forEach(product => {
                //     html += `
                //         <div class = 'product'>
                //             <hr>
                //             <img src="/shop/static/images/products/${product.product_name }.png" alt="${product.product_name}" width="300px" height="300px">
                //             <h4>Назва продукту: ${product.product_name}</h4>
                //         </div>
                //     ` 
                // });
                // $('#products').html(html)
            }
        })
    })
})